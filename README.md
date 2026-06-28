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
- **Matches played**: 72 / 104
- **Last updated**: 2026-06-28 06:17 UTC

## Groups

- **Group A**: 6/6 played → `group/A`
- **Group B**: 6/6 played → `group/B`
- **Group C**: 6/6 played → `group/C`
- **Group D**: 6/6 played → `group/D`
- **Group E**: 6/6 played → `group/E`
- **Group F**: 6/6 played → `group/F`
- **Group G**: 6/6 played → `group/G`
- **Group H**: 6/6 played → `group/H`
- **Group I**: 6/6 played → `group/I`
- **Group J**: 6/6 played → `group/J`
- **Group K**: 6/6 played → `group/K`
- **Group L**: 6/6 played → `group/L`

## GitGraph — Group Stage (Snapshot, mermaid)

```mermaid
---
config:
  gitGraph:
    parallelCommits: true
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
  commit id: "add modal to view mermaid GitGraph larger"
  commit id: "fullscreen modal for Mermaid GitGraph (#25)"
  checkout group/I
  commit id: "initialize Group I"
  commit id: "France 3-1 Senegal (2026-06-16)"
  commit id: "Iraq 1-4 Norway (2026-06-16)"
  commit id: "France 3-0 Iraq (2026-06-22)"
  commit id: "Norway 3-2 Senegal (2026-06-23)"
  commit id: "Norway 1-4 France (2026-06-26)"
  commit id: "Senegal 5-0 Iraq (2026-06-26)"
  checkout main
  merge group/I id: "FRA, NOR advance (#19)"
  checkout group/H
  commit id: "initialize Group H"
  commit id: "Spain 0-0 Cape Verde (2026-06-15)"
  commit id: "Saudi Arabia 1-1 Uruguay (2026-06-15"
  commit id: "Spain 4-0 Saudi Arabia (2026-06-21)"
  commit id: "Uruguay 2-2 Cape Verde (2026-06-21)"
  commit id: "Uruguay 0-1 Spain (2026-06-27)"
  commit id: "Cape Verde 0-0 Saudi Arabia (2026-06"
  checkout main
  merge group/H id: "ESP, CPV advance (#18)"
  checkout group/G
  commit id: "initialize Group G"
  commit id: "Belgium 1-1 Egypt (2026-06-15)"
  commit id: "Iran 2-2 New Zealand (2026-06-16)"
  commit id: "Belgium 0-0 Iran (2026-06-21)"
  commit id: "New Zealand 1-3 Egypt (2026-06-22)"
  commit id: "New Zealand 1-5 Belgium (2026-06-27)"
  commit id: "Egypt 1-2 Iran (2026-06-27)"
  checkout main
  merge group/G id: "BEL, EGY advance (#17)"
  checkout group/J
  commit id: "initialize Group J"
  commit id: "Argentina 3-0 Algeria (2026-06-17)"
  commit id: "Austria 3-1 Jordan (2026-06-17)"
  commit id: "Argentina 2-0 Austria (2026-06-22)"
  commit id: "Jordan 1-2 Algeria (2026-06-23)"
  commit id: "Jordan 1-3 Argentina (2026-06-28)"
  commit id: "Algeria 3-3 Austria (2026-06-28)"
  checkout main
  merge group/J id: "ARG, AUT, ALG advance (#20)"
  checkout group/K
  commit id: "initialize Group K"
  commit id: "Portugal 1-1 Congo DR (2026-06-17)"
  commit id: "Uzbekistan 1-3 Colombia (2026-06-18)"
  commit id: "Portugal 5-0 Uzbekistan (2026-06-23)"
  commit id: "Colombia 1-0 Congo DR (2026-06-24)"
  commit id: "Colombia 0-0 Portugal (2026-06-27)"
  commit id: "Congo DR 3-1 Uzbekistan (2026-06-27)"
  checkout main
  merge group/K id: "COL, POR, COD advance (#21)"
  checkout group/L
  commit id: "initialize Group L"
  commit id: "England 4-2 Croatia (2026-06-17)"
  commit id: "Ghana 1-0 Panama (2026-06-17)"
  commit id: "England 0-0 Ghana (2026-06-23)"
  commit id: "Panama 0-1 Croatia (2026-06-23)"
  commit id: "Panama 0-2 England (2026-06-27)"
  commit id: "Croatia 2-1 Ghana (2026-06-27)"
  checkout main
  merge group/L id: "ENG, CRO, GHA advance (#22)"
  commit id: "support commit range in mermaid GitGraph for"
  commit id: "address code review feedback on commit range"
  commit id: "bounded commit range for Mermaid GitGraph to"
```

