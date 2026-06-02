# Data Dictionary

## 01_fund_master.csv

| Column       | Data Type | Description                          |
| ------------ | --------- | ------------------------------------ |
| amfi_code    | Integer   | Unique AMFI scheme identifier        |
| scheme_name  | Text      | Mutual fund scheme name              |
| fund_house   | Text      | Asset management company             |
| category     | Text      | Fund category                        |
| sub_category | Text      | Fund sub-category                    |
| risk_grade   | Text      | Risk classification                  |
| aum_crore    | Float     | Assets under management in crore INR |

## 02_nav_history.csv

| Column    | Data Type | Description       |
| --------- | --------- | ----------------- |
| amfi_code | Integer   | Scheme identifier |
| date      | Date      | NAV date          |
| nav       | Float     | Net Asset Value   |

## 07_scheme_performance.csv

| Column            | Data Type | Description          |
| ----------------- | --------- | -------------------- |
| amfi_code         | Integer   | Scheme identifier    |
| return_1yr_pct    | Float     | 1-year return (%)    |
| return_3yr_pct    | Float     | 3-year return (%)    |
| return_5yr_pct    | Float     | 5-year return (%)    |
| alpha             | Float     | Alpha measure        |
| beta              | Float     | Beta measure         |
| sharpe_ratio      | Float     | Risk-adjusted return |
| expense_ratio_pct | Float     | Expense ratio (%)    |

## 08_investor_transactions.csv

| Column           | Data Type | Description             |
| ---------------- | --------- | ----------------------- |
| investor_id      | Text      | Unique investor ID      |
| transaction_date | Date      | Transaction date        |
| amfi_code        | Integer   | Scheme identifier       |
| transaction_type | Text      | SIP/Lumpsum/Redemption  |
| amount_inr       | Float     | Transaction amount      |
| state            | Text      | Investor state          |
| kyc_status       | Text      | KYC verification status |
