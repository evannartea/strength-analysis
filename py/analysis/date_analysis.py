import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# ====================
#       Unfiltered
# ====================

# SBD by Year
def unfilitered_sbd_year_m_line_chart(df):
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

    plt.figure(figsize=(12,6))
    plt.xlabel("Year")
    plt.ylabel("Average Weight (kg)")
    plt.legend(title="Lift")
    plt.tight_layout()

    plt.savefig("figures/unfiltered_sbd_m_by_year.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

def unfilitered_sbd_year_f_line_chart(df):
    female_lifters = df[df["Sex"] == "F"]
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

    plt.figure(figsize=(12,6))
    plt.xlabel("Year")
    plt.ylabel("Average Weight (kg)")
    plt.legend(title="Lift")
    plt.tight_layout()

    plt.savefig("figures/unfiltered_sbd_f_by_year.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

# ====================
#       Filtered
# ====================

def filtered_sbd_year_m_line_chart(df):
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

    plt.figure(figsize=(12,6))
    plt.xlabel("Year")
    plt.ylabel("Average Weight (kg)")
    plt.legend(title="Lift")
    plt.tight_layout()

    plt.savefig("figures/filtered_sbd_m_by_year.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

def filtered_sbd_year_f_line_chart(df):
    female_lifters = df[(df["Sex"] == "F") & (df["Year"] >= 2008)]
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

    plt.figure(figsize=(12,6))
    plt.xlabel("Year")
    plt.ylabel("Average Weight (kg)")
    plt.legend(title="Lift")
    plt.gca().xaxis.set_major_locator(MultipleLocator(5))
    plt.tight_layout()

    plt.savefig("figures/filtered_sbd_f_by_year.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

unfilitered_sbd_year_m_line_chart(df)
unfilitered_sbd_year_f_line_chart(df)

filtered_sbd_year_m_line_chart(df)
filtered_sbd_year_f_line_chart(df)