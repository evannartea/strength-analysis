import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# Squat by Country
def squat_country_bar_chart():
    plt.figure(figsize=(12,6))
    
    male_lifters = df[df["Sex"] == "M"]
    female_lifters = df[df["Sex"] == "F"]

    avg_squat_m = male_lifters.groupby("Country")["SquatKg"].mean()
    avg_squat_f = female_lifters.groupby("Country")["SquatKg"].mean()

    x = np.arange(len(avg_squat_m.index))
    width = 0.35

    # Bar chart
    plt.bar(
        x - width/2,
        avg_squat_m.values,
        width,
        label="Male",
        color="skyblue"
    )
    plt.bar(
        x + width/2,
        avg_squat_f.values,
        width,
        label="Female",
        color="lightcoral"
    )

    plt.xticks(x, avg_squat_m.index)
    plt.xlabel("Country")
    plt.ylabel("Average Weight (kg)")
    plt.legend(title="Sex")

    plt.tight_layout()
    #plt.savefig("figures/squat_by_country.png", dpi=300, bbox_inches="tight")
    #print("Figure saved successfully!")
    plt.close()
    #plt.show()

    
# Bench by Country:
def bench_country_bar_chart():
    ...

def deadlift_country_bar_chart():
    ...

squat_country_bar_chart(df)