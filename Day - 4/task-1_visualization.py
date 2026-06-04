import pandas as pd

df = pd.read_csv("accident_50k.csv")

print(df.shape)
print(df.columns.tolist())
print(df.head())