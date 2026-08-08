import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean/openpowerlifting_20260801.csv")

# Total by Country
def total_country_m_bar_chart(df):
    df_filtered = df[(df["Sex"] == "M") & (df["AgeClass"].isin(["24-34", "35-39"]))]

    country_counts = df_filtered["Country"].value_counts()
    valid_countries = country_counts[country_counts > 1000].index

    male_lifters = df_filtered[
    df_filtered["Country"].isin(valid_countries)
    ]

    avg_total_m = (
        male_lifters
        .groupby("Country")["TotalKg"]
        .mean()
        .sort_values(ascending=False)
        .head(20)
    )

    plt.figure(figsize=(12,6))

    # Bar chart
    bars = plt.bar(
       avg_total_m.index,
       avg_total_m.values,
       color="skyblue"
    )

    plt.bar_label(
        bars,
        fmt="%.1f",
        fontsize=8,
        padding=3
    )

    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Average Total (kg)")
    plt.tight_layout()

    plt.savefig("figures/total_by_country_m.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

def total_country_f_bar_chart(df):
    df_filtered = df[(df["Sex"] == "F") & (df["AgeClass"].isin(["24-34", "35-39"]))]
    
    country_counts = df_filtered["Country"].value_counts()
    valid_countries = country_counts[country_counts > 1000].index

    female_lifters = df_filtered[
    df_filtered["Country"].isin(valid_countries)
    ]

    avg_total_f = (
        female_lifters
        .groupby("Country")["TotalKg"]
        .mean()
        .sort_values(ascending=False)
        .head(20)
    )

    plt.figure(figsize=(12,6))

    # Bar chart
    bars = plt.bar(
       avg_total_f.index,
       avg_total_f.values,
       color="lightcoral"
    )

    plt.bar_label(
        bars,
        fmt="%.1f",
        fontsize=8,
        padding=3
    )

    plt.xticks(rotation=45)
    plt.xlabel("Country")
    plt.ylabel("Average Total (kg)")
    plt.tight_layout()

    plt.savefig("figures/total_by_country_f.png", dpi=300, bbox_inches="tight")
    print("Figure saved successfully!")
    plt.close()
    #plt.show()

total_country_m_bar_chart(df)
total_country_f_bar_chart(df)