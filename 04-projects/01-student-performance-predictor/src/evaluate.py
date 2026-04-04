"""Evaluation utilities for the student performance project."""
from sklearn.metrics import r2_score


def evaluate_model(model, x_test, y_test):
    """Compute the R2 score on the test split."""
    y_pred = model.predict(x_test)
    return r2_score(y_test, y_pred)
