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
- [ ] Day 5 — Dashboard
- [ ] Day 6 — Advanced Analytics
- [ ] Day 7 — Final Report

## Notes

- `.db` files are in `.gitignore`. Use `sql/schema.sql` to recreate the database.
- Always `ffill()` NAV after reindexing to handle weekends/holidays.
- Use 252 trading days (not 365) for annualisation.

## Day 1 – Data Ingestion

Implemented using:
- scripts/data_ingestion.py
- scripts/live_nav_fetch.py

## Day 2 – Data Cleaning & Database Loading

Implemented using:
- scripts/clean_data.py
- scripts/load_to_sqlite.py
- sql/schema.sql
- sql/queries.sql

## Power BI Dashboard

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