## GitGraph — KO Stage (mermaid)

```mermaid
---
config:
  gitGraph:
    parallelCommits: true
---
gitGraph LR:
  commit id: "init"
  branch teams/RSA order: 101
  checkout main
  branch teams/CAN order: 102
  checkout main
  branch teams/BRA order: 103
  checkout main
  branch teams/JPN order: 104
  checkout main
  branch teams/GER order: 105
  checkout main
  branch teams/PAR order: 106
  checkout main
  branch teams/NED order: 107
  checkout main
  branch teams/MAR order: 108
  checkout main
  branch teams/CIV order: 109
  checkout main
  branch teams/NOR order: 110
  checkout main
  branch teams/FRA order: 111
  checkout main
  branch teams/SWE order: 112
  checkout main
  branch teams/MEX order: 113
  checkout main
  branch teams/ECU order: 114
  checkout main
  branch teams/ENG order: 115
  checkout main
  branch teams/COD order: 116
  checkout main
  branch teams/BEL order: 117
  checkout main
  branch teams/SEN order: 118
  checkout main
  branch teams/USA order: 119
  checkout main
  branch teams/BIH order: 120
  checkout main
  branch teams/ESP order: 121
  checkout main
  branch teams/AUT order: 122
  checkout main
  branch teams/POR order: 123
  checkout main
  branch teams/CRO order: 124
  checkout main
  branch teams/SUI order: 125
  checkout main
  branch teams/ALG order: 126
  checkout main
  branch teams/AUS order: 127
  checkout main
  branch teams/EGY order: 128
  checkout main
  branch teams/ARG order: 129
  checkout main
  branch teams/CPV order: 130
  checkout main
  branch teams/COL order: 131
  checkout main
  branch teams/GHA order: 132
  checkout main
  checkout teams/RSA
  commit id: "South Africa advances to Round of 32"
  checkout teams/CAN
  commit id: "Canada advances to Round of 32"
  checkout teams/BRA
  commit id: "Brazil advances to Round of 32"
  checkout teams/JPN
  commit id: "Japan advances to Round of 32"
  checkout teams/GER
  commit id: "Germany advances to Round of 32"
  checkout teams/PAR
  commit id: "Paraguay advances to Round of 32"
  checkout teams/NED
  commit id: "Netherlands advances to Round of 32"
  checkout teams/MAR
  commit id: "Morocco advances to Round of 32"
  checkout teams/CIV
  commit id: "Ivory Coast advances to Round of 32"
  checkout teams/NOR
  commit id: "Norway advances to Round of 32"
  checkout teams/FRA
  commit id: "France advances to Round of 32"
  checkout teams/SWE
  commit id: "Sweden advances to Round of 32"
  checkout teams/MEX
  commit id: "Mexico advances to Round of 32"
  checkout teams/ECU
  commit id: "Ecuador advances to Round of 32"
  checkout teams/ENG
  commit id: "England advances to Round of 32"
  checkout teams/COD
  commit id: "Congo DR advances to Round of 32"
  checkout teams/BEL
  commit id: "Belgium advances to Round of 32"
  checkout teams/SEN
  commit id: "Senegal advances to Round of 32"
  checkout teams/USA
  commit id: "USA advances to Round of 32"
  checkout teams/BIH
  commit id: "Bosnia-H. advances to Round of 32"
  checkout teams/ESP
  commit id: "Spain advances to Round of 32"
  checkout teams/AUT
  commit id: "Austria advances to Round of 32"
  checkout teams/POR
  commit id: "Portugal advances to Round of 32"
  checkout teams/CRO
  commit id: "Croatia advances to Round of 32"
  checkout teams/SUI
  commit id: "Switzerland advances to Round of 32"
  checkout teams/ALG
  commit id: "Algeria advances to Round of 32"
  checkout teams/AUS
  commit id: "Australia advances to Round of 32"
  checkout teams/EGY
  commit id: "Egypt advances to Round of 32"
  checkout teams/ARG
  commit id: "Argentina advances to Round of 32"
  checkout teams/CPV
  commit id: "Cape Verde advances to Round of 32"
  checkout teams/COL
  commit id: "Colombia advances to Round of 32"
  checkout teams/GHA
  commit id: "Ghana advances to Round of 32"
  checkout main
  commit id: "support commit range in mermaid GitGraph for"
  commit id: "address code review feedback on commit range"
  commit id: "bounded commit range for Mermaid GitGraph to"
  commit id: "create team branches after group stage and o"
  commit id: "create team branches post-group-stage and or"
```

