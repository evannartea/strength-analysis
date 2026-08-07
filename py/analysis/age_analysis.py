import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# TotalKg by Age
def age_total_scatter_plot(df):
    # Set groups
    male_lifters = df[df["Sex"] == "M"]
    female_lifters = df[df["Sex"] == "F"]

    # Scatter plot
    plt.scatter(
        x=male_lifters["Age"],
        y=male_lifters["TotalKg"],
        label="Male",
        color="skyblue",
        alpha=0.5,
        s=20
    )
    plt.scatter(
        x=female_lifters["Age"],
        y=female_lifters["TotalKg"],
        label="Female",
        color="lightcoral",
        alpha=0.5,
        s=20
    )

    plt.xlabel("Age")
    plt.ylabel("Total (kg)")
    plt.legend(title="Sex")

    plt.tight_layout()
    plt.show()

# Avg TotalKg by AgeClass
def ageclass_total_bar_chart(df):
    male_lifters = df[df["Sex"] == "M"]
    female_lifters = df[df["Sex"] == "F"]

    # Get averages
    avg_total_m = male_lifters.groupby("AgeClass")["TotalKg"].mean()
    avg_total_f = female_lifters.groupby("AgeClass")["TotalKg"].mean()

    # Separate bars
    x = np.arange(len(avg_total_m.index))
    width = 0.35

    # Bar chart
    plt.bar(
        x - width/2,
        avg_total_m.values,
        width,
        label="Male",
        color="skyblue"
    )
    plt.bar(
        x + width/2,
        avg_total_f.values,
        width,
        label="Female",
        color="lightcoral"
    )

    plt.xticks(x, avg_total_m.index)
    plt.xlabel("Age Class")
    plt.ylabel("Average Total (kg)")
    plt.legend(title="Sex")

    plt.tight_layout()
    plt.show()

age_total_scatter_plot(df)
ageclass_total_bar_chart(df)
