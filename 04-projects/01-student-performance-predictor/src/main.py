from data import load_data
from features import split_data
from features import prepare_features
from train import train_model
from evaluate import evaluate_model


def main():
    """Run the full pipeline from data loading to evaluation."""
    df = load_data()
    x, y = prepare_features(df)
    x_train, x_test, y_train, y_test = split_data(x, y)

    model = train_model(x_train, y_train)
    score = evaluate_model(model, x_test, y_test)
    print(f"R2 score: {score:.4f}")


if __name__ == "__main__":
    main()
