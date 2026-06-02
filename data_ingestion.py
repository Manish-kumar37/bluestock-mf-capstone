import pandas as pd
from pathlib import Path

data_dir = Path("data/raw")

csv_files = sorted(data_dir.glob("0*.csv"))

print(f"\nFound {len(csv_files)} datasets\n")

for file in csv_files:

    print("=" * 80)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nPotential Anomalies:")

    if df.isnull().sum().sum() > 0:
        print("Missing values detected")

    if df.duplicated().sum() > 0:
        print(f"Duplicate rows: {df.duplicated().sum()}")

    if df.isnull().sum().sum() == 0 and df.duplicated().sum() == 0:
        print("No obvious anomalies detected")

    print("\n")