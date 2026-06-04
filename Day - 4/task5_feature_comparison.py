import os
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")
result_path = os.path.join(script_dir, "feature_comparison_results(task5).csv")

print("=" * 70)
print("TASK 5 - FEATURE COMPARISON")
print("=" * 70)

# ==================================================
# 1. read_csv()
# ==================================================

df = pd.read_csv(csv_path)

# ==================================================
# 2. shape
# ==================================================

print("\nDataset Shape:")
print(df.shape)

# ==================================================
# 3. columns
# ==================================================

print("\nColumns:")
print(df.columns.tolist())

# ==================================================
# 4. head()
# ==================================================

print("\nFirst 5 Records:")
print(df.head())

# ==================================================
# 5. info()
# ==================================================

print("\nDataset Info:")
df.info()

# ==================================================
# 6. isnull()
# ==================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==================================================
# 7. fillna()
# ==================================================

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        numeric_col = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(numeric_col.median())

# ==================================================
# 8. nunique()
# ==================================================

print("\nUnique Values:")
print(df.nunique())

# ==================================================
# 9. value_counts()
# ==================================================

print("\nSeverity Counts:")
print(df["Accident_Severity"].value_counts())

# ==================================================
# 10. groupby()
# ==================================================

print("\nAverage Casualties by Severity:")
print(
    df.groupby("Accident_Severity")
      ["Number_of_Casualties"]
      .mean()
)

# ==================================================
# 11. sort_values()
# ==================================================

print("\nTop Speed Limits:")
print(
    df[["Speed_limit"]]
      .sort_values(
          by="Speed_limit",
          ascending=False
      )
      .head()
)

# ==================================================
# 12. copy()
# ==================================================

data = df.copy()

# ==================================================
# 13. select_dtypes()
# ==================================================

cat_cols = data.select_dtypes(
    include="object"
).columns

# ==================================================
# Label Encoding
# ==================================================

encoders = {}

for col in cat_cols:

    le = LabelEncoder()

    data[col] = le.fit_transform(
        data[col].astype(str)
    )

    encoders[col] = le

# ==================================================
# 14. corr()
# ==================================================

numeric = data.select_dtypes(
    include=np.number
)

print("\nCorrelation Matrix:")
print(numeric.corr().round(2))

# ==================================================
# Target Variable
# ==================================================

target = "Accident_Severity"

# ==================================================
# Features To Compare
# ==================================================

feature_list = [

    "Speed_limit",

    "Number_of_Vehicles",

    "Number_of_Casualties",

    "Road_Type",

    "Weather_Conditions",

    "Light_Conditions",

    "Urban_or_Rural_Area",

    "Day_of_Week"

]

results = []

print("\n")
print("=" * 70)
print("FEATURE COMPARISON RESULTS")
print("=" * 70)

# ==================================================
# Compare Each Feature
# ==================================================

for feature in feature_list:

    X = data[[feature]]

    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(
        y_test,
        pred
    )

    results.append(
        [feature, acc]
    )

    print(f"{feature:30s} -> {acc:.4f}")

# ==================================================
# 15. DataFrame()
# ==================================================

result_df = pd.DataFrame(
    results,
    columns=[
        "Feature",
        "Accuracy"
    ]
)

# ==================================================
# 16. sort_values()
# ==================================================

result_df = result_df.sort_values(
    by="Accuracy",
    ascending=False
)

print("\n")
print("=" * 70)
print("FEATURE RANKING")
print("=" * 70)

print(result_df)

# ==================================================
# Best Feature
# ==================================================

best_feature = result_df.iloc[0]

print("\nBest Feature:")
print(f"Feature  : {best_feature['Feature']}")
print(f"Accuracy : {best_feature['Accuracy']:.4f}")

# ==================================================
# 17. describe()
# ==================================================

print("\nFeature Accuracy Statistics:")
print(result_df["Accuracy"].describe())

# ==================================================
# 18. sample()
# ==================================================

print("\nRandom Result Sample:")
print(result_df.sample(3))

# ==================================================
# Save Result
# ==================================================

result_df.to_csv(
    result_path,
    index=False
)

print("\nResults saved as:")
print(result_path)

print("\nTASK 5 COMPLETED SUCCESSFULLY")