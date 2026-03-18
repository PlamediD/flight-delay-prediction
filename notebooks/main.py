# -------------------------------
# flight_delay_analysis.py
# -------------------------------

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Config
# -------------------------------
DATA_PATH = "./data/flight_data.csv"
OUT_VIS = "../visuals"
os.makedirs(OUT_VIS, exist_ok=True)
sns.set_theme(style="whitegrid")


# -------------------------------
# Functions
# -------------------------------

def load_data(path: str) -> pd.DataFrame:
    """Load CSV data into a DataFrame."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows with missing arrival delay."""
    df_clean = df.dropna(subset=["ARR_DELAY"])
    print(f"Dataset shape after cleaning: {df_clean.shape}")
    return df_clean


def compute_delay_stats(df: pd.DataFrame) -> float:
    """Compute overall arrival delay >15 min rate."""
    delay_rate = df["ARR_DEL15"].mean() * 100
    print(f"In January 2025, approximately {delay_rate:.2f}% of flights "
          "experienced arrival delays of at least 15 minutes.")
    return delay_rate


def compute_airline_delay(df: pd.DataFrame) -> pd.Series:
    """Compute average delay rate per airline."""
    airline_delay = (
        df.groupby("OP_UNIQUE_CARRIER")["ARR_DEL15"]
        .mean()
        .sort_values(ascending=False)
    )
    print("\nAirline Delay Rate:")
    print(airline_delay)
    return airline_delay


def plot_airline_delay(airline_delay: pd.Series, out_path: str):
    """Plot and save the arrival delay rate per airline."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x=airline_delay.index, y=airline_delay.values)
    plt.xticks(rotation=45)

    plt.title("Arrival Delay Rate by Airline")
    plt.xlabel("Airline")
    plt.ylabel("Delay Rate")

    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()
    print(f"Visualization saved to: {out_path}")

def compute_delay_by_day(df: pd.DataFrame) -> pd.Series:
    """Compute overall arrival delay per day."""
    delay_by_day=(
        df.groupby("DAY_OF_WEEK")["ARR_DEL15"].mean().sort_index()
    )
    print("\nDelay Rate by Day of Week:")
    print(delay_by_day)
    return delay_by_day

def plot_delay_by_day(delay_by_day: pd.Series, out_path: str):
    """Plot and save the delay by day."""
    plt.figure(figsize=(8, 5))
    sns.barplot(x=delay_by_day.index, y=delay_by_day.values)
    plt.xticks(ticks=range(7), labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    plt.title("Delay by Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Delay Rate")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()
    print(f"Visualization saved to: {out_path}")

'''def compute_delay_by_month(df: pd.DataFrame) -> pd.Series:'''
# -------------------------------
# Main Workflow
# -------------------------------

def main():
    # Load & clean data
    df = load_data(DATA_PATH)
    df = clean_data(df)

    # Compute statistics
    compute_delay_stats(df)
    airline_delay = compute_airline_delay(df)
    delay_by_day = compute_delay_by_day(df)



    # Plot & save figure
    'Arrival Delay Rate by Airline'
    plot_path = os.path.join(OUT_VIS, "arrival_delay_rate_airline.png")
    plot_airline_delay(airline_delay, plot_path)

    'Delay by day of the week visualization'
    plot_path_day = os.path.join(OUT_VIS, "delay_rate_by_day.png")
    plot_delay_by_day(delay_by_day, plot_path_day)


if __name__ == "__main__":
    main()