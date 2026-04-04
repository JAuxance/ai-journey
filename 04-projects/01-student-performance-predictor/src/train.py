"""Training entry point for the student performance project."""
from sklearn.linear_model import LinearRegression


def train_model(x_train, y_train):
    """Train the baseline linear regression model."""
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model
