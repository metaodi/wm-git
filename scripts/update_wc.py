#!/usr/bin/env python3
"""
World Cup 2026 git repository updater.

Structures the 2026 FIFA World Cup as git history:
  group/A .. group/L   — one commit per group-stage match
  teams/TLA            — created for the 32 qualifiers, merged during KO rounds
  main                 — receives the final merge when the champion is crowned

Usage:
  FOOTBALL_DATA_API_KEY=<key> python scripts/update_wc.py
"""

import argparse
import json
import logging
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from pprint import pformat

import requests

# ── Config ───────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("FOOTBALL_DATA_API_KEY", "")
API_BASE = "https://api.football-data.org/v4"
COMPETITION = "WC"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)
log = logging.getLogger(__name__)

DRY_RUN = False

REPO_ROOT = Path(
    subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
)
STATE_FILE = REPO_ROOT / "state.json"

KO_STAGES = ["LAST_32", "LAST_16", "QUARTER_FINALS", "SEMI_FINALS", "THIRD_PLACE", "FINAL"]

STAGE_LABEL = {
    "GROUP_STAGE": "Group Stage",
    "LAST_32": "Round of 32",
    "LAST_16": "Round of 16",
    "QUARTER_FINALS": "Quarter-finals",
    "SEMI_FINALS": "Semi-finals",
    "THIRD_PLACE": "Third Place Play-off",
    "FINAL": "Final",
}


# ── Git helpers ───────────────────────────────────────────────────────────────

def git(args: list[str], check: bool = True) -> str:
    r = subprocess.run(["git"] + args, cwd=REPO_ROOT, capture_output=True, text=True, check=check)
    return r.stdout.strip()


def setup_git():
    git(["config", "user.email", "worldcup-bot@github-actions"])
    git(["config", "user.name", "World Cup Bot"])


def branch_exists_local(name: str) -> bool:
    return subprocess.run(
        ["git", "rev-parse", "--verify", name], cwd=REPO_ROOT, capture_output=True
    ).returncode == 0


def branch_exists_remote(name: str) -> bool:
    return subprocess.run(
        ["git", "rev-parse", "--verify", f"origin/{name}"], cwd=REPO_ROOT, capture_output=True
    ).returncode == 0


def checkout(branch: str, create_from: str | None = None):
    """Switch to branch; track remote if available, else create fresh."""
    if branch_exists_local(branch):
        git(["checkout", branch])
    elif branch_exists_remote(branch):
        git(["checkout", "-b", branch, f"origin/{branch}"])
    else:
        if create_from:
            checkout(create_from)
        git(["checkout", "-b", branch])


def has_any_changes() -> bool:
    return bool(
        subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT
        ).returncode
    )


def commit_and_push(branch: str, message: str, files: list[str] | None = None):
    git(["add"] + (files if files else ["-A"]))
    if not has_any_changes():
        return  # nothing staged
    if DRY_RUN:
        log.info("[dry-run] would commit on %s: %s", branch, message)
        git(["reset", "HEAD"])
        return
    git(["commit", "-m", message])
    git(["push", "-u", "origin", branch])


