import pandas as pd

def compute_delay_stats(df: pd.DataFrame) -> float:
    delay_rate = df["ARR_DEL15"].mean() * 100
    print(f"In January 2025, approximately {delay_rate:.2f}% of flights experienced delays.")
    return delay_rate


def compute_airline_delay(df: pd.DataFrame) -> pd.Series:
    return (
        df.groupby("OP_UNIQUE_CARRIER")["ARR_DEL15"]
        .mean()
        .sort_values(ascending=False)
    )


def compute_delay_by_day(df: pd.DataFrame) -> pd.Series:
    return (
        df.groupby("DAY_OF_WEEK")["ARR_DEL15"]
        .mean()
        .sort_index()
    )


def get_best_worst_days(delay_by_day: pd.Series):
    return delay_by_day.idxmax(), delay_by_day.idxmin()


def get_root_cause_analysis(df: pd.DataFrame):
    delay_cols = [
        "CARRIER_DELAY",
        "WEATHER_DELAY",
        "NAS_DELAY",
        "SECURITY_DELAY",
        "LATE_AIRCRAFT_DELAY"
    ]

    df = df.copy()
    df[delay_cols] = df[delay_cols].fillna(0)

    delay_totals = df[delay_cols].sum().sort_values(ascending=False)
    delay_percent = (delay_totals / delay_totals.sum()) * 100

    return delay_totals, delay_percent


def get_worst_airports(df: pd.DataFrame, top_n: int = 10) -> pd.Series:
    return (
        df.groupby("ORIGIN")["ARR_DEL15"]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
    )