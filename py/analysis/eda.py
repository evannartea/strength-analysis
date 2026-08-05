from tabulate import tabulate
import pandas as pd

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

male_lifters = df[df["Sex"] == "M"].drop(columns=["Place"])
female_lifters = df[df["Sex"] == "F"].drop(columns=["Place"])

summary_m = male_lifters.describe().round(1)
print(f"{tabulate(summary_m, headers='keys', tablefmt='github')}\n")

summary_f = female_lifters.describe().round(1)
print(f"{tabulate(summary_f, headers='keys', tablefmt='github')}\n")

null_count = df.isnull().sum().reset_index()
print(tabulate(null_count, headers=["Column", "Null Count"], tablefmt="github", showindex=False))