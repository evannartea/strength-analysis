<img src="images/open_powerlifting_logo.svg" height=1982 width=652>

### Powerlifting Strength Analysis
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![Tableau](https://custom-icon-badges.demolab.com/badge/Tableau-0176D3?logo=tableau&logoColor=fff)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#)

### 📌 Project Overview
#

### 📊 Analysis
#
##### Summary
```text
|       |      Age |   BodyweightKg |   Best3SquatKg |   Best3BenchKg |   Best3DeadliftKg |   TotalKg |
|-------|----------|----------------|----------------|----------------|-------------------|-----------|
| count | 838576   |       838114   |       838292   |       838254   |          838275   |  838576   |
| mean  |     30.4 |           84.2 |          172.3 |          110.8 |             199.3 |     482.4 |
| std   |     11.5 |           21   |           58.5 |           42.7 |              58.8 |     155.1 |
| min   |     18   |           25   |           10   |            6.8 |              20   |      52.5 |
| 25%   |     22   |           68.9 |          125   |           72.5 |             150   |     350   |
| 50%   |     26.5 |           81.8 |          172.5 |          112.5 |             200   |     490   |
| 75%   |     35.5 |           96.8 |          215   |          142.5 |             242.5 |     597.5 |
| max   |     93.5 |          285   |          490.5 |          325   |             492.5 |    1225   |
```

### 🎯 What I Learned
#

### 📝 Notes
#
- The raw data was filtered to include only male or female adults, full SBD events, and raw equipment, while excluding any disqualified entries or no-shows:
```sql
WHERE op."Age" >= 18
AND op."Sex" <> 'Mx'
AND op."Event"  = 'SBD'
AND op."Equipment" = 'Raw'
AND op."Place" NOT IN ('DQ', 'DD', 'NS')
```
- There were several null values identified in the dataset, which may have impacted the analysis of some variables.
```text
| Column          |   Null Count |
|-----------------|--------------|
| Name            |            0 |
| Sex             |            0 |
| Age             |            0 |
| BodyweightKg    |          462 |
| Country         |        12551 |
| Date            |            0 |
| Best3SquatKg    |          284 |
| Best3BenchKg    |          322 |
| Best3DeadliftKg |          301 |
| TotalKg         |            0 |
| Place           |            0 |
```

### 📄 Credits
#
**Author:** Evan Nartea<br>
**Contributors:** Evan Nartea<br>
<br>
Powerlifting data: https://www.openpowerlifting.org<br>
