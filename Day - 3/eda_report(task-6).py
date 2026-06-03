import pandas as pd
from pathlib import Path


def eda_report(df: pd.DataFrame) -> None:
    """Print a concise EDA report for a DataFrame.

    Prints shape, null counts, numeric describe(), and value_counts() for object columns.
    """
    print("DataFrame shape:", df.shape)

    print("\nNull counts per column:")
    print(df.isnull().sum())

    numeric_df = df.select_dtypes(include=["number"])
    print("\nNumeric column summary (describe):")
    if not numeric_df.empty:
        print(numeric_df.describe())
    else:
        print("  No numeric columns found.")

    object_cols = df.select_dtypes(include=["object", "string", "category"]).columns
    if len(object_cols) > 0:
        print("\nValue counts for object/string/category columns:")
        for col in object_cols:
            print(f"\n--- {col} ---")
            print(df[col].value_counts(dropna=False))
    else:
        print("\nNo object/string/category columns found.")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    accident_csv = base_dir / "Accident_Information.csv"

    print("=== EDA Report for Accident_Information.csv ===")
    acc_df = pd.read_csv(accident_csv)
    eda_report(acc_df)
import pandas as pd
from pathlib import Path


def eda_report(df: pd.DataFrame) -> None:
    """Print a simple EDA report for any DataFrame."""
    print("DataFrame shape:", df.shape)
    print("\nNull counts per column:")
    print(df.isnull().sum())

    numeric_df = df.select_dtypes(include=["number"])
    print("\nNumeric column summary:")
    if numeric_df.shape[1] > 0:
        print(numeric_df.describe())
    else:
        print("  No numeric columns found.")

    object_cols = df.select_dtypes(include=["object", "string", "category"]).columns
    if len(object_cols) > 0:
        print("\nValue counts for object/string/category columns:")
        for col in object_cols:
            print(f"\n{col}:")
            print(df[col].value_counts(dropna=False))
    else:
        print("\nNo object/string/category columns found.")


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent

    accident_csv = base_dir / "Accident_Information.csv"
    
    print("=== EDA Report for Accident_Information.csv ===")
    accident_df = pd.read_csv(accident_csv)
    eda_report(accident_df)

