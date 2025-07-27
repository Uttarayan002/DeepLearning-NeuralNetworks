from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class ANNModel:
    def __init__(self, config):
         self.config = config

    def build_model(self):
         model = Sequential()
         model.add(Dense(self.config.HIDDEN_UNITS[0], activation = self.config.ACTIVATION, input_dim = self.config.INPUT_DIM))
         for units in self.config.HIDDEN_UNITS[1:]:
            model.add(Dense(units, activation=self.config.ACTIVATION))
         model.add(Dense(self.config.OUTPUT_DIM, activation = self.config.OUTPUT_ACTIVATION))
         model.compile(optimizer='adam', loss = self.config.LOSS,  metrics=self.config.METRICS)
         return model