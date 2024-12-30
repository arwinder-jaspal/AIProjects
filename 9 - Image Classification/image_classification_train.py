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

# Part 2 - Fitting the CNN to the images
train_datagen = ImageDataGenerator(rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True)

validation_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/train',
                  target_size = (64, 64),
                  batch_size = 8,
                  class_mode = 'binary')
print(validation_datagen)
validation_datagen_set = validation_datagen.flow_from_directory('dataset/val',
             target_size = (64, 64),
             batch_size = 8,
             class_mode = 'binary')

classifier.fit(training_set,
    steps_per_epoch = 100,
    epochs = 50,
    validation_data = validation_datagen_set,
    validation_steps = 2)

# save model as h5 and json
print("Saving Model")
classifier.save_weights('model.weights.h5')
model_json = classifier.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
