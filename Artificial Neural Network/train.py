# train.py

def train_model(model, X_train, y_train, X_val, y_val, epochs, batch_size):
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1
    )
    return history
