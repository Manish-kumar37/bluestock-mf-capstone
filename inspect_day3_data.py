import pandas as pd

files = [
    "03_aum_by_fund_house_clean.csv",
    "04_monthly_sip_inflows_clean.csv",
    "05_category_inflows_clean.csv",
    "06_industry_folio_count_clean.csv",
    "08_investor_transactions_clean.csv",
    "09_portfolio_holdings_clean.csv"
]

for f in files:
    print("\n" + "="*80)
    print(f)

    df = pd.read_csv(f"data/processed/{f}")

    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())