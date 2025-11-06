# -*- coding: utf-8 -*-
"""
Parquet → CSV Converter

Allows converting a .parquet file into a .csv file.
User inputs are requested via CLI.
"""

import pandas as pd
from pathlib import Path

def parquet_to_csv():
    print("\n=== PARQUET → CSV Converter ===")

    while True:
        parquet_path = input("\n📥 Enter input .parquet file path: ").strip().replace('"', '')
        csv_path = input("📤 Enter output .csv file path (including filename): ").strip().replace('"', '')

        try:
            df = pd.read_parquet(parquet_path)
            df.to_csv(csv_path, index=False)

            print(f"\n✅ Conversion complete!\n📄 CSV saved as: {csv_path}")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    parquet_to_csv()
