# 🏆 2026 FIFA World Cup in Git

This repository encodes the **2026 FIFA World Cup** as git history.

## How it works

| Branch | Content |
|--------|---------|
| `group/A` … `group/L` | Group stage — each match is a commit updating the standings |
| `teams/TLA` | Created for each of the 32 qualifiers after group stage |
| KO matches | Merge commits — winner's branch absorbs loser's, forming the bracket |
| `main` | Receives the final merge commit when the champion is crowned |

```bash
# View the full tournament bracket as a git graph
git log --graph --oneline --all
```

## Status

- **Stage**: Group Stage
- **Matches played**: 32 / 104
- **Last updated**: N/A UTC

## Groups

- **Group A**: 4/6 played → `group/A`
- **Group B**: 4/6 played → `group/B`
- **Group C**: 4/6 played → `group/C`
- **Group D**: 4/6 played → `group/D`
- **Group E**: 2/6 played → `group/E`
- **Group F**: 2/6 played → `group/F`
- **Group G**: 2/6 played → `group/G`
- **Group H**: 2/6 played → `group/H`
- **Group I**: 2/6 played → `group/I`
- **Group J**: 2/6 played → `group/J`
- **Group K**: 2/6 played → `group/K`
- **Group L**: 2/6 played → `group/L`