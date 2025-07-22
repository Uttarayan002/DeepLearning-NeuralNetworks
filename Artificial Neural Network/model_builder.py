# model_builder.py

import tensorflow as tf
from config import HIDDEN_UNITS, INPUT_SHAPE, OUTPUT_UNITS, ACTIVATION, OUTPUT_ACTIVATION, LEARNING_RATE, LOSS, METRICS

def build_ann():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=INPUT_SHAPE))

    for units in HIDDEN_UNITS:
        model.add(tf.keras.layers.Dense(units, activation=ACTIVATION))
    
    model.add(tf.keras.layers.Dense(OUTPUT_UNITS, activation=OUTPUT_ACTIVATION))
    
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
                  loss=LOSS,
                  metrics=METRICS)
    return model
