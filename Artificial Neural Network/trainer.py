class ModelTrainer:
    def __init__(self, model, config):
        self.model = model
        self.config = config

    def train(self, X_train, y_train, X_val, y_val):
        history = self.model.fit(X_train, y_train, epochs=self.config.EPOCHS, batch_size=self.config.BATCH_SIZE,
            validation_data=(X_val, y_val), verbose=1)
        return history
