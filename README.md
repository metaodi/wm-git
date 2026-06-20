# 🏆 2026 FIFA World Cup in Git

This repository encodes the **2026 FIFA World Cup** as git history.
Match results are fetched automatically from [football-data.org](https://www.football-data.org/)
every 2 hours via a GitHub Action and committed to the appropriate branches.

## How it works

| Branch | Content |
|--------|---------|
| `group/A` … `group/L` | Group stage — each of the 6 matches per group is a commit updating the standings |
| `teams/TLA` | Created for each of the 32 qualifiers after the group stage ends |
| KO matches | **Merge commits** — the winner's branch absorbs the loser's, forming the bracket in the git graph |
| `main` | Receives the final merge commit when the champion is crowned |

```
main ──────────────────────────────────────── 🏆 Champion
                                                │
                                           Final merge
                                           ╱         ╲
                                        SF1           SF2
                                       ╱   ╲         ╱   ╲
                                     QF1   QF2     QF3   QF4
                                    ╱  ╲  ╱  ╲   ╱  ╲  ╱  ╲
                                   R32 matches ...
                                       │
                               group/A … group/L
                               (one commit per match)
```

```bash
# View the full tournament bracket as a git graph
git log --graph --oneline --all
```

## Setup

### 1. Get a free API key

Register at <https://www.football-data.org/client/register> (free tier covers the World Cup).

### 2. Add the secret to your GitHub repository

Go to **Settings → Secrets and variables → Actions → New repository secret**:

| Name | Value |
|------|-------|
| `FOOTBALL_DATA_API_KEY` | your key from step 1 |

### 3. The GitHub Action does the rest

The workflow (`.github/workflows/update-results.yml`) runs every 2 hours.
You can also trigger it manually from the **Actions** tab with the
**"Update World Cup Results"** workflow → **Run workflow**.

On the first run it will:
1. Create `group/A` through `group/L` branches
2. Replay **all** past match results as individual commits (the tournament started June 11)
3. Create team branches for the 32 qualifiers once the group stage is done
4. Add KO merge commits as those rounds are played

## Explore the repository

```bash
git clone https://github.com/metaodi/wm-git
cd wm-git
git fetch --all

# See every match result as a graph
git log --graph --oneline --all

# Follow one team through the tournament
git log --oneline teams/ARG

# See what happened in Group B
git log --oneline group/B

# Diff two consecutive group-stage commits
git show group/C
```

---

*Updated automatically by [update-results.yml](.github/workflows/update-results.yml)*
