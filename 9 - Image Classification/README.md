# CNN Image Classifier

A convolutional neural network (CNN) built with Keras for binary image classification.

## Overview

This project implements a simple CNN architecture for classifying images into two categories. The network consists of:
- A convolutional layer with ReLU activation
- Max pooling layer
- Flattening layer
- Two fully connected (dense) layers
- Binary classification output with sigmoid activation

## Requirements

- Python 3.12
- Keras
- TensorFlow
- Required Python packages can be installed via:
```bash
pip install keras tensorflow
```

## Dataset Structure

The code expects the following dataset structure:
```
your_directory/
├── model.json
├── model.weights.h5
├── image_classification_train.py
├── image_classification_test.py
└── dataset/
    ├── train/
    │   ├── class1/
    │   │   └── (training images)
    │   └── class2/
    │       └── (training images)
    └── val/
    │   ├── class1/
    │   │   └── (validation images)
    │   └── class2/
    │       └── (validation images)
    └── test/
            └── (images to classify)
```

## Model Architecture

The CNN architecture consists of:
1. Conv2D layer (32 filters, 3x3 kernel, ReLU activation)
2. MaxPooling2D layer (2x2 pool size)
3. Flatten layer
4. Dense layer (128 units, ReLU activation)
5. Output layer (1 unit, sigmoid activation)

## Training

The model is trained with:
- Adam optimizer
- Binary crossentropy loss
- Batch size of 8
- 50 epochs
- Data augmentation (shear, zoom, horizontal flip) for training set
- Input images are resized to 64x64 pixels

### Data Augmentation

Training data is augmented with:
- Rescaling (1/255)
- Random shear (range: 0.2)
- Random zoom (range: 0.2)
- Random horizontal flips

Validation data is only rescaled (1/255).

### Model Saving

After training, the model is saved in two formats:
- Weights file: `model.weights.h5`
- Architecture file: `model.json`

### Usage

1. Prepare your dataset following the structure above
2. Run the script:
```bash
python image_classification_train.py
```

The trained model will be saved in the current directory.

## Testing

The script:
1. Loads the pre-trained model from JSON and weights files
2. Processes each image in the test directory:
   - Resizes image to 64x64 pixels
   - Converts to array format
   - Makes prediction using the loaded model
3. Outputs the classification result for each image:
   - Thanos (if result = 1)
   - Joker (if result = 0)

### Usage

1. Ensure you have the trained model files (`model.json` and `model.weights.h5`) in the same directory as the script
2. Place the images you want to classify in the `dataset/test/` directory
3. Run the script:
```bash
python image_classification_test.py
```

### Output Format

For each image, the script prints:
```
Predicted [image_path] as [Thanos/Joker]
```

## Notes

- Images are automatically resized to 64x64 pixels to match the model's input requirements
- The script processes all files in the test directory
- Make sure your test images are in a supported format (e.g., JPEG, PNG)

## Demo

![Demo](docs/demo.mp4)