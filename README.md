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
- **Last updated**: 2026-06-22 07:23 UTC

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
* 7ea974f Group G, MD2: New Zealand 1-3 Egypt (2026-06-22)
* 0292d06 Group G, MD2: Belgium 0-0 Iran (2026-06-21)
* 9fe5679 Group G, MD1: Iran 2-2 New Zealand (2026-06-16)
* 4bcb958 Group G, MD1: Belgium 1-1 Egypt (2026-06-15)
* 4fa6992 feat: initialize Group G
| * 1effce9 Group H, MD2: Spain 4-0 Saudi Arabia (2026-06-21)
| * 3b60b61 Group H, MD1: Spain 0-0 Cape Verde (2026-06-15)
| * 8d519b9 feat: initialize Group H
|/  
| * 86dfe83 Group F, MD2: Tunisia 0-4 Japan (2026-06-21)
| * 787a2fe Group F, MD2: Netherlands 5-1 Sweden (2026-06-20)
| * 6a730be Group F, MD1: Sweden 5-1 Tunisia (2026-06-15)
| * 6d75801 Group F, MD1: Netherlands 2-2 Japan (2026-06-14)
| * cb1d3c2 feat: initialize Group F
|/  
| * cc9e668 Group E, MD2: Ecuador 0-0 Curaçao (2026-06-21)
| * 4440ac8 Group E, MD2: Germany 2-1 Ivory Coast (2026-06-20)
| * 4271257 Group E, MD1: Germany 7-1 Curaçao (2026-06-14)
| * f2c39f7 feat: initialize Group E
|/  
| * f3668e6 Group D, MD2: Turkey 0-1 Paraguay (2026-06-20)
| * 51403e6 Group D, MD2: USA 2-0 Australia (2026-06-19)
| * ad8aca4 Group D, MD1: Australia 2-0 Turkey (2026-06-14)
| * c9df3e8 Group D, MD1: USA 4-1 Paraguay (2026-06-13)
| * 5d6d02f feat: initialize Group D
|/  
| * da70817 Group C, MD2: Brazil 3-0 Haiti (2026-06-20)
| * b4936d9 Group C, MD2: Scotland 0-1 Morocco (2026-06-19)
| * 52ed795 Group C, MD1: Haiti 0-1 Scotland (2026-06-14)
| * 716d4c6 Group C, MD1: Brazil 1-1 Morocco (2026-06-13)
| * f63bbd5 feat: initialize Group C
|/  
| * 04aaf2e Group A, MD2: Mexico 1-0 Korea Republic (2026-06-19)
| * 30b6eaa Group A, MD2: Czechia 1-1 South Africa (2026-06-18)
| * fd554bb Group A, MD1: Korea Republic 2-1 Czechia (2026-06-12)
| * ca1f705 Group A, MD1: Mexico 2-0 South Africa (2026-06-11)
| * fdd6513 feat: initialize Group A
|/  
| * 821aa86 Group B, MD2: Switzerland 4-1 Bosnia-H. (2026-06-18)
| * ca52c1e Group B, MD1: Qatar 1-1 Switzerland (2026-06-13)
| * 1ee6800 Group B, MD1: Canada 1-1 Bosnia-H. (2026-06-12)
| * cd369b7 feat: initialize Group B
|/  
| * 9daed11 Group K, MD1: Uzbekistan 1-3 Colombia (2026-06-18)
| * 19d68ae Group K, MD1: Portugal 1-1 Congo DR (2026-06-17)
| * af1dac6 feat: initialize Group K
|/  
| * 81878fc Group L, MD1: England 4-2 Croatia (2026-06-17)
| * e52a297 feat: initialize Group L
|/  
| * 694e348 Group J, MD1: Argentina 3-0 Algeria (2026-06-17)
| * bac8b93 feat: initialize Group J
|/  
| * 60a3dff Group I, MD1: France 3-1 Senegal (2026-06-16)
| * ba69374 feat: initialize Group I
|/  
* 235fda3 Clear processed_ids and update group_branches
* caaa883 chore: update results (2026-06-22)
*   29dfaaa Merge pull request #5 from metaodi/copilot/set-favicon-to-trophy-emoji
|\  
| * 32578bb feat: add 🏆 emoji favicon for GitHub Pages
|/  
* 1ba51f6 Disable scheduled updates for World Cup results
* c9440fe chore: update results (2026-06-22)
* 80ceaaa Update update_wc.py
* e7623a1 chore: update results (2026-06-22)
*   5b1799d Merge pull request #4 from metaodi/copilot/order-group-branches-alphabetically
|\  
| * 79be4b5 fix: clarify _branch_order docstring (1-12, not 1-26, explain fallback 99)
| * 357f930 fix: order group/* branches alphabetically in Mermaid gitGraph
|/  
* a2e32a7 chore: update results (2026-06-22)
* 8cf3d8c Update update_wc.py
* 62f9d92 Update update_wc.py
* 73eee9f chore: update results (2026-06-22)
* 2979e64 Exclude specific commit message from display
* 9209ac7 Update update_wc.py
* f72b0ed chore: update results (2026-06-22)
* e7b47e4 Update upload-pages-artifact action version
* 8eb4272 Update update_wc.py
* c4a8c62 Update update-results.yml
* 26edf89 chore: update results (2026-06-22)
* 6e9dfc7 Update update_wc.py
* 52b048d chore: update results (2026-06-22)
*   390c892 Merge pull request #3 from metaodi/copilot/build-github-pages-website
|\  
| * f2dc49f fix: address code review comments (constant, accessibility, log cap)
| * 0b9b3a1 feat: add GitHub Pages site with groups, standings, and Mermaid GitGraph
|/  
* 10dbea3 chore: update results (2026-06-22)
* 5bd1536 chore: update results (2026-06-22)
* ea050b0 chore: update results (2026-06-21)
* 6290273 chore: update results (2026-06-21)
* f1f3203 chore: update results (2026-06-21)
* 66acebe chore: update results (2026-06-21)
* 61d63b9 chore: update results (2026-06-21)
* 3188ba6 chore: update results (2026-06-21)
* 58eaf13 chore: update results (2026-06-21)
* dbb2a8b chore: update results (2026-06-21)
* e978bc3 chore: update results (2026-06-21)
* edc9f58 chore: update results (2026-06-20)
* 69e4845 chore: update results (2026-06-20)
* 368c0a4 chore: update results (2026-06-20)
* 3dcb2ca Update update-results.yml
* 9fc6ab4 chore: update results (2026-06-20)
* a30ddc2 chore: update results (2026-06-20)
* f4276fa chore: update results (2026-06-20)
*   86d6c89 Merge pull request #2 from metaodi/copilot/add-git-log-to-readme
|\  
| * 112093a feat: add git log output to README when regenerating
|/  
* 9e81f0b Update update-results.yml
* 6c75851 chore: update results (2026-06-20)
* 4489135 chore: update results (2026-06-20)
*   b5c7791 Merge pull request #1 from metaodi/claude/world-cup-git-structure-mc792b
|\  
| * 7989c0a feat: World Cup 2026 git structure with auto-updating GitHub Action
|/  
* 6cb78b6 Initial commit
```