"""Feature engineering utilities for the student performance project."""
from typing import Any

import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split


def prepare_features(df) -> tuple[DataFrame, Any]:
    """Encode categorical columns and separate features from the target."""
    categorical_features = [
        "Parental_Involvement",
        "Access_to_Resources",
        "Extracurricular_Activities",
        "Motivation_Level",
        "Internet_Access",
        "Family_Income",
        "Teacher_Quality",
        "Peer_Influence",
        "Learning_Disabilities",
        "Parental_Education_Level",
        "Distance_from_Home",
        "Gender",
        "School_Type",
    ]

    # One-hot encode categorical variables before training.
    df = pd.get_dummies(df, columns=categorical_features)
    x = df.drop(columns=["Exam_Score"])
    y = df["Exam_Score"]
    return x, y


def split_data(x, y):
    """Split the dataset into train and test sets with a fixed random state."""
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test
