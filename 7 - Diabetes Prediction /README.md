# Diabetes Prediction

## Diabetes Prediction Dataset

This dataset is designed for predicting the onset of diabetes based on various physiological and demographic characteristics. It consists of 9 features and 1 label column, providing a comprehensive view of factors that may influence diabetes risk.

### Features
The dataset includes the following features:

1. **Number of Times Pregnant**  
   - Description: The total number of times the patient has been pregnant.

2. **Plasma Glucose Concentration**  
   - Description: The patient's plasma glucose concentration measured after a 2-hour oral glucose tolerance test.

3. **Diastolic Blood Pressure**  
   - Description: The patient's diastolic blood pressure recorded in mm Hg.

4. **Triceps Skin Fold Thickness**  
   - Description: The thickness of the patient's triceps skin fold measured in mm.

5. **2-Hour Serum Insulin**  
   - Description: The patient's serum insulin level measured 2 hours after glucose intake, expressed in mu U/ml.

6. **Body Mass Index (BMI)**  
   - Description: The patient's body mass index, calculated as weight in kg divided by height in m².

7. **Diabetes Pedigree Function**  
   - Description: A function that accounts for the patient's family history of diabetes, indicating genetic predisposition.

8. **Age**  
   - Description: The patient's age in years.

### Label
The label column (Column 10) indicates the presence or absence of diabetes in the patient:
- **1**: Patient has diabetes
- **0**: Patient does not have diabetes

## Code Explanation - Training

### Overview
This Python script implements a neural network model using Keras to predict the onset of diabetes based on the Pima Indians Diabetes dataset. The model is designed to run on a CPU, even if an NVIDIA GPU is available, by setting the appropriate environment variable.

### Requirements
- Python 3.10.12
- NumPy
- Keras
- TensorFlow (as the backend for Keras)
### 1. Environment Setup
The script begins by configuring the environment to ensure that the model runs on the CPU:
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
```

### 2. Data Loading
The dataset is loaded from a CSV file using NumPy's `loadtxt` function:
```python
from numpy import loadtxt
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
```
This function reads the data from the specified CSV file, where values are separated by commas.

### 3. Data Preparation
The dataset is split into input features (X) and output labels (y). The first 70% of the data is used for training:
```python
train_size = int(len(dataset) * 0.7)
dataset = dataset[:train_size]
X = dataset[:, 0:8]
y = dataset[:, 8]
```

### 4. Model Creation
A Sequential model is created with the following architecture:
- Input layer with 8 features
- Two hidden layers with ReLU activation
- Output layer with sigmoid activation for binary classification
```python
from keras.api.models import Sequential
from keras.api.layers import Dense, Input

model = Sequential()
model.add(Input(shape=(8,)))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

### 5. Model Compilation
The model is compiled with binary cross-entropy loss and the Adam optimizer:
```python
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

### 6. Model Training
The model is trained for 150 epochs with a batch size of 10:
```python
model.fit(X, y, epochs=150, batch_size=10)
```

### 7. Model Evaluation
The accuracy of the model is evaluated on the training data:
```python
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
```

### 8. Model Saving
The model architecture and weights are saved to disk for future use:
```python
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.weights.h5")
print("Saved model to disk")
```

## Code Explanation - Testing

### Overview
This Python script is designed to load a pre-trained neural network model for predicting diabetes based on the Pima Indians Diabetes dataset. The script uses the last 30% of the dataset for testing the model's performance, allowing for comparison between actual and predicted outcomes.

### Requirements
- Python 3.10.12
- NumPy
- Keras
- TensorFlow (as the backend for Keras)

### Code Explanation

### 1. Environment Setup
The script begins by ensuring that the model runs on the CPU, even if an NVIDIA GPU is available:
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
```

### 2. Data Loading
The dataset is loaded from a CSV file using NumPy's `loadtxt` function:
```python
from numpy import loadtxt
dataset = loadtxt('pima-indians-diabetes.csv', delimiter=',')
```
This function reads the data from the specified CSV file, where values are separated by commas.

### 3. Data Preparation
The dataset is split into input features (X) and output labels (y). The last 30% of the data is used for testing:
```python
test_size = int(len(dataset) * 0.3)
dataset = dataset[:-test_size]
X = dataset[:, 0:8]
y = dataset[:, 8]
```

### 4. Model Loading
The pre-trained model architecture is loaded from a JSON file:
```python
from keras.api.models import model_from_json

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
```

### 5. Weights Loading
The weights of the model are loaded from a file:
```python
model.load_weights("model.weights.h5")
print("Loaded model from disk")
```

### 6. Prediction
The model is used to make predictions on the input data (X):
```python
y_pred = model.predict(X)
```

### 7. Comparison of Actual vs. Predicted
The script compares the actual labels with the predicted values and prints the results:
```python
for i in range(len(y_pred)):
    print("Actual: %s. Predicted: %s" % (int(y[i]), round(y_pred[i][0])))
```
