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
- **Matches played**: 60 / 104
- **Last updated**: 2026-06-26 09:27 UTC

## Groups

- **Group A**: 6/6 played → `group/A`
- **Group B**: 6/6 played → `group/B`
- **Group C**: 6/6 played → `group/C`
- **Group D**: 6/6 played → `group/D`
- **Group E**: 6/6 played → `group/E`
- **Group F**: 6/6 played → `group/F`
- **Group G**: 4/6 played → `group/G`
- **Group H**: 4/6 played → `group/H`
- **Group I**: 4/6 played → `group/I`
- **Group J**: 4/6 played → `group/J`
- **Group K**: 4/6 played → `group/K`
- **Group L**: 4/6 played → `group/L`

## GitGraph (mermaid)

```mermaid
---
config:
  gitGraph:
    parallelCommits: false
---
gitGraph LR:
  commit id: "init"
  branch group/A order: 1
  checkout main
  branch group/B order: 2
  checkout main
  branch group/C order: 3
  checkout main
  branch group/D order: 4
  checkout main
  branch group/E order: 5
  checkout main
  branch group/F order: 6
  checkout main
  branch group/G order: 7
  checkout main
  branch group/H order: 8
  checkout main
  branch group/I order: 9
  checkout main
  branch group/J order: 10
  checkout main
  branch group/K order: 11
  checkout main
  branch group/L order: 12
  checkout main
  checkout group/G
  commit id: "initialize Group G"
  commit id: "Belgium 1-1 Egypt (2026-06-15)"
  commit id: "Iran 2-2 New Zealand (2026-06-16)"
  commit id: "Belgium 0-0 Iran (2026-06-21)"
  commit id: "New Zealand 1-3 Egypt (2026-06-22)"
  checkout group/H
  commit id: "initialize Group H"
  commit id: "Spain 0-0 Cape Verde (2026-06-15)"
  commit id: "Saudi Arabia 1-1 Uruguay (2026-06-15"
  commit id: "Spain 4-0 Saudi Arabia (2026-06-21)"
  commit id: "Uruguay 2-2 Cape Verde (2026-06-21)"
  checkout group/I
  commit id: "initialize Group I"
  commit id: "France 3-1 Senegal (2026-06-16)"
  commit id: "Iraq 1-4 Norway (2026-06-16)"
  commit id: "France 3-0 Iraq (2026-06-22)"
  commit id: "Norway 3-2 Senegal (2026-06-23)"
  checkout group/J
  commit id: "initialize Group J"
  commit id: "Argentina 3-0 Algeria (2026-06-17)"
  commit id: "Austria 3-1 Jordan (2026-06-17)"
  commit id: "Argentina 2-0 Austria (2026-06-22)"
  commit id: "Jordan 1-2 Algeria (2026-06-23)"
  checkout group/L
  commit id: "initialize Group L"
  commit id: "England 4-2 Croatia (2026-06-17)"
  commit id: "Ghana 1-0 Panama (2026-06-17)"
  commit id: "England 0-0 Ghana (2026-06-23)"
  commit id: "Panama 0-1 Croatia (2026-06-23)"
  checkout group/K
  commit id: "initialize Group K"
  commit id: "Portugal 1-1 Congo DR (2026-06-17)"
  commit id: "Uzbekistan 1-3 Colombia (2026-06-18)"
  commit id: "Portugal 5-0 Uzbekistan (2026-06-23)"
  commit id: "Colombia 1-0 Congo DR (2026-06-24)"
  checkout group/A
  commit id: "initialize Group A"
  commit id: "Mexico 2-0 South Africa (2026-06-11)"
  commit id: "Korea Republic 2-1 Czechia (2026-06-"
  commit id: "Czechia 1-1 South Africa (2026-06-18"
  commit id: "Mexico 1-0 Korea Republic (2026-06-1"
  commit id: "Czechia 0-3 Mexico (2026-06-25)"
  commit id: "South Africa 1-0 Korea Republic (202"
  checkout main
  merge group/A id: "MEX, RSA advance (#11)"
  checkout group/B
  commit id: "initialize Group B"
  commit id: "Canada 1-1 Bosnia-H. (2026-06-12)"
  commit id: "Qatar 1-1 Switzerland (2026-06-13)"
  commit id: "Switzerland 4-1 Bosnia-H. (2026-06-1"
  commit id: "Canada 6-0 Qatar (2026-06-18)"
  commit id: "Switzerland 2-1 Canada (2026-06-24)"
  commit id: "Bosnia-H. 3-1 Qatar (2026-06-24)"
  checkout main
  merge group/B id: "SUI, CAN advance (#12)"
  checkout group/C
  commit id: "initialize Group C"
  commit id: "Brazil 1-1 Morocco (2026-06-13)"
  commit id: "Haiti 0-1 Scotland (2026-06-14)"
  commit id: "Scotland 0-1 Morocco (2026-06-19)"
  commit id: "Brazil 3-0 Haiti (2026-06-20)"
  commit id: "Morocco 4-2 Haiti (2026-06-24)"
  commit id: "Scotland 0-3 Brazil (2026-06-24)"
  checkout main
  merge group/C id: "BRA, MAR advance (#13)"
  commit id: "infer group branch tips from merge commit sub"
  commit id: "fetch all remote branches with wildcard refsp"
  commit id: "prevent merging of sibling branches by only f"
  checkout group/D
  commit id: "initialize Group D"
  commit id: "USA 4-1 Paraguay (2026-06-13)"
  commit id: "Australia 2-0 Turkey (2026-06-14)"
  commit id: "USA 2-0 Australia (2026-06-19)"
  commit id: "Turkey 0-1 Paraguay (2026-06-20)"
  commit id: "Turkey 3-2 USA (2026-06-26)"
  commit id: "Paraguay 0-0 Australia (2026-06-26)"
  checkout main
  merge group/D id: "USA, AUS advance (#14)"
  checkout group/E
  commit id: "initialize Group E"
  commit id: "Germany 7-1 Curaçao (2026-06-14)"
  commit id: "Ivory Coast 1-0 Ecuador (2026-06-14)"
  commit id: "Germany 2-1 Ivory Coast (2026-06-20)"
  commit id: "Ecuador 0-0 Curaçao (2026-06-21)"
  commit id: "Ecuador 2-1 Germany (2026-06-25)"
  commit id: "Curaçao 0-2 Ivory Coast (2026-06-25)"
  checkout main
  merge group/E id: "GER, CIV, ECU advance (#15)"
  checkout group/F
  commit id: "initialize Group F"
  commit id: "Netherlands 2-2 Japan (2026-06-14)"
  commit id: "Sweden 5-1 Tunisia (2026-06-15)"
  commit id: "Netherlands 5-1 Sweden (2026-06-20)"
  commit id: "Tunisia 0-4 Japan (2026-06-21)"
  commit id: "Tunisia 1-3 Netherlands (2026-06-25)"
  commit id: "Japan 1-1 Sweden (2026-06-25)"
  checkout main
  merge group/F id: "NED, JPN, SWE advance (#16)"
```

