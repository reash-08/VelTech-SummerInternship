import os
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("="*60)
print("ACCIDENT SEVERITY PREDICTION")
print("="*60)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")

# ==================================================
# 1. read_csv()
# ==================================================

df = pd.read_csv(csv_path)

# ==================================================
# 2. head()
# ==================================================

print("\nFIRST 5 RECORDS")
print(df.head())

# ==================================================
# 3. tail()
# ==================================================

print("\nLAST 5 RECORDS")
print(df.tail())

# ==================================================
# 4. shape
# ==================================================

print("\nDATASET SHAPE")
print(df.shape)

# ==================================================
# 5. columns
# ==================================================

print("\nCOLUMN NAMES")
print(df.columns.tolist())

# ==================================================
# 6. info()
# ==================================================

print("\nDATASET INFO")
df.info()

# ==================================================
# 7. describe()
# ==================================================

print("\nNUMERICAL SUMMARY")
print(df.describe())

# ==================================================
# 8 & 9. isnull() and sum()
# ==================================================

print("\nMISSING VALUES")
print(df.isnull().sum())

# ==================================================
# 10. fillna()
# ==================================================

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")
    else:
        numeric_col = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(numeric_col.median())

# ==================================================
# 11. astype()
# ==================================================

df["Speed_limit"] = df["Speed_limit"].astype(int)

# ==================================================
# 12. value_counts()
# ==================================================

print("\nACCIDENT SEVERITY COUNTS")
print(df["Accident_Severity"].value_counts())

# ==================================================
# 13. groupby()
# ==================================================

print("\nAVERAGE CASUALTIES BY SEVERITY")

severity_stats = (
    df.groupby("Accident_Severity")
    ["Number_of_Casualties"]
    .mean()
)

print(severity_stats)

# ==================================================
# 14. sort_values()
# ==================================================

print("\nTOP SPEED LIMITS")

print(
    df[["Speed_limit"]]
    .sort_values(
        by="Speed_limit",
        ascending=False
    )
    .head()
)

# ==================================================
# 15. drop()
# ==================================================

df = df.drop(
    columns=[
        "Accident_Index"
    ],
    errors="ignore"
)

# ==================================================
# 16. copy()
# ==================================================

data = df.copy()

# ==================================================
# 17. nunique()
# ==================================================

print("\nUNIQUE VALUES")

print(
    data.nunique()
    .sort_values(
        ascending=False
    )
    .head(10)
)

# ==================================================
# 18. select_dtypes()
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
# 19. corr()
# ==================================================

print("\nCORRELATION MATRIX")

numeric_cols = data.select_dtypes(
    include=np.number
)

print(
    numeric_cols.corr()
    .round(2)
)

# ==================================================
# Features
# ==================================================

features = [
    "Road_Type",
    "Weather_Conditions",
    "Light_Conditions",
    "Speed_limit",
    "Number_of_Vehicles",
    "Number_of_Casualties",
    "Urban_or_Rural_Area",
    "Day_of_Week"
]

target = "Accident_Severity"

X = data[features]

y = data[target]

# ==================================================
# 20. sample()
# ==================================================

print("\nRANDOM SAMPLE")

print(
    data.sample(5)
)

# ==================================================
# Train Test Split
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==================================================
# Random Forest Model
# ==================================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# ==================================================
# Prediction
# ==================================================

pred = model.predict(X_test)

# ==================================================
# Accuracy
# ==================================================

accuracy = accuracy_score(
    y_test,
    pred
)

print("\n" + "="*60)
print("MODEL RESULTS")
print("="*60)

print(f"Accuracy : {accuracy:.4f}")

# ==================================================
# Classification Report
# ==================================================

print("\nCLASSIFICATION REPORT")

print(
    classification_report(
        y_test,
        pred
    )
)

# ==================================================
# Confusion Matrix
# ==================================================

print("\nCONFUSION MATRIX")

print(
    confusion_matrix(
        y_test,
        pred
    )
)

# ==================================================
# Feature Importance
# ==================================================

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")

print(importance)

print("\nTASK 4 COMPLETED SUCCESSFULLY")