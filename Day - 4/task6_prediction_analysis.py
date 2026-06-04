import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "accident_50k.csv")
output_dir = os.path.join(script_dir, "task6_outputs")
os.makedirs(output_dir, exist_ok=True)

print("=" * 70)
print("TASK 6 - PREDICTION ANALYSIS")
print("=" * 70)

# ==================================================
# 1. read_csv()
# ==================================================

df = pd.read_csv(csv_path)

# ==================================================
# 2. shape
# ==================================================

print("\nDataset Shape")
print(df.shape)

# ==================================================
# 3. columns
# ==================================================

print("\nColumns")
print(df.columns.tolist())

# ==================================================
# 4. head()
# ==================================================

print("\nFirst 5 Records")
print(df.head())

# ==================================================
# 5. tail()
# ==================================================

print("\nLast 5 Records")
print(df.tail())

# ==================================================
# 6. info()
# ==================================================

print("\nDataset Info")
df.info()

# ==================================================
# 7. describe()
# ==================================================

print("\nStatistics")
print(df.describe())

# ==================================================
# 8. isnull()
# ==================================================

print("\nMissing Values")
print(df.isnull().sum())

# ==================================================
# 9. fillna()
# ==================================================

for col in df.columns:

    if df[col].dtype == "object":
        df[col] = df[col].fillna("Unknown")

    else:
        numeric_col = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(numeric_col.median())

# ==================================================
# 10. copy()
# ==================================================

data = df.copy()

# ==================================================
# 11. nunique()
# ==================================================

print("\nUnique Values")
print(data.nunique())

# ==================================================
# 12. value_counts()
# ==================================================

print("\nSeverity Counts")
print(
    data["Accident_Severity"]
    .value_counts()
)

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

print("\nCorrelation Matrix")
print(
    numeric.corr()
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
# Train Model
# ==================================================

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42
)

model.fit(X_train, y_train)

# ==================================================
# Predict
# ==================================================

y_pred = model.predict(X_test)

# ==================================================
# Accuracy
# ==================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nAccuracy")
print(f"{accuracy:.4f}")

# ==================================================
# Classification Report
# ==================================================

print("\nClassification Report")
print(
    classification_report(
        y_test,
        y_pred
    )
)

# ==================================================
# Confusion Matrix
# ==================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

# ==================================================
# Graph 1
# Confusion Matrix Heatmap
# ==================================================

plt.figure(figsize=(8,6))

sns.heatmap(

    cm,

    annot=True,

    fmt="d",

    cmap="Blues"
)

plt.title(
    "Confusion Matrix"
)

plt.savefig(
    os.path.join(output_dir, "confusion_matrix.png")
)

plt.close()

# ==================================================
# Graph 2
# Actual vs Predicted Counts
# ==================================================

actual_counts = pd.Series(
    y_test
).value_counts()

predicted_counts = pd.Series(
    y_pred
).value_counts()

comparison = pd.DataFrame({

    "Actual": actual_counts,

    "Predicted": predicted_counts

}).fillna(0)

comparison.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title(
    "Actual vs Predicted"
)

plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    os.path.join(output_dir, "actual_vs_predicted.png")
)

plt.close()

# ==================================================
# Graph 3
# Feature Importance
# ==================================================

importance = pd.DataFrame({

    "Feature": features,

    "Importance":
        model.feature_importances_

})

# ==================================================
# 15. sort_values()
# ==================================================

importance = importance.sort_values(

    by="Importance",

    ascending=False
)

plt.figure(figsize=(10,5))

sns.barplot(

    data=importance,

    x="Importance",

    y="Feature"
)

plt.title(
    "Feature Importance"
)

plt.savefig(
    os.path.join(output_dir, "feature_importance.png")
)

plt.close()

print("\nFeature Importance")
print(importance)

# ==================================================
# 16. sample()
# ==================================================

print("\nRandom Predictions")

sample_df = pd.DataFrame({

    "Actual": y_test,

    "Predicted": y_pred

})

print(
    sample_df.sample(10)
)

# ==================================================
# 17. to_csv()
# ==================================================

sample_df.to_csv(

    os.path.join(output_dir, "predictions.csv"),

    index=False
)

print("\nFiles Saved")


print("\nTASK 6 COMPLETED SUCCESSFULLY")