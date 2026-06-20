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
- **Matches played**: 33 / 104
- **Last updated**: 2026-06-20 16:38 UTC

## Groups

- **Group A**: 4/6 played → `group/A`
- **Group B**: 4/6 played → `group/B`
- **Group C**: 4/6 played → `group/C`
- **Group D**: 4/6 played → `group/D`
- **Group E**: 2/6 played → `group/E`
- **Group F**: 3/6 played → `group/F`
- **Group G**: 2/6 played → `group/G`
- **Group H**: 2/6 played → `group/H`
- **Group I**: 2/6 played → `group/I`
- **Group J**: 2/6 played → `group/J`
- **Group K**: 2/6 played → `group/K`
- **Group L**: 2/6 played → `group/L`

## Git Log

```text
* 107697b Group F, MD2: Netherlands 5-1 Sweden (2026-06-20)
* 862025f Group F, MD1: Sweden 5-1 Tunisia (2026-06-15)
* 52628d1 Group F, MD1: Netherlands 2-2 Japan (2026-06-14)
* fd92970 feat: initialize Group F
| * 3dcb2ca Update update-results.yml
| * 9fc6ab4 chore: update results (2026-06-20)
| * a30ddc2 chore: update results (2026-06-20)
| * f4276fa chore: update results (2026-06-20)
| *   86d6c89 Merge pull request #2 from metaodi/copilot/add-git-log-to-readme
| |\  
| | * 112093a feat: add git log output to README when regenerating
| |/  
| * 9e81f0b Update update-results.yml
| * 6c75851 chore: update results (2026-06-20)
| * 4489135 chore: update results (2026-06-20)
|/  
| * dd95a20 Group D, MD2: Turkey 0-1 Paraguay (2026-06-20)
| * 4167627 Group D, MD2: USA 2-0 Australia (2026-06-19)
| * 113f996 Group D, MD1: Australia 2-0 Turkey (2026-06-14)
| * 4517e79 Group D, MD1: USA 4-1 Paraguay (2026-06-13)
| * 0a2d315 feat: initialize Group D
|/  
| * cc4d903 Group C, MD2: Brazil 3-0 Haiti (2026-06-20)
| * d087aec Group C, MD2: Scotland 0-1 Morocco (2026-06-19)
| * c526561 Group C, MD1: Haiti 0-1 Scotland (2026-06-14)
| * 6d492e0 Group C, MD1: Brazil 1-1 Morocco (2026-06-13)
| * 9b10018 feat: initialize Group C
|/  
| * b8c2d93 Group A, MD2: Mexico 1-0 Korea Republic (2026-06-19)
| * 7146f12 Group A, MD2: Czechia 1-1 South Africa (2026-06-18)
| * 06c0d30 Group A, MD1: Korea Republic 2-1 Czechia (2026-06-12)
| * 154f19a Group A, MD1: Mexico 2-0 South Africa (2026-06-11)
| * 54b8ae8 feat: initialize Group A
|/  
| * b109145 Group B, MD2: Switzerland 4-1 Bosnia-H. (2026-06-18)
| * dd8925c Group B, MD1: Qatar 1-1 Switzerland (2026-06-13)
| * 386a382 Group B, MD1: Canada 1-1 Bosnia-H. (2026-06-12)
| * 402b87e feat: initialize Group B
|/  
| * 867755e Group K, MD1: Uzbekistan 1-3 Colombia (2026-06-18)
| * a441ea5 Group K, MD1: Portugal 1-1 Congo DR (2026-06-17)
| * 97675b2 feat: initialize Group K
|/  
| * 265a1b9 Group L, MD1: England 4-2 Croatia (2026-06-17)
| * 9cc1858 feat: initialize Group L
|/  
| * f9449c6 Group J, MD1: Argentina 3-0 Algeria (2026-06-17)
| * 751d471 feat: initialize Group J
|/  
| * 6fe31c2 Group I, MD1: France 3-1 Senegal (2026-06-16)
| * c483c0f feat: initialize Group I
|/  
| * 41c7043 Group G, MD1: Iran 2-2 New Zealand (2026-06-16)
| * 2272ecc Group G, MD1: Belgium 1-1 Egypt (2026-06-15)
| * 91b73f4 feat: initialize Group G
|/  
| * 8a8a343 Group H, MD1: Spain 0-0 Cape Verde (2026-06-15)
| * 3325c9d feat: initialize Group H
|/  
| * 4e6728c Group E, MD1: Germany 7-1 Curaçao (2026-06-14)
| * 774420e feat: initialize Group E
|/  
*   b5c7791 Merge pull request #1 from metaodi/claude/world-cup-git-structure-mc792b
|\  
| * 7989c0a feat: World Cup 2026 git structure with auto-updating GitHub Action
|/  
* 6cb78b6 Initial commit
```