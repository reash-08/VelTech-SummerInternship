import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")

# =========================
# Pandas Functions Section
# =========================

# Load dataset
print("\nLoading dataset from:", csv_path)
df = pd.read_csv(csv_path)

# 1. shape
print("\nDataset Shape:")
print(df.shape)

# 2. columns
print("\nColumns:")
print(df.columns.tolist())

# 3. head()
print("\nFirst 5 Rows:")
print(df.head())

# 4. tail()
print("\nLast 5 Rows:")
print(df.tail())

# 5. info()
print("\nDataset Info:")
df.info()

# 6. describe()
print("\nStatistical Summary:")
print(df.describe())

# 7. isnull()
print("\nMissing Values:")
print(df.isnull().sum())

# 8. fillna()
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        numeric_col = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(numeric_col.median())

# 9. value_counts()
print("\nAccident Severity Counts:")
print(df["Accident_Severity"].value_counts())

# 10. nunique()
print("\nUnique Values Per Column:")
print(df.nunique())

# 11. groupby()
print("\nAverage Casualties by Severity:")
print(
    df.groupby("Accident_Severity")["Number_of_Casualties"]
    .mean()
)

# 12. sort_values()
print("\nTop 5 Highest Speed Limits:")
print(
    df.sort_values(
        by="Speed_limit",
        ascending=False
    )[["Speed_limit"]].head()
)

# 13. sample()
print("\nRandom Sample:")
print(df.sample(5))

# 14. select_dtypes()
print("\nNumeric Columns:")
print(
    df.select_dtypes(
        include="number"
    ).columns.tolist()
)

# 15. corr()
numeric_df = df.select_dtypes(include="number")

print("\nCorrelation Matrix:")
print(
    numeric_df.corr(numeric_only=True)
)

# 16. copy()
data_copy = df.copy()

# 17. drop()
temp_df = data_copy.drop(
    columns=["Accident_Index"],
    errors="ignore"
)

# 18. astype()
if "Speed_limit" in temp_df.columns:
    temp_df["Speed_limit"] = (
        temp_df["Speed_limit"]
        .astype(float)
    )

# 19. DataFrame()
summary_df = pd.DataFrame({
    "Column": df.columns,
    "Missing": df.isnull().sum().values
})

print("\nSummary DataFrame:")
print(summary_df.head())

# 20. to_csv()
summary_df.to_csv(
    "task3_summary.csv",
    index=False
)