def commit_already_exists(branch: str, grep: str) -> bool:
    if not branch_exists_local(branch) and not branch_exists_remote(branch):
        return False
    ref = branch if branch_exists_local(branch) else f"origin/{branch}"
    out = subprocess.run(
        ["git", "log", ref, "--oneline", f"--grep={grep}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    return bool(out.stdout.strip())


# ── State ─────────────────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"processed_ids": [], "group_branches": False, "team_branches": []}


def save_state(state: dict, extra_files: list[str] | None = None):
    """Write state.json (+ any extra files) and commit on main."""
    state["updated"] = datetime.now(timezone.utc).isoformat()
    if DRY_RUN:
        log.info("[dry-run] would save state and commit README/site on main")
        return
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
    files = ["state.json"] + (extra_files or [])
    checkout("main")
    commit_and_push("main", f"chore: update results ({state['updated'][:10]})", files)


# ── API ───────────────────────────────────────────────────────────────────────

def api_get(path: str, params: dict | None = None) -> dict:
    url = f"{API_BASE}{path}"
    log.debug("API request: GET %s params=%s", url, params)
    resp = requests.get(
        url,
        headers={"X-Auth-Token": API_KEY},
        params=params,
        timeout=20,
    )
    log.debug("API response: status=%d url=%s", resp.status_code, resp.url)
    resp.raise_for_status()
    data = resp.json()
    log.debug("API response body: %s", json.dumps(data)[:500])
    return data


def fetch_matches() -> list[dict]:
    log.debug("Fetching matches for competition %s", COMPETITION)
    matches = api_get(f"/competitions/{COMPETITION}/matches").get("matches", [])
    log.debug("Fetched %d matches", len(matches))
    return matches


def fetch_standings() -> dict[str, list]:
    """Returns {group_letter: [table_entry, ...]}."""
    log.debug("Fetching standings for competition %s", COMPETITION)
    try:
        data = api_get(f"/competitions/{COMPETITION}/standings")
        result: dict[str, list] = {}
        for s in data.get("standings", []):
            if s.get("type") == "TOTAL":
                letter = s.get("group", "").replace("GROUP_", "")
                result[letter] = s.get("table", [])
        log.debug("Fetched standings for %d group(s): %s", len(result), pformat(result))
        return result
    except Exception:
        log.debug("Failed to fetch standings", exc_info=True)
        return {}


# ── Content generators ────────────────────────────────────────────────────────

def tname(team: dict) -> str:
    return team.get("shortName") or team.get("tla") or team["name"]


def fmt_score(m: dict) -> str:
    ft = m["score"]["fullTime"]
    if ft.get("home") is None:
        return "vs"
    h, a = ft["home"], ft["away"]
    pen = m["score"].get("penalties") or {}
    if pen.get("home") is not None:
        return f"{h}-{a} (pen. {pen['home']}-{pen['away']})"
    return f"{h}-{a}"


def winner_tla(m: dict) -> str | None:
    pen = m["score"].get("penalties") or {}
    if pen.get("home") is not None:
        return m["homeTeam"]["tla"] if pen["home"] > pen["away"] else m["awayTeam"]["tla"]
    w = m["score"].get("winner", "")
    if w == "HOME_TEAM":
        return m["homeTeam"]["tla"]
    if w == "AWAY_TEAM":
        return m["awayTeam"]["tla"]
    return None


def result_icon(m: dict, tla: str) -> str:
    pen = m["score"].get("penalties") or {}
    w = m["score"].get("winner", "")
    if pen.get("home") is not None:
        w = "HOME_TEAM" if pen["home"] > pen["away"] else "AWAY_TEAM"
    if w == "DRAW":
        return "🤝"
    home_wins = w == "HOME_TEAM"
    is_home = m["homeTeam"]["tla"] == tla
    return "✅" if home_wins == is_home else "❌"


def group_md(letter: str, matches: list[dict], standings: list | None = None) -> str:
    lines = [f"# Group {letter} — 2026 FIFA World Cup\n"]
    if standings:
        lines += [
            "## Standings\n",
            "| # | Team | P | W | D | L | GF | GA | GD | Pts |",
            "|---|------|---|---|---|---|----|----|----|----|",
        ]
        for e in standings:
            t = tname(e["team"])
            lines.append(
                f"| {e['position']} | {t} | {e['playedGames']} | {e['won']} | "
                f"{e['draw']} | {e['lost']} | {e['goalsFor']} | {e['goalsAgainst']} | "
                f"{e['goalDifference']:+d} | **{e['points']}** |"
            )
        lines.append("")
    lines.append("## Matches\n")
    for m in sorted(matches, key=lambda x: x["utcDate"]):
        date = m["utcDate"][:10]
        icon = "✅" if m["status"] == "FINISHED" else "📅"
        lines.append(f"- {icon} **{tname(m['homeTeam'])} {fmt_score(m)} {tname(m['awayTeam'])}** ({date})")
    return "\n".join(lines) + "\n"


def team_md(tla: str, name: str, matches: list[dict], status: str = "") -> str:
    lines = [f"# {name} ({tla}) — 2026 FIFA World Cup\n"]
    if status:
        lines.append(f"**{status}**\n")
    lines.append("## Results\n")
    for m in sorted(matches, key=lambda x: x["utcDate"]):
        if m["status"] != "FINISHED":
            continue
        icon = result_icon(m, tla)
        stage = STAGE_LABEL.get(m["stage"], m["stage"])
        lines.append(
            f"- {icon} {tname(m['homeTeam'])} {fmt_score(m)} {tname(m['awayTeam'])} "
            f"— {stage} ({m['utcDate'][:10]})"
        )
    return "\n".join(lines) + "\n"


def readme_md(matches: list[dict], state: dict, git_log: str = "") -> str:
    finished = [m for m in matches if m["status"] == "FINISHED"]
    updated = state.get("updated", "N/A")[:16].replace("T", " ")
    active_stages = sorted({m["stage"] for m in finished})
    stage_str = ", ".join(STAGE_LABEL.get(s, s) for s in active_stages) or "Not started"
    starting_commit = state.get("starting_commit")
    mermaid_graph = generate_mermaid_gitgraph(starting_commit)

    lines = [
        "# 🏆 2026 FIFA World Cup in Git\n",
        "This repository encodes the **2026 FIFA World Cup** as git history.\n",
        "## How it works\n",
        "| Branch | Content |",
        "|--------|---------|",
        "| `group/A` … `group/L` | Group stage — each match is a commit updating the standings |",
        "| `teams/TLA` | Created for each of the 32 qualifiers after group stage |",
        "| KO matches | Merge commits — winner's branch absorbs loser's, forming the bracket |",
        "| `main` | Receives the final merge commit when the champion is crowned |\n",
        "```bash",
        "# View the full tournament bracket as a git graph",
        "git log --graph --oneline --all",
        "```\n",
        "## Status\n",
        f"- **Stage**: {stage_str}",
        f"- **Matches played**: {len(finished)} / {len(matches)}",
        f"- **Last updated**: {updated} UTC\n",
        "## Groups\n",
    ]

    groups: dict[str, list] = {}
    for m in matches:
        if m["stage"] == "GROUP_STAGE":
            g = m.get("group", "").replace("GROUP_", "")
            groups.setdefault(g, []).append(m)
    for letter in sorted(groups):
        done = sum(1 for m in groups[letter] if m["status"] == "FINISHED")
        lines.append(f"- **Group {letter}**: {done}/{len(groups[letter])} played → `group/{letter}`")

    ko = [m for m in finished if m["stage"] in KO_STAGES]
    if ko:
        lines.append("\n## Knockout Bracket\n")
        for stage in KO_STAGES:
            stage_ms = [m for m in ko if m["stage"] == stage]
            if not stage_ms:
                continue
            lines.append(f"### {STAGE_LABEL[stage]}\n")
            for m in sorted(stage_ms, key=lambda x: x["utcDate"]):
                w = winner_tla(m)
                adv = f" → **{w}**" if w else ""
                lines.append(
                    f"- {tname(m['homeTeam'])} {fmt_score(m)} {tname(m['awayTeam'])}{adv}"
                )
            lines.append("")
    if mermaid_graph:
        lines += [
            "\n## GitGraph (mermaid)\n",
            "```mermaid",
            mermaid_graph,
            "```",
        ]
    if git_log:
        lines += [
            "\n## Git Log\n",
            "```text",
            git_log.rstrip(),
            "```",
        ]

    return "\n".join(lines)


_MERMAID_SUBJECT_LEN = 50  # max chars of commit subject kept in Mermaid commit IDs


def generate_mermaid_gitgraph(starting_commit: str | None = None) -> str:
    """Parse the git DAG and produce Mermaid gitGraph syntax."""
    all_commit_ids = list[str] = []
    sep = "\x1f"
    try:
        cmd = ["git", "log", "--all", "--topo-order", "--reverse",
               f"--pretty=format:%H{sep}%P{sep}%D{sep}%s"]
        if starting_commit:
            cmd.append(f"{starting_commit}^..")
        raw = subprocess.check_output(
            cmd,
            cwd=REPO_ROOT, text=True, stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return 'gitGraph\n  commit id: "init"'

    if not raw:
        return 'gitGraph\n  commit id: "init"'

    commits: list[dict] = []
    sha_to_commit: dict[str, dict] = {}
    for line in raw.split("\n"):
        if not line:
            continue
        parts = line.split(sep, 3)
        if len(parts) < 4:
            continue
        sha, parents_raw, refs_raw, subject = parts
        parents = [p for p in parents_raw.split() if p]

        branch_refs: list[str] = []
        for ref in refs_raw.split(","):
            r = ref.strip()
            if not r or r == "HEAD":
                continue
            if " -> " in r:
                r = r.split(" -> ")[-1].strip()
            if r.startswith("origin/"):
                r = r[7:]
            if r and r != "HEAD":
                branch_refs.append(r)

        log.debug(f"Found the following branches: {branch_refs}")

        c: dict = dict(
            sha=sha,
            parents=parents,
            branch_refs=branch_refs,
            subject=subject[:_MERMAID_SUBJECT_LEN].replace('"', "'"),
        )
        commits.append(c)
        sha_to_commit[sha] = c

    # Assign each commit to a branch by walking backwards from tips.
    # Priority: main first (0), then group/* (1), then teams/* (2), other (3).
    sha_to_branch: dict[str, str] = {}

    tip_pairs: list[tuple[str, str]] = [
        (ref, c["sha"]) for c in commits for ref in c["branch_refs"]
    ]

    def _prio(name: str) -> int:
        if name == "main":
            return 0
        if name.startswith("group/"):
            return 1
        if name.startswith("teams/"):
            return 2
        return 3

    tip_pairs.sort(key=lambda x: (_prio(x[0]), x[0]))

    for branch, tip_sha in tip_pairs:
        stack = [tip_sha]
        while stack:
            sha = stack.pop()
            if sha in sha_to_branch:
                continue
            sha_to_branch[sha] = branch
            commit = sha_to_commit.get(sha)
            if commit and commit["parents"]:
                # Only follow the first parent so we don't bleed through merge
                # commit second-parents into sibling branches. Without this,
                # walking main's tip would cross into group/* commits via their
                # merge-parent and claim them for main before the group branch
                # walk gets a chance.
                p = commit["parents"][0]
                if p not in sha_to_branch:
                    stack.append(p)
    log.debug(f"SHA to branch: {pformat(sha_to_branch)}")

    def _branch_order(name: str) -> int:
        """Return a numeric order for Mermaid branch declarations.

        main is the implicit base (order 0); group/* branches get order 1-12
        sorted alphabetically (A=1 … L=12); teams/* and others follow after.
        An empty group suffix falls back to 99.
        """
        if name == "main":
            return 0
        if name.startswith("group/"):
            letter = name[6:].upper()
            return ord(letter[0]) - ord("A") + 1 if letter else 99
        if name.startswith("teams/"):
            return 100
        return 200

    # Emit gitGraph commands
    lines = [
      "---",
      "config:",
      "  gitGraph:",
      "    parallelCommits: true",
      "---",
      "gitGraph LR:",
      '  commit id: "init"'
    ]
    cur: str | None = None
    created: set[str] = set()
    
    def ensure_on(branch: str, parent_branch: str | None = None) -> None:
        nonlocal cur
        if branch not in created:
            pb = parent_branch if (parent_branch and parent_branch in created) else "main"
            if pb in created and pb != cur:
                lines.append(f'  checkout {pb}')
                cur = pb
            order = _branch_order(branch)
            lines.append(f'  branch {branch} order: {order}')
            created.add(branch)
            cur = branch
        elif branch != cur:
            lines.append(f'  checkout {branch}')
            cur = branch

    if not created:
        created.add("main")
        cur = "main"

    # create all group branches
    ensure_on("group/A", "main")
    ensure_on("group/B", "main")
    ensure_on("group/C", "main")
    ensure_on("group/D", "main")
    ensure_on("group/E", "main")
    ensure_on("group/F", "main")
    ensure_on("group/G", "main")
    ensure_on("group/H", "main")
    ensure_on("group/I", "main")
    ensure_on("group/J", "main")
    ensure_on("group/K", "main")
    ensure_on("group/L", "main")
    ensure_on("main", "main")
    
    for c in commits:
        sha = c["sha"]
        branch = sha_to_branch.get(sha, "main")
        parents = c["parents"]
        subject = c["subject"]
        short = sha[:7]
      
        _, _, result = subject.partition(":")
        subject = result.strip()

        if not subject or 'update results' in subject:
            continue

        # prevent commits with the same id
        if subject in all_commits_ids:
            continue

        par_branch = sha_to_branch.get(parents[0]) if parents else None
        ensure_on(branch, par_branch)

        if len(parents) > 1:
            mb = sha_to_branch.get(parents[1])
            if mb and mb in created and mb != branch:
                lines.append(f'  merge {mb} id: "{subject}"')
            else:
                lines.append(f'  commit id: "{subject}"')
        else:
            lines.append(f'  commit id: "{subject}"')

        all_commit_ids.append(subject)

    return "\n".join(lines)


def html_site(matches: list[dict], standings: dict[str, list], state: dict) -> str:
    """Generate the full GitHub Pages HTML for the tournament."""
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    updated = state.get("updated", "")[:16].replace("T", " ")
    finished_count = sum(1 for m in matches if m["status"] == "FINISHED")
    total_count = len(matches)

    # ── Mermaid gitGraph ──────────────────────────────────────────────────────
    starting_commit = state.get("starting_commit")
    mermaid_graph = generate_mermaid_gitgraph(starting_commit)

    # ── ASCII git log (capped to avoid huge pages as history grows) ────────────
    git_log_cmd = ["log", "--graph", "--oneline", "--all", "--max-count=150"]
    if starting_commit:
        git_log_cmd.append(f"{starting_commit}^..")
    git_log_ascii = git(git_log_cmd)

    # ── Groups ────────────────────────────────────────────────────────────────
    groups: dict[str, list] = {}
    for m in matches:
        if m["stage"] == "GROUP_STAGE":
            g = m.get("group", "").replace("GROUP_", "")
            if g:
                groups.setdefault(g, []).append(m)

    groups_html_parts: list[str] = []
    for letter in sorted(groups):
        gm = sorted(groups[letter], key=lambda x: x["utcDate"])
        stand = standings.get(f"Group {letter}", [])
        done = sum(1 for m in gm if m["status"] == "FINISHED")

        table_rows = ""
        for e in stand:
            t = tname(e["team"])
            gd = e["goalDifference"]
            table_rows += (
                f"<tr><td>{e['position']}</td><td><strong>{t}</strong></td>"
                f"<td>{e['playedGames']}</td><td>{e['won']}</td><td>{e['draw']}</td>"
                f"<td>{e['lost']}</td><td>{gd:+d}</td><td><strong>{e['points']}</strong></td></tr>"
            )
        table_html = (
            f"<table aria-label='Group {letter} standings'><thead><tr>"
            "<th scope='col'>#</th><th scope='col'>Team</th><th scope='col'>P</th>"
            "<th scope='col'>W</th><th scope='col'>D</th><th scope='col'>L</th>"
            "<th scope='col'>GD</th><th scope='col'>Pts</th>"
            f"</tr></thead><tbody>{table_rows}</tbody></table>"
            if table_rows else ""
        )

        match_items = ""
        for m in gm:
            date = m["utcDate"][:10]
            icon = "✅" if m["status"] == "FINISHED" else "📅"
            match_items += (
                f"<li>{icon} <strong>{tname(m['homeTeam'])} {fmt_score(m)} "
                f"{tname(m['awayTeam'])}</strong> "
                f"<span class='date'>({date})</span></li>"
            )

        groups_html_parts.append(
            f"<section class='group' id='group-{letter}'>"
            f"<h3>Group {letter} <span class='branch-tag'>group/{letter}</span></h3>"
            f"<p class='played'>{done}/{len(gm)} played</p>"
            f"{table_html}"
            f"<ul class='matches'>{match_items}</ul>"
            f"</section>"
        )
    groups_html = "\n".join(groups_html_parts)

    # ── Knockout stage ────────────────────────────────────────────────────────
    ko_matches = [m for m in matches if m["stage"] in KO_STAGES and m["status"] == "FINISHED"]
    ko_html = ""
    if ko_matches:
        ko_parts: list[str] = ["<section class='knockout'><h2>Knockout Stage</h2>"]
        for stage in KO_STAGES:
            stage_ms = sorted(
                [m for m in ko_matches if m["stage"] == stage],
                key=lambda x: x["utcDate"],
            )
            if not stage_ms:
                continue
            ko_parts.append(f"<h3>{STAGE_LABEL[stage]}</h3><ul class='matches'>")
            for m in stage_ms:
                w = winner_tla(m)
                adv = f" → <strong>{w}</strong>" if w else ""
                ko_parts.append(
                    f"<li>✅ <strong>{tname(m['homeTeam'])} {fmt_score(m)} "
                    f"{tname(m['awayTeam'])}</strong>{adv} "
                    f"<span class='date'>({m['utcDate'][:10]})</span></li>"
                )
            ko_parts.append("</ul>")
        ko_parts.append("</section>")
        ko_html = "\n".join(ko_parts)

    clone_cmd = f"git clone https://github.com/{repo}.git && git log --graph --oneline --all" if repo else "git log --graph --oneline --all"
    github_link = f'<a href="https://github.com/{repo}" style="font-size:.6em;font-weight:400;vertical-align:middle" title="View on GitHub">GitHub</a>' if repo else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>2026 FIFA World Cup in Git</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🏆</text></svg>">
  <script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
  <style>
    *{{box-sizing:border-box;margin:0;padding:0}}
    body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
         background:#0d1117;color:#c9d1d9;max-width:1400px;margin:0 auto;padding:1.5rem 2rem}}
    h1{{color:#f0f6fc;border-bottom:2px solid #21262d;padding-bottom:.75rem;margin-bottom:1rem;font-size:1.8rem}}
    h2{{color:#e6edf3;margin:2rem 0 .75rem;font-size:1.3rem}}
    h3{{color:#c9d1d9;margin:.75rem 0 .4rem;font-size:1rem}}
    a{{color:#58a6ff}}
    .status{{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:1rem 1.25rem;
             margin-bottom:1.5rem;display:flex;gap:1.5rem;flex-wrap:wrap;align-items:center}}
    .status code{{background:#21262d;padding:2px 6px;border-radius:4px;font-size:.8rem}}
    .stat{{font-size:.95rem}}
    .stat strong{{color:#f0f6fc}}
    .last-updated{{color:#7d8590;font-size:.8rem}}
    .groups-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(480px,1fr));gap:1.25rem;margin-top:.5rem}}
    .group{{background:#161b22;border:1px solid #30363d;border-radius:6px;padding:1.25rem}}
    .branch-tag{{background:#1f6feb22;border:1px solid #1f6feb66;color:#58a6ff;
                 border-radius:4px;padding:1px 7px;font-size:.72rem;font-family:monospace}}
    .played{{color:#7d8590;font-size:.8rem;margin-bottom:.5rem}}
    table{{border-collapse:collapse;width:100%;font-size:.82rem;margin:.4rem 0 .9rem}}
    th,td{{text-align:left;padding:5px 8px;border-bottom:1px solid #21262d}}
    th{{background:#21262d;color:#7d8590;font-weight:600}}
    tr:hover td{{background:#21262d}}
    ul.matches{{list-style:none;padding:0}}
    ul.matches li{{padding:3px 0;border-bottom:1px solid #161b22;font-size:.82rem}}
    .date{{color:#7d8590;font-size:.78rem}}
    .knockout{{background:#161b22;border:1px solid #30363d;border-radius:6px;
               padding:1.25rem;margin-bottom:1.5rem}}
    details{{background:#161b22;border:1px solid #30363d;border-radius:6px;
             padding:.75rem 1.25rem;margin-top:1rem}}
    summary{{cursor:pointer;color:#e6edf3;font-weight:600;font-size:.95rem;padding:.25rem 0}}
    summary:hover{{color:#f0f6fc}}
    .gitgraph-wrap{{overflow-x:auto;padding-top:.75rem}}
    .mermaid{{background:transparent!important}}
    pre.git-log{{background:#0d1117;border:1px solid #21262d;border-radius:4px;
                 padding:.75rem;overflow-x:auto;font-size:.7rem;line-height:1.45;
                 color:#7ee787;margin-top:.75rem}}
  </style>
</head>
<body>
  <h1>🏆 2026 FIFA World Cup in Git {github_link}</h1>

  <div class="status">
    <span class="stat">⚽ <strong>{finished_count}</strong> / <strong>{total_count}</strong> matches played</span>
    <span class="last-updated">Updated: {updated} UTC</span>
    <span class="stat" style="margin-left:auto"><code>{clone_cmd}</code></span>
  </div>

  <h2>Git DAG</h2>
  <details open>
    <summary>Mermaid GitGraph</summary>
    <div class="gitgraph-wrap">
      <div class="mermaid">
{mermaid_graph}
      </div>
    </div>
  </details>
  <details>
    <summary>ASCII Git Log</summary>
    <pre class="git-log">{git_log_ascii}</pre>
  </details>

  <script>
    mermaid.initialize({{
      startOnLoad: true,
      theme: 'dark',
      gitGraph: {{ rotateCommitLabel: true, parallelCommits: true, showBranches: true }}
    }});
  </script>

  {ko_html}

  <h2>Groups</h2>
  <div class="groups-grid">
    {groups_html}
  </div>

  
</body>
</html>
"""


# ── Branch management ─────────────────────────────────────────────────────────

def ensure_group_branches(state: dict):
    if state.get("group_branches"):
        return
    checkout("main")
    for letter in "ABCDEFGHIJKL":
        branch = f"group/{letter}"
        if branch_exists_local(branch) or branch_exists_remote(branch):
            continue
        checkout(branch, create_from="main")
        path = REPO_ROOT / "groups" / f"group_{letter}.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text(f"# Group {letter} — 2026 FIFA World Cup\n\nNo matches played yet.\n")
        commit_and_push(branch, f"feat: initialize Group {letter}")
        print(f"  ✓ branch created: {branch}")
    checkout("main")
    state["group_branches"] = True


def process_group_match(m: dict, state: dict, all_group: list[dict], standings: dict):
    g = m.get("group", "").replace("GROUP_", "")
    if not g:
        return
    branch = f"group/{g}"
    date = m["utcDate"][:10]

    # Idempotency: skip if commit already exists for this match
    if commit_already_exists(branch, f"Group {g}.*{tname(m["homeTeam"])}.*{tname(m["awayTeam"])}.*{date}"):
        return

    checkout(branch, create_from="main")
    processed = set(state["processed_ids"] + [m["id"]])
    visible = [x for x in all_group if x.get("group", "").replace("GROUP_", "") == g and x["id"] in processed]

    path = REPO_ROOT / "groups" / f"group_{g}.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text(group_md(g, visible, standings.get(f"Group {g}")))

    md = m.get("matchday", "?")
    h, a, s = tname(m["homeTeam"]), tname(m["awayTeam"]), fmt_score(m)
    msg = f"Group {g}, MD{md}: {h} {s} {a} ({date})"
    commit_and_push(branch, msg, [f"groups/group_{g}.md"])
    print(f"  ✓ {msg}")


def group_is_complete(letter: str, matches: list[dict]) -> bool:
    """Return True when every match in the group is finished."""
    group_matches = [
        m for m in matches
        if m["stage"] == "GROUP_STAGE" and m.get("group", "").replace("GROUP_", "") == letter
    ]
    return bool(group_matches) and all(m["status"] == "FINISHED" for m in group_matches)


def group_merge_commit_msg(letter: str, group_standings: list, qualified_tlas: set[str]) -> str:
    """Build a --no-ff merge commit message for the end of a group stage.

    Shows the final standings table and marks which teams advance to the KO round.
    ``qualified_tlas`` should contain only TLAs from this group that are known to
    have qualified; pass an empty set when the best-third-place draw hasn't happened yet.
    """
    assert group_standings and len(group_standings), "No group standings available"
    advancing = [tname(e["team"]) for e in group_standings if e["team"]["tla"] in qualified_tlas]
    summary = f" — {' & '.join(advancing)} advance" if advancing else ""
    lines = [f"merge: Group {letter} complete{summary}\n", "Final standings:"]
    for e in group_standings:
        t = tname(e["team"])
        pts, w, d, l = e["points"], e["won"], e["draw"], e["lost"]
        gd = e["goalDifference"]
        tla = e["team"]["tla"]
        if qualified_tlas:
            icon = "✅" if tla in qualified_tlas else "❌"
        else:
            # KO draw hasn't happened yet — top 2 are guaranteed, 3rd is TBD
            icon = "✅" if e["position"] <= 2 else "⏳"
        lines.append(f"  {e['position']}. {t:<20} {pts:2d} pts  (W{w} D{d} L{l}, {gd:+d})  {icon}")
    if advancing:
        lines.append(f"\nAdvancing to Round of 32: {', '.join(advancing)}")
    return "\n".join(lines)


def merge_group_branch_to_main(letter: str, group_standings: list, matches: list[dict], state: dict):
    """Merge group/letter into main with a commit message showing the final standings."""
    branch = f"group/{letter}"
    if not branch_exists_local(branch) and not branch_exists_remote(branch):
        log.debug("Group branch %s does not exist, skipping merge", branch)
        return

    # Determine which teams from this group qualified for the KO stage
    ko_tlas: set[str] = {
        t["tla"]
        for m in matches if m["stage"] in KO_STAGES
        for t in (m["homeTeam"], m["awayTeam"])
    }
    group_tlas: set[str] = {
        t["tla"]
        for m in matches
        if m["stage"] == "GROUP_STAGE" and m.get("group", "").replace("GROUP_", "") == letter
        for t in (m["homeTeam"], m["awayTeam"])
    }
    qualified_in_group = ko_tlas & group_tlas

    msg = group_merge_commit_msg(letter, group_standings, qualified_in_group)
    checkout("main")
    if DRY_RUN:
        log.info("[dry-run] would merge group/%s → main: %s", letter, msg.splitlines()[0])
        state.setdefault("merged_groups", []).append(letter)
        print(f"  [dry-run] would merge group/{letter} → main")
        return
    r = subprocess.run(
        ["git", "merge", "--no-ff", branch, "-m", msg],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if r.returncode != 0:
        log.debug("Merge conflict for %s, falling back to ours strategy: %s", branch, r.stderr)
        subprocess.run(["git", "merge", "--abort"], cwd=REPO_ROOT, check=False)
        subprocess.run(
            ["git", "merge", "--no-ff", "-s", "ours", branch, "-m", msg],
            cwd=REPO_ROOT, check=True,
        )
    git(["push", "origin", "main"])
    state.setdefault("merged_groups", []).append(letter)
    print(f"  ✓ merged group/{letter} → main")


def ensure_team_branches(matches: list[dict], state: dict):
    """Create teams/TLA branches off their group branch for every team in the KO stage."""
    ko_teams: dict[str, dict] = {}
    for m in matches:
        if m["stage"] in KO_STAGES:
            for key in ("homeTeam", "awayTeam"):
                t = m[key]
                ko_teams[t["tla"]] = t

    tla_to_group: dict[str, str] = {}
    for m in matches:
        if m["stage"] == "GROUP_STAGE":
            g = m.get("group", "").replace("GROUP_", "")
            tla_to_group[m["homeTeam"]["tla"]] = g
            tla_to_group[m["awayTeam"]["tla"]] = g

    for tla, team in ko_teams.items():
        if tla in state.get("team_branches", []):
            continue
        group = tla_to_group.get(tla)
        if not group:
            continue
        branch = f"teams/{tla}"
        if branch_exists_local(branch) or branch_exists_remote(branch):
            state.setdefault("team_branches", []).append(tla)
            continue

        # Branch from the final state of the group branch
        checkout(f"group/{group}", create_from="main")
        git(["checkout", "-b", branch])

        all_team = [x for x in matches if x["homeTeam"]["tla"] == tla or x["awayTeam"]["tla"] == tla]
        (REPO_ROOT / "teams").mkdir(exist_ok=True)
        (REPO_ROOT / "teams" / f"{tla}.md").write_text(
            team_md(tla, team.get("name", tla), all_team, "Round of 32")
        )
        commit_and_push(branch, f"feat: {team.get('shortName', tla)} advances to Round of 32", [f"teams/{tla}.md"])
        state.setdefault("team_branches", []).append(tla)
        print(f"  ✓ team branch: {branch} (from group/{group})")


def process_ko_match(m: dict, state: dict, all_matches: list[dict]):
    htla, atla = m["homeTeam"]["tla"], m["awayTeam"]["tla"]
    wtla = winner_tla(m)
    if not wtla:
        print(f"  ⚠ no winner yet for {htla} vs {atla}")
        return
    ltla = atla if wtla == htla else htla

    wb, lb = f"teams/{wtla}", f"teams/{ltla}"
    stage = STAGE_LABEL.get(m["stage"], m["stage"])
    h, a, s = tname(m["homeTeam"]), tname(m["awayTeam"]), fmt_score(m)
    msg = f"{stage}: {h} {s} {a} ({m['utcDate'][:10]})"

    # Idempotency
    if commit_already_exists(wb, stage):
        return

    for branch in (wb, lb):
        if not branch_exists_local(branch) and not branch_exists_remote(branch):
            print(f"  ⚠ missing branch {branch}, skipping {msg}")
            return

    processed = set(state["processed_ids"] + [m["id"]])

    # Mark loser as eliminated
    checkout(lb)
    lteam = m["awayTeam"] if wtla == htla else m["homeTeam"]
    lmatches = [x for x in all_matches if (x["homeTeam"]["tla"] == ltla or x["awayTeam"]["tla"] == ltla) and x["id"] in processed]
    (REPO_ROOT / "teams" / f"{ltla}.md").write_text(
        team_md(ltla, lteam.get("name", ltla), lmatches, f"❌ Eliminated in {stage}")
    )
    commit_and_push(lb, f"eliminated: {ltla} exits at {stage}", [f"teams/{ltla}.md"])

    # Update winner and merge loser branch → creates the bracket edge in git graph
    checkout(wb)
    wteam = m["homeTeam"] if wtla == htla else m["awayTeam"]
    wmatches = [x for x in all_matches if (x["homeTeam"]["tla"] == wtla or x["awayTeam"]["tla"] == wtla) and x["id"] in processed]
    (REPO_ROOT / "teams" / f"{wtla}.md").write_text(
        team_md(wtla, wteam.get("name", wtla), wmatches, stage)
    )

    if DRY_RUN:
        log.info("[dry-run] would merge %s → %s: %s", lb, wb, msg)
        print(f"  [dry-run] would merge: {msg}")
        if m["stage"] == "FINAL":
            champion = wteam.get("shortName") or wtla
            print(f"  [dry-run] would merge {wb} → main: 🏆 World Cup 2026 Champion: {champion}!")
        return

    git(["add", f"teams/{wtla}.md"])

    r = subprocess.run(
        ["git", "merge", "--no-ff", lb, "-m", msg],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    if r.returncode != 0:
        # Conflict resolution: keep our content
        subprocess.run(["git", "merge", "--abort"], cwd=REPO_ROOT)
        subprocess.run(["git", "merge", "--no-ff", "-s", "ours", lb, "-m", msg], cwd=REPO_ROOT, check=True)
        # Restore our updated files after ours-merge
        (REPO_ROOT / "teams" / f"{wtla}.md").write_text(
            team_md(wtla, wteam.get("name", wtla), wmatches, stage)
        )
        git(["add", "-A"])
        git(["commit", "--amend", "--no-edit"])

    git(["push", "-u", "origin", wb])
    print(f"  ✓ merge: {msg}")

    if m["stage"] == "FINAL":
        checkout("main")
        champion = wteam.get("shortName") or wtla
        subprocess.run(
            ["git", "merge", "--no-ff", wb, "-m", f"🏆 World Cup 2026 Champion: {champion}!"],
            cwd=REPO_ROOT, check=True,
        )
        git(["push", "origin", "main"])
        print(f"  🏆 Champion merged to main: {champion}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    global DRY_RUN
    parser = argparse.ArgumentParser(description="World Cup 2026 git repository updater.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch data and show what would be done, but make no commits or pushes.",
    )
    args = parser.parse_args()
    DRY_RUN = args.dry_run

    if not API_KEY:
        print("Error: FOOTBALL_DATA_API_KEY environment variable is not set.", file=sys.stderr)
        print("Get a free key at https://www.football-data.org/client/register", file=sys.stderr)
        sys.exit(1)

    setup_git()
    log.debug("Git configured for World Cup bot")
    print("🌍 World Cup 2026 Git Updater" + (" [DRY RUN]" if DRY_RUN else ""))
    print("=" * 40)

    checkout("main")
    git(["fetch", "--all", "--prune"])
    state = load_state()
    log.debug("Loaded state: processed_ids=%d, group_branches=%s, team_branches=%s",
              len(state.get("processed_ids", [])),
              state.get("group_branches"),
              state.get("team_branches", []))

    print("\n📁 Ensuring group branches...")
    ensure_group_branches(state)

    print("\n📡 Fetching data from football-data.org...")
    try:
        matches = fetch_matches()
        standings = fetch_standings()
    except requests.HTTPError as exc:
        log.debug("HTTP error fetching API data: %s", exc, exc_info=True)
        print(f"API error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"  {len(matches)} total matches")
    if log.isEnabledFor(logging.DEBUG):
        log.debug("Match statuses: %s", dict(Counter(m["status"] for m in matches)))

    processed_ids = set(state.get("processed_ids", []))
    finished = [m for m in matches if m["status"] == "FINISHED"]
    new_matches = sorted(
        [m for m in finished if m["id"] not in processed_ids],
        key=lambda m: m["utcDate"],
    )
    print(f"  {len(finished)} finished, {len(new_matches)} new to process")
    if log.isEnabledFor(logging.DEBUG):
        log.debug("New matches to process: %s", [f"{m['homeTeam']['tla']} vs {m['awayTeam']['tla']} ({m['utcDate'][:10]})" for m in new_matches])

    all_group = [m for m in matches if m["stage"] == "GROUP_STAGE"]

    # Group stage
    new_group = [m for m in new_matches if m["stage"] == "GROUP_STAGE"]
    if new_group:
        print(f"\n⚽ Processing {len(new_group)} group-stage match(es)...")
        for m in new_group:
            log.debug("Processing group match id=%s: %s vs %s (%s)", m["id"], m["homeTeam"]["tla"], m["awayTeam"]["tla"], m["utcDate"][:10])
            process_group_match(m, state, all_group, standings)
            state["processed_ids"].append(m["id"])

    # Merge completed group branches into main
    merged_groups = set(state.get("merged_groups", []))
    groups_to_merge = [
        letter for letter in "ABCDEFGHIJKL"
        if letter not in merged_groups and group_is_complete(letter, matches)
    ]
    if groups_to_merge:
        print(f"\n🔀 Merging {len(groups_to_merge)} completed group branch(es) into main...")
        checkout("main")
        for letter in groups_to_merge:
            log.debug("Merging group/%s into main", letter)
            # merge_group_branch_to_main(letter, standings.get(f"Group {letter}", []), matches, state)

    # KO stage
    new_ko = [m for m in new_matches if m["stage"] in KO_STAGES]
    if new_ko:
        print("\n🏟️  Ensuring team branches...")
        checkout("main")
        ensure_team_branches(matches, state)

        print(f"\n🔥 Processing {len(new_ko)} knockout match(es)...")
        for m in new_ko:
            log.debug("Processing KO match id=%s stage=%s: %s vs %s (%s)", m["id"], m["stage"], m["homeTeam"]["tla"], m["awayTeam"]["tla"], m["utcDate"][:10])
            process_ko_match(m, state, matches)
            state["processed_ids"].append(m["id"])

    # Update README, site, and state on main
    print("\n💾 Saving state, updating README, and generating site...")
    checkout("main")
    starting_commit = state.get("starting_commit")
    git_log_cmd = ["log", "--graph", "--oneline", "--all"]
    sep = "\x1f"
    git_output_cmd = ["log", "--all", "--topo-order", "--reverse", f"--pretty=format:%H{sep}%P{sep}%D{sep}%s"]
  
    if starting_commit:
        git_log_cmd.append(f"{starting_commit}^..")
        git_output_cmd.append(f"{starting_commit}^..")
    git_log = git(git_log_cmd)
    git_output = git(git_output_cmd)
    print(f"Git Output:\n{git_output}")
    (REPO_ROOT / "README.md").write_text(readme_md(matches, state, git_log))
    docs_dir = REPO_ROOT / "docs"
    docs_dir.mkdir(exist_ok=True)
    (docs_dir / "index.html").write_text(html_site(matches, standings, state))
    save_state(state, extra_files=["README.md", "docs/index.html"])

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
