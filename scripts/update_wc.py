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

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

# ── Config ───────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("FOOTBALL_DATA_API_KEY", "")
API_BASE = "https://api.football-data.org/v4"
COMPETITION = "WC"

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
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")
    files = ["state.json"] + (extra_files or [])
    checkout("main")
    commit_and_push("main", f"chore: update results ({state['updated'][:10]})", files)


# ── API ───────────────────────────────────────────────────────────────────────

def api_get(path: str, params: dict | None = None) -> dict:
    resp = requests.get(
        f"{API_BASE}{path}",
        headers={"X-Auth-Token": API_KEY},
        params=params,
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json()


def fetch_matches() -> list[dict]:
    return api_get(f"/competitions/{COMPETITION}/matches").get("matches", [])


def fetch_standings() -> dict[str, list]:
    """Returns {group_letter: [table_entry, ...]}."""
    try:
        data = api_get(f"/competitions/{COMPETITION}/standings")
        result: dict[str, list] = {}
        for s in data.get("standings", []):
            if s.get("type") == "TOTAL":
                letter = s.get("group", "").replace("GROUP_", "")
                result[letter] = s.get("table", [])
        return result
    except Exception:
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

    if git_log:
        lines += [
            "\n## Git Log\n",
            "```text",
            git_log.rstrip(),
            "```",
        ]

    return "\n".join(lines)


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
    if commit_already_exists(branch, f"Group {g}.*{date}"):
        return

    checkout(branch, create_from="main")
    processed = set(state["processed_ids"] + [m["id"]])
    visible = [x for x in all_group if x.get("group", "").replace("GROUP_", "") == g and x["id"] in processed]

    path = REPO_ROOT / "groups" / f"group_{g}.md"
    path.parent.mkdir(exist_ok=True)
    path.write_text(group_md(g, visible, standings.get(g)))

    md = m.get("matchday", "?")
    h, a, s = tname(m["homeTeam"]), tname(m["awayTeam"]), fmt_score(m)
    msg = f"Group {g}, MD{md}: {h} {s} {a} ({date})"
    commit_and_push(branch, msg, [f"groups/group_{g}.md"])
    print(f"  ✓ {msg}")


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
    if not API_KEY:
        print("Error: FOOTBALL_DATA_API_KEY environment variable is not set.", file=sys.stderr)
        print("Get a free key at https://www.football-data.org/client/register", file=sys.stderr)
        sys.exit(1)

    setup_git()
    print("🌍 World Cup 2026 Git Updater")
    print("=" * 40)

    checkout("main")
    git(["fetch", "--all", "--prune"])
    state = load_state()

    print("\n📁 Ensuring group branches...")
    ensure_group_branches(state)

    print("\n📡 Fetching data from football-data.org...")
    try:
        matches = fetch_matches()
        standings = fetch_standings()
    except requests.HTTPError as exc:
        print(f"API error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"  {len(matches)} total matches")

    processed_ids = set(state.get("processed_ids", []))
    finished = [m for m in matches if m["status"] == "FINISHED"]
    new_matches = sorted(
        [m for m in finished if m["id"] not in processed_ids],
        key=lambda m: m["utcDate"],
    )
    print(f"  {len(finished)} finished, {len(new_matches)} new to process")

    all_group = [m for m in matches if m["stage"] == "GROUP_STAGE"]

    # Group stage
    new_group = [m for m in new_matches if m["stage"] == "GROUP_STAGE"]
    if new_group:
        print(f"\n⚽ Processing {len(new_group)} group-stage match(es)...")
        for m in new_group:
            process_group_match(m, state, all_group, standings)
            state["processed_ids"].append(m["id"])

    # KO stage
    new_ko = [m for m in new_matches if m["stage"] in KO_STAGES]
    if new_ko:
        print("\n🏟️  Ensuring team branches...")
        checkout("main")
        ensure_team_branches(matches, state)

        print(f"\n🔥 Processing {len(new_ko)} knockout match(es)...")
        for m in new_ko:
            process_ko_match(m, state, matches)
            state["processed_ids"].append(m["id"])

    # Update README + state on main
    print("\n💾 Saving state and updating README...")
    checkout("main")
    git_log = git(["log", "--graph", "--oneline", "--all"])
    (REPO_ROOT / "README.md").write_text(readme_md(matches, state, git_log))
    save_state(state, extra_files=["README.md"])

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
