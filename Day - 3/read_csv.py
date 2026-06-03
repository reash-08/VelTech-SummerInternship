import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "student-mat.csv"
df = pd.read_csv(csv_path, sep="\t")

print("Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 3 Rows:")
print(df.tail(3))

print("\nInternet Access Count:")
print(df["internet"].value_counts())