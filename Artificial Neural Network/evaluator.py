    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

    class Evaluator:
        def __init__(self, model):
            self.model = model

        def evaluate(self, X_test, y_test):
            y_pred = self.model.predict(X_test).flatten()  # ensure it's 1D
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            print(f"Mean Squared Error (MSE): {mse:.4f}")
            print(f"Mean Absolute Error (MAE): {mae:.4f}")
            print(f"R² Score: {r2:.4f}")