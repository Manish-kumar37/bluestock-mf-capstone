# Bluestock MF Capstone Project

Mutual Fund data analytics capstone — ETL, EDA, performance metrics, dashboard, and advanced analytics.

## Setup

```bash
git clone <your-repo-url>
cd bluestock_mf_capstone
pip install -r requirements.txt
```

## Running Day 1 Scripts

```bash
# Fetch live NAV data from mfapi.in
python scripts/live_nav_fetch.py

# Run ETL pipeline on local CSVs (place CSVs in data/raw/ first)
python scripts/etl_pipeline.py
```

## Folder Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/           ← original downloaded files
│   ├── processed/     ← cleaned, merged CSVs
│   └── db/            ← bluestock_mf.db (SQLite) — NOT committed to git
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── bluestock_mf.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
└── README.md
```

## Progress

- [x] Day 1 — Data Ingestion & ETL
- [x] Day 2 — Data Cleaning & SQLite
- [x] Day 3 — EDA
- [x] Day 4 — Performance Metrics
- [x] Day 5 — Dashboard
- [x] Day 6 — Advanced Analytics
- [x] Day 7 — Final Report

## Notes

- `.db` files are in `.gitignore`. Use `sql/schema.sql` to recreate the database.
- Always `ffill()` NAV after reindexing to handle weekends/holidays.
- Use 252 trading days (not 365) for annualisation.

## Project Progress

### Day 1 – Data Profiling

* Explored all mutual fund datasets.
* Checked schema, data types, missing values, and duplicates.
* Created dataset inventory and quality assessment.

Implemented using:
- scripts/data_ingestion.py
- scripts/live_nav_fetch.py
### Day 2 – Data Cleaning

* Standardized column names and formats.
* Removed duplicates and handled data inconsistencies.
* Generated cleaned datasets for analysis.

Implemented using:
- scripts/clean_data.py
- scripts/load_to_sqlite.py
- sql/schema.sql
- sql/queries.sql\


### Day 3 – Feature Engineering

* Calculated CAGR, Alpha, Beta, Sharpe Ratio, and Max Drawdown.
* Created fund ranking and scorecard metrics.
* Prepared analytical datasets for reporting.

### Day 4 – ETL & Live Data Integration

* Built ETL pipeline using Python.
* Integrated live NAV data from MFAPI.
* Performed AMFI code validation and data quality checks.

### Day 5 – Power BI Dashboard

* Imported cleaned datasets into Power BI.
* Created relationships using `amfi_code`.
* Built 5 dashboard pages:

  * Industry Overview
  * Fund Performance
  * Investor Analytics
  * SIP & Market Trends
  * Fund Detail (Drill-through)
* Added KPI cards, slicers, benchmark comparisons, and interactive visualizations.

### Pages
1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends
5. Fund Detail (Drill Through)

### Features
- KPI Cards
- Risk vs Return Analysis
- Benchmark Comparison
- Investor Demographics
- SIP Trend Analysis
- Heatmap Visualization
- Drill Through Navigation


# Bluestock Mutual Fund Analytics Capstone Project

## Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, fund flows, portfolio composition, and investment risk.

The project combines data engineering, financial analytics, and business intelligence techniques to transform raw mutual fund datasets into actionable insights.

## Key Features

### ETL Pipeline

* Automated data cleaning and validation
* Missing value handling
* Duplicate record removal
* AMFI code validation
* SQLite database integration

### Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Benchmark Comparison

### Advanced Analytics

* Value at Risk (VaR 95%)
* Conditional Value at Risk (CVaR 95%)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Portfolio Concentration Analysis (HHI)
* Risk-Based Fund Recommendation Engine

### Business Intelligence Dashboard

* Overview Dashboard
* Investor Analytics Dashboard
* Fund Flow Dashboard
* Risk Analytics Dashboard
* Fund Detail Dashboard

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── reports/
│   ├── Final_Report.pdf
│   ├──final_presentation.pptx
│   └── charts/
│
├── dashboard/
│   └── Mutual_Fund_Dashboard.pbix
│
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* Matplotlib
* Seaborn
* Power BI
* Git & GitHub

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd bluestock_mf_capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Fetch Live NAV Data

```bash
python scripts/live_nav_fetch.py
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Run Fund Recommender

```bash
python scripts/recommender.py
```

## Deliverables

* Final_Report.pdf
* Final_Presentation.pptx
* Power BI Dashboard
* Analytics Notebooks
* ETL Pipeline
* GitHub Repository

## Author

Manish Kumar

Data Analytics Internship – Bluestock
