import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

def age_scatter_plot(df):
    # Set groups
    male_lifters = df[df["Sex"] == "M"]
    female_lifters = df[df["Sex"] == "F"]

    # Scatter plot
    plt.scatter(
        male_lifters["Age"],
        male_lifters["TotalKg"],
        label="Male",
        color="skyblue",
        alpha=0.5,
        s=20
    )

    plt.scatter(
        female_lifters["Age"],
        female_lifters["TotalKg"],
        label="Female",
        color="lightcoral",
        alpha=0.5,
        s=20
    )

    plt.xlabel("Age")
    plt.ylabel("Total Kg")
    plt.legend(title="Sex")

    plt.tight_layout()
    plt.show()

age_scatter_plot(df)