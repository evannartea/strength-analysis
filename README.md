<img src="images/open_powerlifting_logo.svg" height=1982 width=652>

### Powerlifting Strength Analysis
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![Tableau](https://custom-icon-badges.demolab.com/badge/Tableau-0176D3?logo=tableau&logoColor=fff)](#)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff)](#)

### 📌 Project Overview
#

### 📷 Examples
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

### 📄 Credits
#
**Author:** Evan Nartea<br>
**Contributors:** Evan Nartea<br>
<br>
Powerlifting data: https://www.openpowerlifting.org<br>
