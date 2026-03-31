import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter
import numpy as np

LINE_WIDTH = 68


def page_title(title):
    print("\n" + "=" * LINE_WIDTH)
    print(title.upper().center(LINE_WIDTH))
    print("=" * LINE_WIDTH)


def section(title):
    print(f"\n[ {title} ]")
    print("-" * LINE_WIDTH)

if __name__ == "__main__":
    page_title("Matplotlib Journal")

    plt.plot([1, 3, 2], [5, 4, 3])
    plt.show()