import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    data = pd.read_csv("epa-sea-level.csv")
    fig, ax = plt.subplots()
    ax.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

    all_years_fit = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    all_years = range(1880, 2051)
    ax.plot(
        all_years,
        [all_years_fit.intercept + all_years_fit.slope * year for year in all_years],
        "r",
    )

    recent_data = data[data["Year"] >= 2000]
    recent_fit = linregress(
        recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"]
    )
    recent_years = range(2000, 2051)
    ax.plot(
        recent_years,
        [recent_fit.intercept + recent_fit.slope * year for year in recent_years],
        "r",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    fig.savefig("sea_level_plot.png")
    return ax
