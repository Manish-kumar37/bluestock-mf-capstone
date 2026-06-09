import pandas as pd

perf = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

def recommend_funds(risk_level):

    risk_mapping = {
        "Low": ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High"]
    }

    filtered = perf[
        perf["risk_grade"].isin(
            risk_mapping[risk_level]
        )
    ]

    return (
        filtered.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        [
            [
                "scheme_name",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct"
            ]
        ]
        .head(3)
    )

if __name__ == "__main__":

    risk = input(
        "Enter Risk Level (Low/Moderate/High): "
    )

    print("\nTop Recommended Funds:\n")

    print(
        recommend_funds(risk)
    )