## Git Log

```text
* facc459 Enhance debug logging for fetched matches
* c2b9053 chore: update results (2026-06-28)
*   bc27e9a feat: create team branches post-group-stage and order GitGraph by bracket (#27)
|\  
| * 19a1d7b feat: create team branches after group stage and order them by bracket in GitGraph
|/  
* c1b4427 chore: update results (2026-06-28)
* 6b629d8 Add ending_commit field to state.json
* f18185d chore: update results (2026-06-28)
*   6bba9dc feat: bounded commit range for Mermaid GitGraph to preserve group stage snapshot (#26)
|\  
| * b29ac47 fix: address code review feedback on commit range GitGraph feature
| * 73c3da7 feat: support commit range in mermaid GitGraph for group stage snapshot
|/  
* f3c37a8 Update Ghana team status with checkmark
* 8bf4695 Rearrange teams in third place standings
* a6a2976 Update standings in third_place.md
* 5d5cd1b chore: update results (2026-06-28)
*   c9b1c6a Group L: ENG, CRO, GHA advance (#22)
|\  
* \   3e29db3 Group K: COL, POR, COD advance (#21)
|\ \  
* \ \   3d49e70 Group J: ARG, AUT, ALG advance (#20)
|\ \ \  
* | | | 122e90f chore: update results (2026-06-28)
* | | | 2c38269 chore: update results (2026-06-27)
* | | | d17b313 Enable parallel commits in gitGraph configuration
* | | | e845a12 Add Congo DR to third place standings
* | | | 1ee9c12 Add Uruguay to third place standings
* | | | a7ed900 Update third_place.md
* | | | d36044a Add Senegal's results to third place standings
* | | | ff1eee7 Add Iran's entry to the third place standings
* | | | fc045de Update group standings and match results
* | | | 66a20dd Mark Paraguay as qualified with a checkmark
* | | |   35e2cf4 Group G: BEL, EGY advance (#17)
|\ \ \ \  
* \ \ \ \   e3bea87 Group H: ESP, CPV advance (#18)
|\ \ \ \ \  
* | | | | | bf25afa chore: update results (2026-06-27)
* | | | | | 0f51768 chore: update results (2026-06-27)
* | | | | |   7cd5b66 Group I: FRA, NOR advance (#19)
|\ \ \ \ \ \  
* | | | | | | 4393b31 chore: update results (2026-06-26)
* | | | | | | 9265497 chore: update results (2026-06-26)
* | | | | | |   aeeb1f6 feat: fullscreen modal for Mermaid GitGraph (#25)
|\ \ \ \ \ \ \  
| * | | | | | | 7ea859d feat: add modal to view mermaid GitGraph larger
|/ / / / / / /  
* | | | | | | 991535c chore: update results (2026-06-26)
* | | | | | | 76c0d15 Update Congo DR entry to Senegal in standings
* | | | | | | 3cbda12 Add new teams and update standings in third_place.md
* | | | | | | 4c2d875 Add checkmarks to teams in standings
* | | | | | | c05297f Add Scotland to third place standings
* | | | | | | a795492 Add Algeria to third place standings
* | | | | | | ca6b833 Add Korea Republic to third place standings
* | | | | | | 78cb5f9 Add Croatia's entry to third place standings
* | | | | | | f8348b0 Add Paraguay to third place standings
* | | | | | | 7293832 chore: update results (2026-06-26)
* | | | | | | c3a80fa Change parallelCommits setting to false
* | | | | | | 622fb7b chore: update results (2026-06-26)
* | | | | | | 4c84768 Fix typo in variable name for commit IDs
* | | | | | | 3279c6c Fix type hint syntax for all_commit_ids variable
* | | | | | | bc49820 Append commit ID to all_commit_ids list
* | | | | | | dddd7fc Fix function definition syntax in update_wc.py
* | | | | | | 332da53 Update update_wc.py
* | | | | | | fd70bea chore: update results (2026-06-26)
* | | | | | | 80722e0 Update update_wc.py
* | | | | | | 2e5027e chore: update results (2026-06-26)
* | | | | | | fe06e7d Update starting_commit in state.json
* | | | | | | 387fa14 chore: update results (2026-06-26)
* | | | | | | 9acabe8 chore: update results (2026-06-26)
* | | | | | | 1ae3674 Update third_place.md
* | | | | | | b48e1cc Add Ecuador team to third place standings
* | | | | | | 701f697 Add third place standings markdown file
* | | | | | | d6351b3 chore: update results (2026-06-26)
* | | | | | |   b2474ad Group F: NED, JPN, SWE advance (#16)
|\ \ \ \ \ \ \  
* \ \ \ \ \ \ \   e2a060a Group E: GER, CIV, ECU advance (#15)
|\ \ \ \ \ \ \ \  
* \ \ \ \ \ \ \ \   6f49e3c Group D: USA, AUS advance (#14)
|\ \ \ \ \ \ \ \ \  
* | | | | | | | | | 8aae2fe chore: update results (2026-06-26)
* | | | | | | | | | 0bd3a04 chore: update results (2026-06-25)
* | | | | | | | | | 9985da4 Update update_wc.py
* | | | | | | | | | 14b7d30 chore: update results (2026-06-25)
* | | | | | | | | |   5d95d20 fix: prevent merging of sibling branches by only following the first … (#24)
|\ \ \ \ \ \ \ \ \ \  
| * | | | | | | | | | 5c03e0c fix: prevent merging of sibling branches by only following the first parent in commit history
|/ / / / / / / / / /  
* | | | | | | | | | 672d35f Update update-results.yml
* | | | | | | | | | e273890 Add debug logging for branches and SHA mapping
* | | | | | | | | | af871da Fix formatting in git_output_cmd command
* | | | | | | | | | 65c5589 Refactor git log commands in update_wc.py
* | | | | | | | | | 2567c42 chore: update results (2026-06-25)
* | | | | | | | | |   234a479 Fix group branches missing from Mermaid GitGraph due to narrow fetch refspec (#23)
|\ \ \ \ \ \ \ \ \ \  
| * | | | | | | | | | 8dba9b3 Remove the merge guessing
| * | | | | | | | | | 0917a6d fix: fetch all remote branches with wildcard refspec in workflow
| * | | | | | | | | | adcc7d8 fix: infer group branch tips from merge commit subjects when branch refs are deleted
|/ / / / / / / / / /  
* | | | | | | | | | 95d2fbb chore: update results (2026-06-25)
* | | | | | | | | | 20bb335 Update state.json
* | | | | | | | | |   1853711 Group C: BRA, MAR advance (#13)
|\ \ \ \ \ \ \ \ \ \  
* \ \ \ \ \ \ \ \ \ \   582cdde Group B: SUI, CAN advance (#12)
|\ \ \ \ \ \ \ \ \ \ \  
* \ \ \ \ \ \ \ \ \ \ \   2601f9a Group A: MEX, RSA advance (#11)
|\ \ \ \ \ \ \ \ \ \ \ \  
* | | | | | | | | | | | | e5c328e chore: update results (2026-06-25)
* | | | | | | | | | | | | 63ecdfc Update update_wc.py
* | | | | | | | | | | | | 2452db4 chore: update results (2026-06-25)
* | | | | | | | | | | | | 09b3863 Update update_wc.py
* | | | | | | | | | | | | 58eaddf Update update_wc.py
* | | | | | | | | | | | | d795d15 chore: update results (2026-06-25)
* | | | | | | | | | | | | 766e2f9 chore: update results (2026-06-24)
* | | | | | | | | | | | | 44b4375 chore: update results (2026-06-24)
* | | | | | | | | | | | | c9ac0a0 Disable scheduled updates for World Cup results
* | | | | | | | | | | | | 3363bd4 chore: update results (2026-06-24)
* | | | | | | | | | | | | 33f3158 chore: update results (2026-06-24)
* | | | | | | | | | | | | 69a9d9b chore: update results (2026-06-24)
* | | | | | | | | | | | | e9982f7 Update update_wc.py
* | | | | | | | | | | | | d97b331 chore: update results (2026-06-24)
* | | | | | | | | | | | | e5a5a17 Add commit id to gitGraph command output
* | | | | | | | | | | | | e1b30f2 chore: update results (2026-06-24)
* | | | | | | | | | | | | ef8924b chore: update results (2026-06-24)
* | | | | | | | | | | | | 9b9ffa2 chore: update results (2026-06-24)
* | | | | | | | | | | | | e8d508e chore: update results (2026-06-23)
* | | | | | | | | | | | | 211ffde Update update_wc.py
* | | | | | | | | | | | | a4c4ecc chore: update results (2026-06-23)
* | | | | | | | | | | | | 0dae92a chore: update results (2026-06-23)
* | | | | | | | | | | | | b4349ce Update state.json
* | | | | | | | | | | | | 28444af chore: update results (2026-06-23)
* | | | | | | | | | | | | 0226e32 Allow display of chore commits in update_wc.py
* | | | | | | | | | | | | 0827645 Update starting_commit in state.json
* | | | | | | | | | | | | e37f30d chore: update results (2026-06-23)
* | | | | | | | | | | | | f027d96 Update starting_commit in state.json
* | | | | | | | | | | | | 9bb0204 chore: update results (2026-06-23)
* | | | | | | | | | | | | c6254c2 Update starting_commit in state.json
* | | | | | | | | | | | | 795f227 chore: update results (2026-06-23)
* | | | | | | | | | | | | 2eb25c8 Update starting_commit to new commit hash
| | | | | | | | | | | | | * be71aa7 feat: Ghana advances to Round of 32
| | | | | | | | | | | | |/  
| | | | | | | | | | | | | * c4fe5ae feat: Colombia advances to Round of 32
| | | | | | | | | | | | |/  
| | | | | | | | | | | |/|   
| | | | | | | | | | | | | * cbdbe9d feat: Cape Verde advances to Round of 32
| | | | | | | | | |_|_|_|/  
| | | | | | | | |/| | | |   
| | | | | | | | | | | | | * 50d9b3a feat: Argentina advances to Round of 32
| | | | | | | | | | | |_|/  
| | | | | | | | | | |/| |   
| | | | | | | | | | | | | * c55e2b9 feat: Egypt advances to Round of 32
| | | | | | | | | | |_|_|/  
| | | | | | | | | |/| | |   
| | | | | | | | | | | | | * 42b8d83 feat: Australia advances to Round of 32
| | | | | |_|_|_|_|_|_|_|/  
| | | | |/| | | | | | | |   
| | | | | | | | | | | | | * 1625e5c feat: Algeria advances to Round of 32
| | | | | | | | | | | |_|/  
| | | | | | | | | | |/| |   
| | | | | | | | | | | | | * f81e0ef feat: Switzerland advances to Round of 32
| | | |_|_|_|_|_|_|_|_|_|/  
| | |/| | | | | | | | | |   
| | | | | | | | | | | | | * 17d2671 feat: Croatia advances to Round of 32
| | | | | | | | | | | | |/  
| | | | | | | | | | | | | * 1100b4d feat: Portugal advances to Round of 32
| | | | | | | | | | | | |/  
| | | | | | | | | | | |/|   
| | | | | | | | | | | | | * 6bb0c4c feat: Austria advances to Round of 32
| | | | | | | | | | | |_|/  
| | | | | | | | | | |/| |   
| | | | | | | | | | * | | a263387 Group J, MD3: Algeria 3-3 Austria (2026-06-28)
| | | | | | | | | | * | | f789e3c Group J, MD3: Jordan 1-3 Argentina (2026-06-28)
| | | | | | | | | | * | | 64f56fa Group J, MD2: Jordan 1-2 Algeria (2026-06-23)
| | | | | | | | | | * | | a04bce5 Group J, MD2: Argentina 2-0 Austria (2026-06-22)
| | | | | | | | | | * | | d62db80 Group J, MD1: Austria 3-1 Jordan (2026-06-17)
| | | | | | | | | | * | | 555de8f Group J, MD1: Argentina 3-0 Algeria (2026-06-17)
| | | | | | | | | | * | | 26d1524 feat: initialize Group J
| |_|_|_|_|_|_|_|_|/ / /  
|/| | | | | | | | | | |   
| | | | | | | | | | | | * 6183468 feat: Spain advances to Round of 32
| | | | | | | | | |_|_|/  
| | | | | | | | |/| | |   
| | | | | | | | * | | | 6bcba87 Group H, MD3: Cape Verde 0-0 Saudi Arabia (2026-06-27)
| | | | | | | | * | | | 936cae0 Group H, MD3: Uruguay 0-1 Spain (2026-06-27)
| | | | | | | | * | | | 041ba94 Group H, MD2: Uruguay 2-2 Cape Verde (2026-06-21)
| | | | | | | | * | | | 4187777 Group H, MD2: Spain 4-0 Saudi Arabia (2026-06-21)
| | | | | | | | * | | | b8d1966 Group H, MD1: Saudi Arabia 1-1 Uruguay (2026-06-15)
| | | | | | | | * | | | 0d818f0 Group H, MD1: Spain 0-0 Cape Verde (2026-06-15)
| | | | | | | | * | | | ea91a7b feat: initialize Group H
| |_|_|_|_|_|_|/ / / /  
|/| | | | | | | | | |   
| | | | | | | | | | | * 6bb95d0 feat: Bosnia-H. advances to Round of 32
| | | |_|_|_|_|_|_|_|/  
| | |/| | | | | | | |   
| | | | | | | | | | | * 009956f feat: USA advances to Round of 32
| | | | | |_|_|_|_|_|/  
| | | | |/| | | | | |   
| | | | | | | | | | | * d3ec69d feat: Senegal advances to Round of 32
| | | | | | | | |_|_|/  
| | | | | | | |/| | |   
| | | | | | | | | | | * dcbd99c feat: Belgium advances to Round of 32
| | | | | | | | | |_|/  
| | | | | | | | |/| |   
| | | | | | | | * | | 5228e04 Group G, MD3: Egypt 1-2 Iran (2026-06-27)
| | | | | | | | * | | a8eb1cc Group G, MD3: New Zealand 1-5 Belgium (2026-06-27)
| | | | | | | | * | | 1aa234b Group G, MD2: New Zealand 1-3 Egypt (2026-06-22)
| | | | | | | | * | | 9a649da Group G, MD2: Belgium 0-0 Iran (2026-06-21)
| | | | | | | | * | | 4198b88 Group G, MD1: Iran 2-2 New Zealand (2026-06-16)
| | | | | | | | * | | 7f1d992 Group G, MD1: Belgium 1-1 Egypt (2026-06-15)
| | | | | | | | * | | 9ba404e feat: initialize Group G
| |_|_|_|_|_|_|/ / /  
|/| | | | | | | | |   
| | | | | | | | | | * 5672b0b feat: Congo DR advances to Round of 32
| | | | | | | | | |/  
| | | | | | | | |/|   
| | | | | | | | * | 8744925 Group K, MD3: Congo DR 3-1 Uzbekistan (2026-06-27)
| | | | | | | | * | 3d35870 Group K, MD3: Colombia 0-0 Portugal (2026-06-27)
| | | | | | | | * | f5de9cc Group K, MD2: Colombia 1-0 Congo DR (2026-06-24)
| | | | | | | | * | 6143609 Group K, MD2: Portugal 5-0 Uzbekistan (2026-06-23)
| | | | | | | | * | 03093dc Group K, MD1: Uzbekistan 1-3 Colombia (2026-06-18)
| | | | | | | | * | 9e313b3 Group K, MD1: Portugal 1-1 Congo DR (2026-06-17)
| | | | | | | | * | 682f112 feat: initialize Group K
| |_|_|_|_|_|_|/ /  
|/| | | | | | | |   
| | | | | | | | | * 8b598ba feat: England advances to Round of 32
| | | | | | | | |/  
| | | | | | | | * e8fed03 Group L, MD3: Croatia 2-1 Ghana (2026-06-27)
| | | | | | | | * 475af9c Group L, MD3: Panama 0-2 England (2026-06-27)
| | | | | | | | * 7551de5 Group L, MD2: Panama 0-1 Croatia (2026-06-23)
| | | | | | | | * 6a430be Group L, MD2: England 0-0 Ghana (2026-06-23)
| | | | | | | | * ab54662 Group L, MD1: Ghana 1-0 Panama (2026-06-17)
| | | | | | | | * 9709b5e Group L, MD1: England 4-2 Croatia (2026-06-17)
| | | | | | | | * 4ece383 feat: initialize Group L
| |_|_|_|_|_|_|/  
|/| | | | | | |   
| | | | | | | | * 09d842a feat: Ecuador advances to Round of 32
| | | | | | |_|/  
| | | | | |/| |   
| | | | | | | | * 447aabb feat: Mexico advances to Round of 32
| | |_|_|_|_|_|/  
| |/| | | | | |   
| | | | | | | | * 8b96aa3 feat: Sweden advances to Round of 32
| | | | | | | |/  
| | | | | | |/|   
| | | | | | | | * 4a6c4ef feat: France advances to Round of 32
| | | | | | | |/  
| | | | | | | | * 31d39aa feat: Norway advances to Round of 32
| | | | | | | |/  
| | | | | | | * 5703db8 Group I, MD3: Senegal 5-0 Iraq (2026-06-26)
| | | | | | | * c05f27d Group I, MD3: Norway 1-4 France (2026-06-26)
| | | | | | | * 5a0f84e Group I, MD2: Norway 3-2 Senegal (2026-06-23)
| | | | | | | * 40fce23 Group I, MD2: France 3-0 Iraq (2026-06-22)
| | | | | | | * 432ca77 Group I, MD1: Iraq 1-4 Norway (2026-06-16)
| | | | | | | * 769feea Group I, MD1: France 3-1 Senegal (2026-06-16)
| | | | | | | * a28079d feat: initialize Group I
| |_|_|_|_|_|/  
|/| | | | | |   
| | | | | | | * 57a304b feat: Ivory Coast advances to Round of 32
| | | | | | |/  
| | | | | |/|   
| | | | | | | * b958ff3 feat: Morocco advances to Round of 32
| | | | |_|_|/  
| | | |/| | |   
| | | | | | | * 6f089b1 feat: Netherlands advances to Round of 32
| | | | | | |/  
| | | | | | | * 7803851 feat: Paraguay advances to Round of 32
| | | | | |_|/  
| | | | |/| |   
| | | | * | | a0a688a Group D, MD3: Paraguay 0-0 Australia (2026-06-26)
| | | | * | | 6fa6b3a Group D, MD3: Turkey 3-2 USA (2026-06-26)
| | | | * | | e28a6dc Group D, MD2: Turkey 0-1 Paraguay (2026-06-20)
| | | | * | | f307f62 Group D, MD2: USA 2-0 Australia (2026-06-19)
| | | | * | | d9483dc Group D, MD1: Australia 2-0 Turkey (2026-06-14)
| | | | * | | 3829793 Group D, MD1: USA 4-1 Paraguay (2026-06-13)
| | | | * | | da0de21 feat: initialize Group D
| |_|_|/ / /  
|/| | | | |   
| | | | | | * c4373a3 feat: Germany advances to Round of 32
| | | | | |/  
| | | | |/|   
| | | | * | 1e58c16 Group E, MD3: Curaçao 0-2 Ivory Coast (2026-06-25)
| | | | * | 3a01352 Group E, MD3: Ecuador 2-1 Germany (2026-06-25)
| | | | * | 54ae035 Group E, MD2: Ecuador 0-0 Curaçao (2026-06-21)
| | | | * | fd81778 Group E, MD2: Germany 2-1 Ivory Coast (2026-06-20)
| | | | * | 7948bbe Group E, MD1: Ivory Coast 1-0 Ecuador (2026-06-14)
| | | | * | 6256d77 Group E, MD1: Germany 7-1 Curaçao (2026-06-14)
| | | | * | cd1b6fc feat: initialize Group E
| |_|_|/ /  
|/| | | |   
| | | | | * e07b324 feat: Japan advances to Round of 32
| | | | |/  
| | | | * 3fb3b66 Group F, MD3: Japan 1-1 Sweden (2026-06-25)
| | | | * d3f08c9 Group F, MD3: Tunisia 1-3 Netherlands (2026-06-25)
| | | | * 37486e3 Group F, MD2: Tunisia 0-4 Japan (2026-06-21)
| | | | * 62cfd94 Group F, MD2: Netherlands 5-1 Sweden (2026-06-20)
| | | | * a3802dd Group F, MD1: Sweden 5-1 Tunisia (2026-06-15)
| | | | * 55a2a87 Group F, MD1: Netherlands 2-2 Japan (2026-06-14)
| | | | * f136fe6 feat: initialize Group F
| |_|_|/  
|/| | |   
| | | | * 038f852 feat: Brazil advances to Round of 32
| | | |/  
| | | * 1e63230 Group C, MD3: Scotland 0-3 Brazil (2026-06-24)
| | | * 914859e Group C, MD3: Morocco 4-2 Haiti (2026-06-24)
| | | * 713ade3 Group C, MD2: Brazil 3-0 Haiti (2026-06-20)
| | | * 1ea95ac Group C, MD2: Scotland 0-1 Morocco (2026-06-19)
| | | * cae8412 Group C, MD1: Haiti 0-1 Scotland (2026-06-14)
| | | * 4c1fb49 Group C, MD1: Brazil 1-1 Morocco (2026-06-13)
| | | * de0ccc8 feat: initialize Group C
| |_|/  
|/| |   
| | | * 9e0d65e feat: Canada advances to Round of 32
| | |/  
| | * 0a60654 Group B, MD3: Bosnia-H. 3-1 Qatar (2026-06-24)
| | * c1e4c7e Group B, MD3: Switzerland 2-1 Canada (2026-06-24)
| | * 3357170 Group B, MD2: Canada 6-0 Qatar (2026-06-18)
| | * 2f0881b Group B, MD2: Switzerland 4-1 Bosnia-H. (2026-06-18)
| | * d12dfee Group B, MD1: Qatar 1-1 Switzerland (2026-06-13)
| | * 647c3f3 Group B, MD1: Canada 1-1 Bosnia-H. (2026-06-12)
| | * 73fea82 feat: initialize Group B
| |/  
|/|   
| | * ad50414 feat: South Africa advances to Round of 32
| |/  
| * fb7d903 Group A, MD3: South Africa 1-0 Korea Republic (2026-06-25)
| * 1276260 Group A, MD3: Czechia 0-3 Mexico (2026-06-25)
| * f768041 Group A, MD2: Mexico 1-0 Korea Republic (2026-06-19)
| * dbc69ea Group A, MD2: Czechia 1-1 South Africa (2026-06-18)
| * 777a2b6 Group A, MD1: Korea Republic 2-1 Czechia (2026-06-12)
| * 612b691 Group A, MD1: Mexico 2-0 South Africa (2026-06-11)
| * b22d60b feat: initialize Group A
|/  
* ca7d95c chore: update results (2026-06-23)
* 29bcdac chore: update results (2026-06-23)
* 59ccdf1 chore: update results (2026-06-23)
* 2e629c7 chore: update results (2026-06-23)
* 3c96f35 Update update_wc.py
```