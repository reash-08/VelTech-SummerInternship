import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "Accident_Information.csv"
df = pd.read_csv(csv_path)

print("Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 3 Rows:")
print(df.tail(3))

