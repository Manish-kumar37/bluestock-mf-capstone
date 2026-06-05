import pandas as pd

files = [
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv"
]

for f in files:
    df = pd.read_csv(f"data/raw/{f}")

    print("\n" + "=" * 80)
    print(f)
    print("Columns:")
    print(df.columns.tolist())

    print("\nFirst 3 rows:")
    print(df.head(3))