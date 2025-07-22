# config.py

EPOCHS = 50
BATCH_SIZE = 32
LEARNING_RATE = 0.001
HIDDEN_UNITS = [64, 32]
INPUT_SHAPE = (30,)  # Example for 30 features
OUTPUT_UNITS = 1     # Binary classification
ACTIVATION = 'relu'
OUTPUT_ACTIVATION = 'sigmoid'
LOSS = 'binary_crossentropy'
METRICS = ['accuracy']
