from keras.api.models import Sequential
from keras.api.layers import Conv2D
from keras.api.layers import MaxPooling2D
from keras.api.layers import Flatten
from keras.api.layers import Dense
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

# import tensorflow as tf

# Part 1 Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3),  activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])    
