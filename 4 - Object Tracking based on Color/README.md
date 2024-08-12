# README for Color Detection Python Script

## Overview
This Python script utilizes OpenCV and imutils libraries to perform real-time color detection through a webcam feed. It identifies specific colors based on HSV (Hue, Saturation, Value) values, detects the largest contour of the detected color, and provides directional feedback based on the object's position relative to the center of the frame.

## Features
- Real-time color detection using a webcam.
- Adjustable HSV color range for detecting different colors.
- Visual feedback with contours and centroids drawn on detected objects.
- Console output for movement instructions based on the detected object's position.

## Requirements
To run this script, ensure you have the following installed:
- Python 3.x
- OpenCV
- imutils

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```

## Usage
1. **Set HSV Color Range**: Modify the `hsv_lower` and `hsv_upper` variables to set the desired color range for detection. 
   - This can be done using the `colorCalibrationHSV.py` script
    ```bash
    python colorCalibrationHSV.py
    ```
   - Example: 
   ```python
   hsv_lower = (0, 129, 155)  # Lower bound for the color
   hsv_upper = (30, 255, 240)  # Upper bound for the color
   ```

2. **Run the Script**: Execute the script in your terminal or command prompt:
   ```bash
   python object_tracking_color_based.py
   ```

3. **Interact with the Output**:
   - A window will open displaying the webcam feed.
   - The script will draw a yellow circle around detected objects and a red dot at their centroid.
   - Movement instructions will be printed to the console based on the detected object's position:
     - "Stop Moving" if the object is too close.
     - "Move Right" or "Move Left" based on the centroid's position.
     - "Move Forward" if the object is at a reasonable distance.

4. **Exit the Program**: Press the 'q' key to quit the application.

## Code Explanation
- **Video Capture**: The script initializes video capture from the default camera.
- **Image Processing**:
  - Resizes the frame for easier processing.
  - Applies Gaussian blur to reduce noise.
  - Converts the image to HSV color space for better color detection.
- **Masking**: Creates a binary mask to isolate the colors within the specified HSV range.
- **Morphological Operations**: Erosion and dilation are applied to refine the mask.
- **Contour Detection**: Finds contours in the mask and identifies the largest contour.
- **Centroid Calculation**: Calculates the centroid of the largest contour to determine its position in the frame.
- **Movement Feedback**: Provides feedback based on the position of the detected object.

## Troubleshooting
- **Camera Not Detected**: Ensure your webcam is connected and not being used by another application.
- **No Detection**: Adjust the HSV values to better match the color you want to detect.
- **Performance Issues**: Reduce the resolution of the captured frame by adjusting the `width` parameter in `imutils.resize()`.

## Acknowledgments
- OpenCV for computer vision capabilities.
- imutils for simplifying image processing tasks.

Feel free to modify and enhance the code for your specific needs!