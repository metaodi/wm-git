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
- **Matches played**: 40 / 104
- **Last updated**: 2026-06-22 10:43 UTC

## Groups

- **Group A**: 4/6 played → `group/A`
- **Group B**: 4/6 played → `group/B`
- **Group C**: 4/6 played → `group/C`
- **Group D**: 4/6 played → `group/D`
- **Group E**: 4/6 played → `group/E`
- **Group F**: 4/6 played → `group/F`
- **Group G**: 4/6 played → `group/G`
- **Group H**: 4/6 played → `group/H`
- **Group I**: 2/6 played → `group/I`
- **Group J**: 2/6 played → `group/J`
- **Group K**: 2/6 played → `group/K`
- **Group L**: 2/6 played → `group/L`

## Git Log

```text
* 897cbd1 Group G, MD2: New Zealand 1-3 Egypt (2026-06-22)
* 89c1873 Group G, MD2: Belgium 0-0 Iran (2026-06-21)
* af7c2db Group G, MD1: Iran 2-2 New Zealand (2026-06-16)
* d6a3526 Group G, MD1: Belgium 1-1 Egypt (2026-06-15)
* bb6a8d0 feat: initialize Group G
| * 7434b24 Group H, MD2: Spain 4-0 Saudi Arabia (2026-06-21)
| * bf47c54 Group H, MD1: Spain 0-0 Cape Verde (2026-06-15)
| * 9b3f4a5 feat: initialize Group H
|/  
| * 2ed2b42 Group F, MD2: Tunisia 0-4 Japan (2026-06-21)
| * 34cb55b Group F, MD2: Netherlands 5-1 Sweden (2026-06-20)
| * f03deba Group F, MD1: Sweden 5-1 Tunisia (2026-06-15)
| * e3faf8f Group F, MD1: Netherlands 2-2 Japan (2026-06-14)
| * 6221114 feat: initialize Group F
|/  
| * 95cb151 Group E, MD2: Ecuador 0-0 Curaçao (2026-06-21)
| * bdc2b59 Group E, MD2: Germany 2-1 Ivory Coast (2026-06-20)
| * 29ffe4f Group E, MD1: Germany 7-1 Curaçao (2026-06-14)
| * 9b79d23 feat: initialize Group E
|/  
| * a4c9b2f Group D, MD2: Turkey 0-1 Paraguay (2026-06-20)
| * 36486fb Group D, MD2: USA 2-0 Australia (2026-06-19)
| * 1717375 Group D, MD1: Australia 2-0 Turkey (2026-06-14)
| * ea2ec87 Group D, MD1: USA 4-1 Paraguay (2026-06-13)
| * 3db2275 feat: initialize Group D
|/  
| * 894ce73 Group C, MD2: Brazil 3-0 Haiti (2026-06-20)
| * 3650e8d Group C, MD2: Scotland 0-1 Morocco (2026-06-19)
| * 74489a4 Group C, MD1: Haiti 0-1 Scotland (2026-06-14)
| * b63fc0b Group C, MD1: Brazil 1-1 Morocco (2026-06-13)
| * b5a3cc1 feat: initialize Group C
|/  
| * 31f09f8 Group A, MD2: Mexico 1-0 Korea Republic (2026-06-19)
| * 4e3fd65 Group A, MD2: Czechia 1-1 South Africa (2026-06-18)
| * 6ddc6f9 Group A, MD1: Korea Republic 2-1 Czechia (2026-06-12)
| * e97a374 Group A, MD1: Mexico 2-0 South Africa (2026-06-11)
| * c256116 feat: initialize Group A
|/  
| * 95e679a Group B, MD2: Switzerland 4-1 Bosnia-H. (2026-06-18)
| * d0ee5b9 Group B, MD1: Qatar 1-1 Switzerland (2026-06-13)
| * 1214368 Group B, MD1: Canada 1-1 Bosnia-H. (2026-06-12)
| * 9e56bce feat: initialize Group B
|/  
| * 2ff4bd0 Group K, MD1: Uzbekistan 1-3 Colombia (2026-06-18)
| * cf6cc8c Group K, MD1: Portugal 1-1 Congo DR (2026-06-17)
| * 366e4d3 feat: initialize Group K
|/  
| * 360006b Group L, MD1: England 4-2 Croatia (2026-06-17)
| * d8a2e99 feat: initialize Group L
|/  
| * f51e35b Group J, MD1: Argentina 3-0 Algeria (2026-06-17)
| * 13e1b64 feat: initialize Group J
|/  
| * b011f08 Group I, MD1: France 3-1 Senegal (2026-06-16)
| * d51a976 feat: initialize Group I
|/  
* 4434da5 Update state.json
* 63e0f08 chore: update results (2026-06-22)
*   b91b150 Merge pull request #7 from metaodi/copilot/define-starting-commit
|\  
| * 9a765ee feat: add starting_commit to state.json and use it for git log and GitGraph
|/  
*   13359cd Merge pull request #6 from metaodi/copilot/add-logging-to-update-wc-script
|\  
| * 454ac12 Address code review: use Counter and lazy debug evaluation
| * 1d0aec4 Add logging to update_wc.py at DEBUG level
|/  
* 7e590a1 chore: update results (2026-06-22)
* 235fda3 Clear processed_ids and update group_branches
```