"""Data loading utilities for the student performance project."""
from pathlib import Path

import pandas as pd


def load_data():
    """Load the dataset stored in the project data folder."""
    data_path = Path(__file__).resolve().parent.parent / "data" / "StudentPerformanceFactors.csv"
    df = pd.read_csv(data_path)
    return df
