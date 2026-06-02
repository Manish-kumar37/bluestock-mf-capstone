import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(RAW / file)

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove fully empty rows
    df = df.dropna(how="all")

    output_name = file.replace(".csv", "_clean.csv")

    df.to_csv(PROCESSED / output_name, index=False)

    print(f"Saved: {output_name}")