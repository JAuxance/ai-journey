from unicodedata import category

import matplotlib.pyplot as plt
import numpy as np


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
    plt.show()

def pie_section():
    section("4. Pie Chart")


def main():
    page_title("My Matplotlib Journal")
    # line_chart_section()
    # bar_chart_section()
    pie_chart_section()


if __name__ == "__main__":
    main()
