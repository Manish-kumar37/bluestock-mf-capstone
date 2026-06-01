"""
live_nav_fetch.py — Tasks 4 & 5: Fetch live NAV from mfapi.in
Bluestock MF Capstone Project
"""

import pathlib
import requests
import pandas as pd
from datetime import datetime

# ── Paths ──────────────────────────────────────────────────────────────────
ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

BASE_URL = "https://api.mfapi.in/mf"

# ── Task 4 & 5: 5 Key Schemes ─────────────────────────────────────────────
SCHEMES = {
    125497: "HDFC Top 100 Direct",
    119551: "SBI Bluechip Direct",
    120503: "ICICI Prudential Bluechip Direct",
    118632: "Nippon India Large Cap Direct",
    119092: "Axis Bluechip Direct",
    120841: "Kotak Bluechip Direct",
}


def fetch_nav(scheme_code: int, scheme_name: str) -> pd.DataFrame | None:
    """Fetch full NAV history for a scheme and return as DataFrame."""
    url = f"{BASE_URL}/{scheme_code}"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        meta = data.get("meta", {})
        nav_records = data.get("data", [])

        if not nav_records:
            print(f"  [WARN] No NAV data returned for {scheme_name} ({scheme_code})")
            return None

        df = pd.DataFrame(nav_records)
        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")
        df["scheme_code"] = scheme_code
        df["scheme_name"] = meta.get("scheme_name", scheme_name)
        df["fund_house"] = meta.get("fund_house", "")
        df["scheme_type"] = meta.get("scheme_type", "")
        df["scheme_category"] = meta.get("scheme_category", "")
        df = df.sort_values("date").reset_index(drop=True)

        print(f"  ✓ {scheme_name:<40} | {len(df):>5} records | "
              f"Latest NAV: ₹{df['nav'].iloc[-1]:.4f} on {df['date'].iloc[-1].date()}")
        return df

    except requests.exceptions.ConnectionError:
        print(f"  [ERROR] Network error for {scheme_name} ({scheme_code}). Check connection.")
        return None
    except requests.exceptions.Timeout:
        print(f"  [ERROR] Timeout for {scheme_name} ({scheme_code}).")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"  [ERROR] HTTP {e.response.status_code} for {scheme_name} ({scheme_code}).")
        return None
    except Exception as e:
        print(f"  [ERROR] Unexpected error for {scheme_name}: {e}")
        return None


def fetch_all_schemes() -> pd.DataFrame:
    """Fetch NAV for all 6 schemes and save individual + combined CSVs."""
    print("\n" + "="*60)
    print("  Fetching live NAV data from mfapi.in")
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

    all_dfs = []
    for code, name in SCHEMES.items():
        df = fetch_nav(code, name)
        if df is not None:
            # Save individual CSV
            fname = f"nav_{code}_{name.lower().replace(' ', '_')}.csv"
            df.to_csv(RAW / fname, index=False)
            all_dfs.append(df)

    if not all_dfs:
        print("\n  [ERROR] No data fetched. Check your internet connection.")
        return pd.DataFrame()

    # Combined file
    combined = pd.concat(all_dfs, ignore_index=True)
    combined_path = RAW / "nav_live_all_schemes.csv"
    combined.to_csv(combined_path, index=False)

    print(f"\n  Combined CSV saved → {combined_path}")
    print(f"  Total records: {len(combined):,}")
    print(f"  Schemes fetched: {combined['scheme_code'].nunique()}")
    print(f"  Date range: {combined['date'].min().date()} → {combined['date'].max().date()}")
    return combined


if __name__ == "__main__":
    df = fetch_all_schemes()
    if not df.empty:
        print("\n  Latest NAV snapshot:")
        latest = (
            df.sort_values("date")
            .groupby("scheme_code")
            .last()[["scheme_name", "date", "nav"]]
            .reset_index()
        )
        print(latest.to_string(index=False))
        print("\n  ✓ live_nav_fetch.py complete.")
