# main.py

from data_loader import load_data
from preprocessing import scale_data
from model_builder import build_ann
from train import train_model
from evaluate import evaluate_model
from config import EPOCHS, BATCH_SIZE

def main():
    # Load and split the dataset
    X_train, X_test, y_train, y_test = load_data("data.csv")

    # Preprocess features
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)

    # Build model
    model = build_ann()

    # Train model
    train_model(model, X_train_scaled, y_train, X_test_scaled, y_test, EPOCHS, BATCH_SIZE)

    # Evaluate model
    evaluate_model(model, X_test_scaled, y_test)

if __name__ == "__main__":
    main()
