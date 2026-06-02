import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
PROCESSED.mkdir(exist_ok=True)

# NAV HISTORY
nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

# forward fill missing NAV within each fund
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

nav.to_csv(PROCESSED / "02_nav_history_clean.csv", index=False)

print("NAV cleaned")

tx = pd.read_csv(RAW / "08_investor_transactions.csv")

tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])

tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

tx["transaction_type"] = tx["transaction_type"].replace(mapping)

tx = tx[tx["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending", "Rejected"]

tx["kyc_valid"] = tx["kyc_status"].isin(valid_kyc)

tx.to_csv(
    PROCESSED / "08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

perf = pd.read_csv(RAW / "07_scheme_performance.csv")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf["expense_ratio_flag"] = (
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
)

perf.to_csv(
    PROCESSED / "07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")