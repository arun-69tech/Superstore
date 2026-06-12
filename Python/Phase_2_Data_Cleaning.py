"""
Phase 2: Python Data Cleaning

This script contains the Phase 2 code from Superstore_EDA.ipynb.
It cleans the raw Superstore dataset and exports cleaned_superstore.csv.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "Datasets" / "Superstore.csv"
CLEANED_DATA_PATH = PROJECT_ROOT / "Datasets" / "cleaned_superstore.csv"


def main() -> None:
    data = pd.read_csv(RAW_DATA_PATH, encoding="unicode_escape")

    data.drop(columns="Row ID", inplace=True)
    data["Postal Code"] = data["Postal Code"].astype(str)
    data["Order Date"] = pd.to_datetime(data["Order Date"], dayfirst=True)
    data["Ship Date"] = pd.to_datetime(data["Ship Date"], dayfirst=True)
    data["Shipping Duration"] = (data["Ship Date"] - data["Order Date"]).dt.days
    data["Order Year"] = data["Order Date"].dt.year
    data["Order Month"] = data["Order Date"].dt.month_name()
    data["Order Quarter"] = data["Order Date"].dt.quarter

    print("\nCleaned Dataset Info")
    print("=" * 50)
    data.info()

    print("\nDuplicate Row Count Before Dropping")
    print("=" * 50)
    print(data.duplicated().sum())

    print("\nDuplicate Rows")
    print("=" * 50)
    print(data[data.duplicated(keep=False)])

    data.drop_duplicates(inplace=True)

    print("\nDuplicate Row Count After Dropping")
    print("=" * 50)
    print(data.duplicated().sum())

    data.to_csv(CLEANED_DATA_PATH, index=False, encoding="utf-8")
    print(f"\nCleaned dataset exported to: {CLEANED_DATA_PATH}")


if __name__ == "__main__":
    main()
