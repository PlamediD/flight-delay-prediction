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
    plt.title("Arrival Delay Rate by Airline")
    plt.xlabel("Airline")
    plt.ylabel("Delay Rate")

    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()
    print(f"Visualization saved to: {out_path}")


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

    # Plot & save figure
    plot_path = os.path.join(OUT_VIS, "arrival_delay_rate_airline.png")
    plot_airline_delay(airline_delay, plot_path)


if __name__ == "__main__":
    main()