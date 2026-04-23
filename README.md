Job Market Report Automation

 Overview

An automated data pipeline that processes job market data, performs validation, generates insights, and creates Excel reports with key business metrics.

Tech Stack

* Python
* SQLite
* Pandas
* OpenPyXL
* Schedule

Features

* Data ingestion from CSV to SQL
* Data validation (missing values, duplicates, inconsistencies)
* Insights generation:

  * Top companies, roles, locations
  * Skill demand analysis
  * Salary insights
  * Job posting trends
* Multi-sheet Excel report generation
* Automation with scheduler

 How to Run


pip install -r requirements.txt
python main.py
```

Run scheduler:

```bash
python -m scripts.scheduler
```


 Output

* Excel report with multiple sheets (summary, skills, salary, trends)
* Validation reports

 Use Case

Automates repetitive business reporting tasks and provides actionable job market insights.

---

Debakshi Saha
