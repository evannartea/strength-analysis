import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# Total by Country
def total_country_m_bar_chart(df):
    male_lifters = df[df["Sex"] == "M"]
    avg_squat_m = (
        male_lifters
        .groupby("Country")["TotalKg"]
        .mean()
        .sort_values(ascending=False)
        .head(20)
    )

    plt.figure(figsize=(12,6))
    
    # Bar chart
    plt.bar(
       avg_squat_m.index,
       avg_squat_m.values
    )

    plt.xlabel("Country")
    plt.ylabel("Average Total (kg)")
    plt.tight_layout()

    #plt.savefig("figures/squat_by_country.png", dpi=300, bbox_inches="tight")
    #print("Figure saved successfully!")
    #plt.close()
    plt.show()

total_country_m_bar_chart(df)