from unicodedata import category

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LINE_WIDTH = 68


def page_title(title):
    print("\n" + "=" * LINE_WIDTH)
    print(title.upper().center(LINE_WIDTH))
    print("=" * LINE_WIDTH)


def section(title):
    print(f"\n[ {title} ]")
    print("-" * LINE_WIDTH)


# Matplotlib topics:
# - Drawing multiple lines on the same plot
# - Customizing markers with a shared style dict
# - Titles, axis labels, tick positions, and grid
def line_chart_section():
    section("1. Line Chart")

    line_style = dict(
        marker=".",
        markerfacecolor="#171240",
        markersize=10,
        markeredgecolor="#171240",
    )
    x = np.array([2023, 2024, 2025, 2026])
    y1 = np.array([15, 25, 30, 20])
    y2 = np.array([27, 23, 40, 23])
    y3 = np.array([47, 35, 40, 5])

    plt.title("Matplotlib first graphique", fontsize=15, family="SF Mono",
              fontweight="bold")
    plt.xlabel("x", fontsize=15)
    plt.ylabel("y", fontsize=15)
    plt.xticks(x)
    plt.plot(x, y1, color="#52e625", **line_style)
    plt.plot(x, y2, color="#8f33bd", **line_style)
    plt.plot(x, y3, color="#44ebe8", **line_style)
    plt.grid(True, linestyle="dashdot")
    # plt.savefig("figures/line_chart.png")
    print("→ figures/line_chart.png")
    plt.show()


# Matplotlib topics:
# - Drawing a vertical bar chart
# - Using categorical labels on the x-axis
def bar_chart_section():
    section("2. Bar Chart")

    category_1 = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
    values = np.array([4, 3, 2, 10, 3, 2])

    plt.bar(category_1, values, color="#72f27f")
    plt.title("Daily Consumption")
    plt.xlabel("Category")
    plt.ylabel("Value")
    # plt.savefig("figures/bar_chart.png")
    print("→ figures/bar_chart.png")
    plt.show()


def pie_chart_section():
    section("3. Pie Chart")

    category_1 = ["Work", "Sleep", "Sport", "Family", "Hobbies"]
    time = np.array(["8", "8", "2", "2", "4"])

    plt.pie(time, labels=category_1,
            autopct="%1.1f%%",
            explode=[0.1, 0.1, 0, 0, 0],
            shadow=False,
            startangle=90)
    plt.title("Day Time")
    # plt.savefig("figures/pie_chart.png")
    print("→ figures/pie_chart.png")
    plt.show()

def scatter_section():
    section("4. Scatter Chart")

    x = np.array([1, 2, 3, 4, 5, 8])
    y = np.array([10, 13, 23, 37, 50, 60])

    x1 = np.array([1, 3, 4, 6, 8, 10])
    y1 = np.array([11, 12, 23, 24, 37, 45])

    plt.scatter(x, y, s = 100, label="Class A")
    plt.scatter(x1, y1, c="red",
                s = 100,
                label="Class B"
                )
    plt.xlabel("Hours Studied")
    plt.ylabel("Grade")
    plt.legend(loc="upper left")
    plt.title("Scatter Chart")
    # plt.savefig("figures/scatter_chart.png")
    print("→ figures/scatter_chart.png")
    plt.show()

def histogram_section():
    section("5. Histogram Chart")
    scores = np.random.normal(loc=70, scale=10, size=100)
    scores = np.clip(scores, a_min=0, a_max=100)
    plt.hist(scores, bins=15,
             color="#ebcae2",
             edgecolor="#f08bd6")
    plt.xlabel("Score")
    plt.ylabel("# of students")
    plt.title("Histogram Chart")
    # plt.savefig("figures/histogram_chart.png")
    print("→ figures/histogram_chart.png")
    plt.show()

def figure_and_axes_section():
    section("6. Figure and Axes Chart")

    x = np.array([1, 4, 23, 33, 45])

    figure , axes = plt.subplots(2, 3)

    axes[0, 0].plot(x, x*2, color="red")
    axes[0, 0].set_title("First Axes")
    axes[0, 1].plot(x, x / 3, color="blue")
    axes[0, 1].set_title("Second Axes")
    axes[0, 2].plot(x, x**4, color="green")
    axes[0, 2].set_title("Third Axes")
    axes[1, 0].plot(x, x % 5, color="yellow")
    axes[1, 0].set_title("Fourth Axes")
    axes[1, 1].plot(x, x*6, color="orange")
    axes[1, 1].set_title("Fifth Axes")
    axes[1, 2].plot(x, x**7, color="purple")
    axes[1, 2].set_title("Sixth Axes")
    plt.tight_layout()
    # plt.savefig("figures/figure_and_axes.png")
    print("→ figures/figure_and_axes.png")
    plt.show()
def csv_chart_section():
    section("7. Csv Chart")

    df = pd.read_csv("data/pokemon.csv")

    type_count = df["Type 1"].value_counts(ascending=True)

    plt.barh(type_count.index, type_count, color="lightblue",
             edgecolor="darkgreen")
    plt.title("# of Pokemon by Primary Type")
    plt.xlabel("Primary Type Count")
    plt.ylabel("Type")
    plt.tight_layout()
    # plt.savefig("figures/csv_chart.png")
    print("→ figures/csv_chart.png")
    plt.show()

def main():
    page_title("My Matplotlib Journal")
    line_chart_section()
    bar_chart_section()
    pie_chart_section()
    scatter_section()
    histogram_section()
    figure_and_axes_section()
    csv_chart_section()
if __name__ == "__main__":
    main()
