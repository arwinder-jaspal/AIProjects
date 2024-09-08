import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''

from numpy import loadtxt
from keras.api.models import model_from_json

# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# split into input (X) and output (y) variables
# only use last 30% of data for test
test_size = int(len(dataset) * 0.3)
dataset = dataset[:-test_size]
X = dataset[:, 0:8]
y = dataset[:, 8]

# load model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load weights
model.load_weights("model.weights.h5")
print("Loaded model from disk")

#predict
y_pred = model.predict(X)
# compare actual vs prediction
for i in range(len(y_pred)):
    print("Actual: %s. Predicted: %s" % (int(y[i]), round(y_pred[i][0])))