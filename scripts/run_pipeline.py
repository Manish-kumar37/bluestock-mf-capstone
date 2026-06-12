"""
Master Execution Script

This script runs the complete Mutual Fund Analytics pipeline:

1. Fetch Live NAV Data
2. Run ETL Pipeline

Author: Manish Kumar
Project: Bluestock Mutual Fund Analytics Capstone
"""

import subprocess
import sys


def run_script(script_name):
    """Execute a Python script and stop if an error occurs."""

    print(f"\n{'=' * 50}")
    print(f"Running: {script_name}")
    print(f"{'=' * 50}")

    result = subprocess.run(
        [sys.executable, script_name]
    )

    if result.returncode != 0:
        print(f"\nError while running {script_name}")
        sys.exit(result.returncode)

    print(f"\nCompleted: {script_name}")


def main():
    """Run the complete analytics pipeline."""

    run_script("scripts/live_nav_fetch.py")
    run_script("scripts/etl_pipeline.py")

    print("\nPipeline executed successfully.")


if __name__ == "__main__":
    main()