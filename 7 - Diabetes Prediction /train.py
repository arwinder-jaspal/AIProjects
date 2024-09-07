# Hack to use CPU instead of GPU if using NVIDIA GPU
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''

from numpy import loadtxt
from keras.api.models import Sequential
from keras.api.layers import Dense, Input

# import tensorflow as tf
# tf.config.list_physical_devices('GPU')

# print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
# load the dataset
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')

# split into input (X) and output (y) variables
X = dataset[:, 0:8]
y = dataset[:, 8]

# create model
model = Sequential()
# deprecated
# model.add(Dense(12, input_dim=8, activation='relu')) # hidden layer
model.add(Input(shape=(8,)))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu')) # hidden layer
model.add(Dense(1, activation='sigmoid')) # output layer

# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=150, batch_size=10)

# evaluate the model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

# Save model
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# Save weights
model.save_weights("model.weights.h5")
print("Saved model to disk")