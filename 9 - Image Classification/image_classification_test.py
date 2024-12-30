from keras.api.models import model_from_json
from keras.api.preprocessing import image
import numpy as np
import os

# load model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)
model.load_weights("model.weights.h5")
print("Loaded model from disk")



