import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent / "Accident_Information.csv"

df = pd.read_csv(csv_path)

print("Initial null counts per column:")
null_counts = df.isnull().sum()
print(null_counts)

null_columns = null_counts[null_counts > 0]
if null_columns.empty:
    print("\nNo missing values found.")
else:
    print("\nColumns with missing values and counts:")
    print(null_columns)

# Fill numeric nulls with the column mean.
numeric_columns = df.select_dtypes(include=["number"]).columns
if not numeric_columns.empty:
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Fill text/null object columns with 'Unknown'.
text_columns = df.select_dtypes(include=["object", "string", "category"]).columns
if not text_columns.empty:
    df[text_columns] = df[text_columns].fillna("Unknown")

# If you wanted to drop any remaining rows with nulls instead of filling them:
# df.dropna(inplace=True)

print("\nNull counts after filling:")
null_counts_after = df.isnull().sum()
print(null_counts_after)
print("\nTotal missing values after fill:", null_counts_after.sum())

if null_counts_after.sum() == 0:
    print("\nVerification: No nulls remain.")
    df.to_csv(csv_path, index=False)
    print(f"Filled data saved back to {csv_path.name}.")
else:
    print("\nWarning: Some nulls remain. Check the data types or special missing values.")
