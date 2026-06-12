"""
Phase 1: Dataset Understanding

This script contains the Phase 1 code from Superstore_EDA.ipynb.
It loads the raw Superstore dataset and prints basic dataset checks.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "Datasets" / "Superstore.csv"


def main() -> None:
    data = pd.read_csv(RAW_DATA_PATH, encoding="unicode_escape")

    print("\nDataset Info")
    print("=" * 50)
    data.info()

    print("\nFirst 5 Rows")
    print("=" * 50)
    print(data.head())

    print("\nDescriptive Statistics")
    print("=" * 50)
    print(data.describe())

    print("\nDuplicate Row Count")
    print("=" * 50)
    print(data.duplicated().sum())


if __name__ == "__main__":
    main()
