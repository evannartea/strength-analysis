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

### 🎯 What I Learned
#

### 📝 Notes
#
- The raw data was filtered to include only adults, full SBD events, and raw equipment, while excluding any disqualified entries or no-shows:
```sql
WHERE "Age" >= 18
AND "Event"  = 'SBD'
AND "Equipment" = 'Raw'
AND "Place" NOT IN ('DQ', 'DD', 'NS')
```
- There were several null values identified in the dataset, which may have impacted the analysis of some variables.
```text
Column             Count
------------------------
Name                   0
Sex                    0
Age                    0
BodyweightKg         462
Country            12551
Date                   0
Best3SquatKg         284
Best3BenchKg         322
Best3DeadliftKg      301
TotalKg                0
Place                  0
```

### 📄 Credits
#
**Author:** Evan Nartea<br>
**Contributors:** Evan Nartea<br>
<br>
Powerlifting data: https://www.openpowerlifting.org<br>
