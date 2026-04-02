# -------------------------------
# flight_delay_analysis.py
# -------------------------------

import os
import seaborn as sns

# -------------------------------
# Config
# -------------------------------
DATA_PATH = "./data/flight_data.csv"
OUT_VIS = "visuals"
os.makedirs(OUT_VIS, exist_ok=True)
sns.set_theme(style="whitegrid")


from src.data_loader import load_data
from src.preprocessing import clean_data
from src.analysis import (
    compute_delay_stats,
    compute_airline_delay,
    compute_delay_by_day,
    get_best_worst_days,
    get_root_cause_analysis,
    get_worst_airports
)
from src.visualization import (
    plot_airline_delay,
    plot_delay_by_day,
    plot_delay_causes,
    plot_worst_airports
)


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

    'Key insight'
    max_day, min_day = get_best_worst_days(delay_by_day)

    day_map = {
        1: "Monday", 2: "Tuesday", 3: "Wednesday",
        4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
    }

    print("\n--- Key Insight ---")
    print(f"Flights are most delayed on {day_map[max_day]} and least delayed on {day_map[min_day]}.")

    delay_totals, delay_percent = get_root_cause_analysis(df)
    cause_map = {
        "CARRIER_DELAY": "Airline Issues",
        "WEATHER_DELAY": "Weather",
        "NAS_DELAY": "Air System",
        "SECURITY_DELAY": "Security",
        "LATE_AIRCRAFT_DELAY": "Late Aircraft"
    }

    delay_percent.index = delay_percent.index.map(cause_map)

    print("\n--- Total Delay by Cause ---")
    print(delay_totals)

    print("\n--- Delay Cause Distribution (%) ---")
    print(delay_percent)

    top_cause = delay_percent.idxmax()

    print("\n--- Key Insight ---")
    print(f"The primary cause of delays is {top_cause}.")

    airport_delay = get_worst_airports(df)

    plot_path_airports = os.path.join(OUT_VIS, "worst_airports.png")
    plot_worst_airports(airport_delay, plot_path_airports)
    worst_airport = airport_delay.idxmax()

    print("\n--- Key Insight ---")
    print(f"{worst_airport} has the highest delay rate among analyzed airports.")

if __name__ == "__main__":
    main()