import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# SBD by Year
def unfilitered_sbd_year_line_chart(df):
    plt.figure(figsize=(12,6))

    male_lifters = df[df["Sex"] == "M"]
    yearly_avg = male_lifters.groupby("Year")[["SquatKg", "BenchKg", "DeadliftKg"]].mean()

    plt.plot(
        yearly_avg.index,
        yearly_avg["SquatKg"],
        label="Squat",
        color="#ffae20"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["BenchKg"],
        label="Bench",
        color="#00e0d9"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["DeadliftKg"],
        label="Deadlift",
        color="#cba5ff"
    )

    plt.xlabel("Year")
    plt.ylabel("Weight (kg)")
    plt.legend(title="Lift")

    plt.tight_layout()
    plt.savefig("figures/unfiltered_sbd_by_year.png", dpi=300, bbox_inches="tight")
    plt.close()
    #plt.show()

def filtered_sbd_year_m_line_chart(df):
    plt.figure(figsize=(12,6))

    male_lifters = df[(df["Sex"] == "M") & (df["Year"] >= 1998)]
    yearly_avg = male_lifters.groupby("Year")[["SquatKg", "BenchKg", "DeadliftKg"]].mean()

    plt.plot(
        yearly_avg.index,
        yearly_avg["SquatKg"],
        label="Squat",
        color="#ffae20"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["BenchKg"],
        label="Bench",
        color="#00e0d9"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["DeadliftKg"],
        label="Deadlift",
        color="#cba5ff"
    )

    plt.xlabel("Year")
    plt.ylabel("Weight (kg)")
    plt.legend(title="Lift")

    plt.tight_layout()
    #plt.savefig("figures/unfiltered_sbd_by_year.png", dpi=300, bbox_inches="tight")
    #plt.close()
    plt.show()

def filtered_sbd_year_f_line_chart(df):
    plt.figure(figsize=(12,6))

    female_lifters = df[(df["Sex"] == "F") & (df["Year"] >= 1998)]
    yearly_avg = female_lifters.groupby("Year")[["SquatKg", "BenchKg", "DeadliftKg"]].mean()

    plt.plot(
        yearly_avg.index,
        yearly_avg["SquatKg"],
        label="Squat",
        color="#ffae20"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["BenchKg"],
        label="Bench",
        color="#00e0d9"
    )
    plt.plot(
        yearly_avg.index,
        yearly_avg["DeadliftKg"],
        label="Deadlift",
        color="#cba5ff"
    )

    plt.xlabel("Year")
    plt.ylabel("Weight (kg)")
    plt.legend(title="Lift")

    plt.tight_layout()
    #plt.savefig("figures/unfiltered_sbd_by_year.png", dpi=300, bbox_inches="tight")
    #plt.close()
    plt.show()

#unfilitered_sbd_year_line_chart(df)
filtered_sbd_year_m_line_chart(df)
filtered_sbd_year_f_line_chart(df)