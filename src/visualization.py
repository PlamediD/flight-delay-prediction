import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


def plot_airline_delay(airline_delay, out_path):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=airline_delay.index, y=airline_delay.values)
    plt.xticks(rotation=45)
    plt.title("Arrival Delay Rate by Airline")
    plt.xlabel("Airline")
    plt.ylabel("Delay Rate")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()


def plot_delay_by_day(delay_by_day, out_path):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=delay_by_day.index, y=delay_by_day.values)
    plt.xticks(ticks=range(7), labels=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    plt.title("Delay by Day of Week")
    plt.xlabel("Day")
    plt.ylabel("Delay Rate")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()


def plot_delay_causes(delay_percent, out_path):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=delay_percent.index, y=delay_percent.values)
    plt.xticks(rotation=30)
    plt.title("Delay Causes Distribution (%)")
    plt.xlabel("Cause")
    plt.ylabel("Percentage")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()


def plot_worst_airports(airport_delay, out_path):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=airport_delay.index, y=airport_delay.values)
    plt.xticks(rotation=45)
    plt.title("Top 10 Worst Airports by Delay Rate")
    plt.xlabel("Airport")
    plt.ylabel("Delay Rate")
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    plt.show()