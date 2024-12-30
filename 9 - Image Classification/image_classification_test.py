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

def classify_image(image_path):
    img = image.load_img(image_path, target_size=(64, 64))
    test_img = image.img_to_array(img)
    test_img = np.expand_dims(test_img, axis=0)
    result = model.predict(test_img)

    if result[0][0] == 1:
        prediction = "Thanos"
    else:
        prediction = "Joker"

    print("Predicted ", image_path, " as ", prediction, '\n')

path = os.path.dirname(os.path.abspath(__file__)) + "/dataset/test/"

for file in os.listdir(path):
    classify_image(path + file)

