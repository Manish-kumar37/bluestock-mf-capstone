"""
etl_pipeline.py — Day 1: Data Ingestion & Validation
Bluestock MF Capstone Project
"""

import os
import pathlib
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────────
ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
RAW.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)

# ── Helper ─────────────────────────────────────────────────────────────────
def load_csv(filename: str, **kwargs) -> pd.DataFrame:
    """Load a CSV from data/raw with basic inspection."""
    path = RAW / filename
    if not path.exists():
        print(f"  [SKIP] {filename} not found in data/raw/")
        return pd.DataFrame()
    df = pd.read_csv(path, **kwargs)
    print(f"\n{'─'*50}")
    print(f"  File   : {filename}")
    print(f"  Shape  : {df.shape}")
    print(f"  Dtypes :\n{df.dtypes.to_string()}")
    print(f"  Head   :\n{df.head(3).to_string()}")
    nulls = df.isnull().sum()
    if nulls.any():
        print(f"  Nulls  :\n{nulls[nulls > 0].to_string()}")
    return df


def inspect_anomalies(df: pd.DataFrame, name: str) -> dict:
    """Return a dict of data quality flags."""
    flags = {}
    flags["shape"] = df.shape
    flags["null_cols"] = df.isnull().sum()[df.isnull().sum() > 0].to_dict()
    flags["dup_rows"] = int(df.duplicated().sum())
    return {name: flags}


# ── Task 3: Load all CSV datasets ──────────────────────────────────────────
CSV_FILES = [
    "fund_master.csv",
    "nav_history.csv",
    "scheme_returns.csv",
    "portfolio_holdings.csv",
    "amc_details.csv",
    "risk_metrics.csv",
    "benchmark_data.csv",
    "investor_data.csv",
    "sip_data.csv",
    "category_avg_returns.csv",
]

def load_all_datasets() -> dict[str, pd.DataFrame]:
    print("\n" + "="*60)
    print("  TASK 3 — Loading all CSV datasets")
    print("="*60)
    dfs = {}
    quality_report = {}
    for f in CSV_FILES:
        df = load_csv(f)
        if not df.empty:
            key = f.replace(".csv", "")
            dfs[key] = df
            quality_report.update(inspect_anomalies(df, key))
    return dfs, quality_report


# ── Task 6: Explore fund_master ────────────────────────────────────────────
def explore_fund_master(df: pd.DataFrame):
    print("\n" + "="*60)
    print("  TASK 6 — Fund Master Exploration")
    print("="*60)
    for col in ["fund_house", "category", "sub_category", "risk_grade"]:
        if col in df.columns:
            vals = df[col].value_counts()
            print(f"\n  Unique {col} ({len(vals)}):\n{vals.to_string()}")
    if "scheme_code" in df.columns:
        sample = df["scheme_code"].head(5)
        print(f"\n  Sample AMFI codes: {sample.tolist()}")
        print("  AMFI codes are 6-digit integers assigned by AMFI to each scheme.")


# ── Task 7: Validate AMFI codes ────────────────────────────────────────────
def validate_amfi_codes(fund_master: pd.DataFrame, nav_history: pd.DataFrame) -> str:
    print("\n" + "="*60)
    print("  TASK 7 — AMFI Code Validation")
    print("="*60)
    if fund_master.empty or nav_history.empty:
        print("  [SKIP] One or both dataframes are empty.")
        return "Skipped — data not available."

    master_codes = set(fund_master["scheme_code"].astype(str))
    nav_codes = set(nav_history["scheme_code"].astype(str))

    missing_in_nav = master_codes - nav_codes
    extra_in_nav = nav_codes - master_codes

    summary = (
        f"\n  DATA QUALITY SUMMARY\n"
        f"  {'─'*40}\n"
        f"  Fund master codes    : {len(master_codes)}\n"
        f"  NAV history codes    : {len(nav_codes)}\n"
        f"  Codes in master, missing from NAV : {len(missing_in_nav)}\n"
        f"  Extra codes in NAV (not in master): {len(extra_in_nav)}\n"
        f"  Match rate           : {(1 - len(missing_in_nav)/max(len(master_codes),1))*100:.1f}%\n"
    )
    print(summary)
    if missing_in_nav:
        print(f"  Missing codes sample: {list(missing_in_nav)[:10]}")

    # Save quality report
    report_path = PROCESSED / "data_quality_summary.txt"
    with open(report_path, "w") as f:
        f.write(f"Data Quality Summary — {datetime.now()}\n")
        f.write(summary)
    print(f"\n  Saved quality summary → {report_path}")
    return summary


# ── Main ───────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\n  Project root : {ROOT}")
    print(f"  Raw data dir : {RAW}")

    dfs, quality_report = load_all_datasets()

    fund_master = dfs.get("fund_master", pd.DataFrame())
    nav_history = dfs.get("nav_history", pd.DataFrame())

    if not fund_master.empty:
        explore_fund_master(fund_master)

    validate_amfi_codes(fund_master, nav_history)

    print("\n\n  ✓ ETL pipeline complete. Check data/processed/ for outputs.")
