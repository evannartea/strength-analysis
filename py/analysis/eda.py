from tabulate import tabulate
import pandas as pd

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

summary = df.describe().round(1)
print(tabulate(summary, headers="keys", tablefmt="github"))

null_count = df.isnull().sum().reset_index()
print(tabulate(null_count, headers=["Column", "Null Count"], tablefmt="github", showindex=False))