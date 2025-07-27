class Config:
    INPUT_DIM = 4
    HIDDEN_UNITS = [64, 32]
    OUTPUT_DIM = 1
    ACTIVATION = 'relu'
    OUTPUT_ACTIVATION = 'sigmoid'
    LOSS = 'mean_squared_error'
    METRICS = ['mae']
    EPOCHS = 20
    BATCH_SIZE = 32
