import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

files = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/processed/02_nav_history_clean.csv",
    "scheme_performance": "data/processed/07_scheme_performance_clean.csv",
    "investor_transactions": "data/processed/08_investor_transactions_clean.csv"
}

for table, path in files.items():
    df = pd.read_csv(path)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(table, len(df))