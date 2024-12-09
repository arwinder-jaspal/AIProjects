# Real-Time Object Detection with MobileNet SSD

This Python script performs real-time object detection using a pre-trained MobileNet SSD (Single Shot Detector) model. It captures video from your webcam, processes each frame to identify objects, and displays bounding boxes around detected items along with their class labels and confidence scores.

## Features

- **Real-Time Detection**: Processes video frames in real time.
- **Multiple Classes**: Detects a variety of objects, including vehicles, animals, and everyday items.
- **Interactive Display**: Shows bounding boxes and labels on detected objects in the video feed.
- **Customizable Confidence Threshold**: Adjusts the sensitivity of detections.

## Requirements

To run this script, you will need:

- Python 3.x
- OpenCV
- NumPy
- imutils

You can install the required packages using pip and the requirement.txt from root folder:

```bash
pip install -r requirements.txt
```

## Getting Started

### 1. Download Pre-trained Model Files

You need to download the MobileNet SSD model files. These files are based on the Caffe framework and include the model architecture and weights. You can find them at:

- [MobileNetSSD_deploy.caffemodel](https://github.com/chuanqi305/MobileNet-SSD/blob/master/MobileNetSSD_deploy.caffemodel)
- [MobileNetSSD_deploy.prototxt.txt](https://github.com/chuanqi305/MobileNet-SSD/blob/master/MobileNetSSD_deploy.prototxt)

Place these files in the same directory as your script.

### 2. Run the Script

Ensure your webcam is connected and run the script:

```bash
python object_detection_using_caffe_model.py
```

### 3. Usage Instructions

Once the script is running, it will open a window displaying the video feed from your webcam. Detected objects will have bounding boxes drawn around them, and their class names along with confidence percentages will be displayed. To exit the application, press `q`.

## Code Overview

1. **Imports Libraries**: The script imports necessary libraries for image processing and computer vision.
2. **Sets Up Classes and Colors**: Defines a list of object classes and generates random colors for bounding boxes.
3. **Loads the Pre-trained Model**: Loads the pre-trained MobileNet SSD model using OpenCV's DNN module, specifically designed for use with Caffe models.
4. **Initializes Video Stream**: Captures video from the webcam and allows time for the camera to warm up.
5. **Processes Each Frame**:
   - Resizes frames for processing.
   - Converts frames into a blob format suitable for input into the neural network.
   - Runs forward propagation to get detections.
   - Filters out weak detections based on a confidence threshold.
   - Draws bounding boxes and labels on detected objects.
6. **Displays Output**: Shows the processed frame in a window until `q` is pressed.

## Example Output

<!--  TODO: Replace with an actual image link if available -->
