import pandas as pd

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

print(df.describe().round(1))
print(df.isnull().sum())