## Git Log

```text
* c3a80fa Change parallelCommits setting to false
* 622fb7b chore: update results (2026-06-26)
* 4c84768 Fix typo in variable name for commit IDs
* 3279c6c Fix type hint syntax for all_commit_ids variable
* bc49820 Append commit ID to all_commit_ids list
* dddd7fc Fix function definition syntax in update_wc.py
* 332da53 Update update_wc.py
* fd70bea chore: update results (2026-06-26)
* 80722e0 Update update_wc.py
* 2e5027e chore: update results (2026-06-26)
* fe06e7d Update starting_commit in state.json
* 387fa14 chore: update results (2026-06-26)
* 9acabe8 chore: update results (2026-06-26)
* 1ae3674 Update third_place.md
* b48e1cc Add Ecuador team to third place standings
* 701f697 Add third place standings markdown file
* d6351b3 chore: update results (2026-06-26)
*   b2474ad Group F: NED, JPN, SWE advance (#16)
|\  
| * 3fb3b66 Group F, MD3: Japan 1-1 Sweden (2026-06-25)
| * d3f08c9 Group F, MD3: Tunisia 1-3 Netherlands (2026-06-25)
| * 37486e3 Group F, MD2: Tunisia 0-4 Japan (2026-06-21)
| * 62cfd94 Group F, MD2: Netherlands 5-1 Sweden (2026-06-20)
| * a3802dd Group F, MD1: Sweden 5-1 Tunisia (2026-06-15)
| * 55a2a87 Group F, MD1: Netherlands 2-2 Japan (2026-06-14)
| * f136fe6 feat: initialize Group F
* |   e2a060a Group E: GER, CIV, ECU advance (#15)
|\ \  
| * | 1e58c16 Group E, MD3: Curaçao 0-2 Ivory Coast (2026-06-25)
| * | 3a01352 Group E, MD3: Ecuador 2-1 Germany (2026-06-25)
| * | 54ae035 Group E, MD2: Ecuador 0-0 Curaçao (2026-06-21)
| * | fd81778 Group E, MD2: Germany 2-1 Ivory Coast (2026-06-20)
| * | 7948bbe Group E, MD1: Ivory Coast 1-0 Ecuador (2026-06-14)
| * | 6256d77 Group E, MD1: Germany 7-1 Curaçao (2026-06-14)
| * | cd1b6fc feat: initialize Group E
| |/  
* |   6f49e3c Group D: USA, AUS advance (#14)
|\ \  
| * | a0a688a Group D, MD3: Paraguay 0-0 Australia (2026-06-26)
| * | 6fa6b3a Group D, MD3: Turkey 3-2 USA (2026-06-26)
| * | e28a6dc Group D, MD2: Turkey 0-1 Paraguay (2026-06-20)
| * | f307f62 Group D, MD2: USA 2-0 Australia (2026-06-19)
| * | d9483dc Group D, MD1: Australia 2-0 Turkey (2026-06-14)
| * | 3829793 Group D, MD1: USA 4-1 Paraguay (2026-06-13)
| * | da0de21 feat: initialize Group D
| |/  
* | 8aae2fe chore: update results (2026-06-26)
* | 0bd3a04 chore: update results (2026-06-25)
* | 9985da4 Update update_wc.py
* | 14b7d30 chore: update results (2026-06-25)
* |   5d95d20 fix: prevent merging of sibling branches by only following the first … (#24)
|\ \  
| * | 5c03e0c fix: prevent merging of sibling branches by only following the first parent in commit history
|/ /  
* | 672d35f Update update-results.yml
* | e273890 Add debug logging for branches and SHA mapping
* | af871da Fix formatting in git_output_cmd command
* | 65c5589 Refactor git log commands in update_wc.py
* | 2567c42 chore: update results (2026-06-25)
* |   234a479 Fix group branches missing from Mermaid GitGraph due to narrow fetch refspec (#23)
|\ \  
| * | 8dba9b3 Remove the merge guessing
| * | 0917a6d fix: fetch all remote branches with wildcard refspec in workflow
| * | adcc7d8 fix: infer group branch tips from merge commit subjects when branch refs are deleted
|/ /  
* | 95d2fbb chore: update results (2026-06-25)
* | 20bb335 Update state.json
* |   1853711 Group C: BRA, MAR advance (#13)
|\ \  
| * | 1e63230 Group C, MD3: Scotland 0-3 Brazil (2026-06-24)
| * | 914859e Group C, MD3: Morocco 4-2 Haiti (2026-06-24)
| * | 713ade3 Group C, MD2: Brazil 3-0 Haiti (2026-06-20)
| * | 1ea95ac Group C, MD2: Scotland 0-1 Morocco (2026-06-19)
| * | cae8412 Group C, MD1: Haiti 0-1 Scotland (2026-06-14)
| * | 4c1fb49 Group C, MD1: Brazil 1-1 Morocco (2026-06-13)
| * | de0ccc8 feat: initialize Group C
| |/  
* |   582cdde Group B: SUI, CAN advance (#12)
|\ \  
| * | 0a60654 Group B, MD3: Bosnia-H. 3-1 Qatar (2026-06-24)
| * | c1e4c7e Group B, MD3: Switzerland 2-1 Canada (2026-06-24)
| * | 3357170 Group B, MD2: Canada 6-0 Qatar (2026-06-18)
| * | 2f0881b Group B, MD2: Switzerland 4-1 Bosnia-H. (2026-06-18)
| * | d12dfee Group B, MD1: Qatar 1-1 Switzerland (2026-06-13)
| * | 647c3f3 Group B, MD1: Canada 1-1 Bosnia-H. (2026-06-12)
| * | 73fea82 feat: initialize Group B
| |/  
* |   2601f9a Group A: MEX, RSA advance (#11)
|\ \  
| * | fb7d903 Group A, MD3: South Africa 1-0 Korea Republic (2026-06-25)
| * | 1276260 Group A, MD3: Czechia 0-3 Mexico (2026-06-25)
| * | f768041 Group A, MD2: Mexico 1-0 Korea Republic (2026-06-19)
| * | dbc69ea Group A, MD2: Czechia 1-1 South Africa (2026-06-18)
| * | 777a2b6 Group A, MD1: Korea Republic 2-1 Czechia (2026-06-12)
| * | 612b691 Group A, MD1: Mexico 2-0 South Africa (2026-06-11)
| * | b22d60b feat: initialize Group A
| |/  
* | e5c328e chore: update results (2026-06-25)
* | 63ecdfc Update update_wc.py
* | 2452db4 chore: update results (2026-06-25)
* | 09b3863 Update update_wc.py
* | 58eaddf Update update_wc.py
* | d795d15 chore: update results (2026-06-25)
* | 766e2f9 chore: update results (2026-06-24)
* | 44b4375 chore: update results (2026-06-24)
* | c9ac0a0 Disable scheduled updates for World Cup results
* | 3363bd4 chore: update results (2026-06-24)
* | 33f3158 chore: update results (2026-06-24)
* | 69a9d9b chore: update results (2026-06-24)
* | e9982f7 Update update_wc.py
* | d97b331 chore: update results (2026-06-24)
* | e5a5a17 Add commit id to gitGraph command output
* | e1b30f2 chore: update results (2026-06-24)
* | ef8924b chore: update results (2026-06-24)
* | 9b9ffa2 chore: update results (2026-06-24)
* | e8d508e chore: update results (2026-06-23)
* | 211ffde Update update_wc.py
* | a4c4ecc chore: update results (2026-06-23)
* | 0dae92a chore: update results (2026-06-23)
* | b4349ce Update state.json
* | 28444af chore: update results (2026-06-23)
* | 0226e32 Allow display of chore commits in update_wc.py
* | 0827645 Update starting_commit in state.json
* | e37f30d chore: update results (2026-06-23)
* | f027d96 Update starting_commit in state.json
* | 9bb0204 chore: update results (2026-06-23)
* | c6254c2 Update starting_commit in state.json
* | 795f227 chore: update results (2026-06-23)
* | 2eb25c8 Update starting_commit to new commit hash
|/  
| * f5de9cc Group K, MD2: Colombia 1-0 Congo DR (2026-06-24)
| * 6143609 Group K, MD2: Portugal 5-0 Uzbekistan (2026-06-23)
| * 03093dc Group K, MD1: Uzbekistan 1-3 Colombia (2026-06-18)
| * 9e313b3 Group K, MD1: Portugal 1-1 Congo DR (2026-06-17)
| * 682f112 feat: initialize Group K
|/  
| * 7551de5 Group L, MD2: Panama 0-1 Croatia (2026-06-23)
| * 6a430be Group L, MD2: England 0-0 Ghana (2026-06-23)
| * ab54662 Group L, MD1: Ghana 1-0 Panama (2026-06-17)
| * 9709b5e Group L, MD1: England 4-2 Croatia (2026-06-17)
| * 4ece383 feat: initialize Group L
|/  
| * 64f56fa Group J, MD2: Jordan 1-2 Algeria (2026-06-23)
| * a04bce5 Group J, MD2: Argentina 2-0 Austria (2026-06-22)
| * d62db80 Group J, MD1: Austria 3-1 Jordan (2026-06-17)
| * 555de8f Group J, MD1: Argentina 3-0 Algeria (2026-06-17)
| * 26d1524 feat: initialize Group J
|/  
| * 5a0f84e Group I, MD2: Norway 3-2 Senegal (2026-06-23)
| * 40fce23 Group I, MD2: France 3-0 Iraq (2026-06-22)
| * 432ca77 Group I, MD1: Iraq 1-4 Norway (2026-06-16)
| * 769feea Group I, MD1: France 3-1 Senegal (2026-06-16)
| * a28079d feat: initialize Group I
|/  
| * 041ba94 Group H, MD2: Uruguay 2-2 Cape Verde (2026-06-21)
| * 4187777 Group H, MD2: Spain 4-0 Saudi Arabia (2026-06-21)
| * b8d1966 Group H, MD1: Saudi Arabia 1-1 Uruguay (2026-06-15)
| * 0d818f0 Group H, MD1: Spain 0-0 Cape Verde (2026-06-15)
| * ea91a7b feat: initialize Group H
|/  
| * 1aa234b Group G, MD2: New Zealand 1-3 Egypt (2026-06-22)
| * 9a649da Group G, MD2: Belgium 0-0 Iran (2026-06-21)
| * 4198b88 Group G, MD1: Iran 2-2 New Zealand (2026-06-16)
| * 7f1d992 Group G, MD1: Belgium 1-1 Egypt (2026-06-15)
| * 9ba404e feat: initialize Group G
|/  
* ca7d95c chore: update results (2026-06-23)
* 29bcdac chore: update results (2026-06-23)
* 59ccdf1 chore: update results (2026-06-23)
* 2e629c7 chore: update results (2026-06-23)
* 3c96f35 Update update_wc.py
```