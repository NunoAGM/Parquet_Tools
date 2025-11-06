# -*- coding: utf-8 -*-
"""
Parquet → Excel Converter

Allows converting a .parquet file into an Excel (.xlsx) file.
User inputs are requested via CLI.
"""

import pandas as pd
from pathlib import Path

def parquet_to_excel():
    while True:
        parquet_path = input("\n📥 Enter the path of the .parquet file to convert: ").strip().replace('"', '')
        try:
            df = pd.read_parquet(parquet_path)
            output_path = parquet_path.replace('.parquet', '.xlsx')

            df.to_excel(output_path, index=False)
            print(f"\n✅ Conversion complete!\n📄 Saved as: {output_path}")
            break

        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    parquet_to_excel()
