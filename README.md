<img src="images/open_powerlifting_logo.svg" height=1982 width=652>

### Powerlifting Strength Analysis
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![Tableau](https://custom-icon-badges.demolab.com/badge/Tableau-0176D3?logo=tableau&logoColor=fff)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#)

### 📌 Project Overview
#

### 📊 Results
#
#### Summary

Male Lifters
```text
|       |      Age |   BodyweightKg |   Best3SquatKg |   Best3BenchKg |   Best3DeadliftKg |   TotalKg |
|-------|----------|----------------|----------------|----------------|-------------------|-----------|
| count | 552232   |       551942   |       552002   |       551969   |          551983   |  552232   |
| mean  |     29.7 |           91.2 |          201.3 |          134.3 |             230.4 |     566   |
| std   |     11.4 |           19.3 |           47.4 |           31.4 |              44.5 |     115.3 |
| min   |     18   |           25   |           15   |           12.5 |              20   |      60   |
| 25%   |     21.5 |           79   |          170   |          112.5 |             200   |     490   |
| 50%   |     26   |           89   |          200   |          132.5 |             230   |     562.5 |
| 75%   |     34   |          101.8 |          230   |          155   |             260   |     640   |
| max   |     93.5 |          285   |          490.5 |          325   |             492.5 |    1225   |
```

Female Lifters
```text
|       |      Age |   BodyweightKg |   Best3SquatKg |   Best3BenchKg |   Best3DeadliftKg |   TotalKg |
|-------|----------|----------------|----------------|----------------|-------------------|-----------|
| count | 286226   |       286054   |       286172   |       286167   |          286174   |  286226   |
| mean  |     31.8 |           70.7 |          116.4 |           65.4 |             139.5 |     321.2 |
| std   |     11.5 |           17.2 |           30.9 |           17.6 |              29.4 |      73.4 |
| min   |     18   |           34.9 |           10   |            6.8 |              20   |      52.5 |
| 25%   |     22.5 |           59   |           95   |           52.5 |             120   |     270   |
| 50%   |     28.5 |           67.2 |          115   |           62.5 |             140   |     317.5 |
| 75%   |     38.5 |           78.7 |          135   |           75   |             157.5 |     367.5 |
| max   |     92   |          216   |          318.5 |          188.2 |             297.5 |     759   |
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
