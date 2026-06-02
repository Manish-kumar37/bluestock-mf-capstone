import pandas as pd

files = [
    "data/raw/02_nav_history.csv",
    "data/raw/07_scheme_performance.csv",
    "data/raw/08_investor_transactions.csv"
]

for f in files:
    print("\n" + "="*80)
    print(f)
    df = pd.read_csv(f)
    print(df.columns.tolist())
    print(df.head(3))