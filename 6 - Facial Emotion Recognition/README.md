# README for Facial Emotion Recognition Python Script

## Webcam
### Overview
This Python script employs the `facial_emotion_recognition` library to perform real-time facial emotion recognition using a webcam feed. It captures video frames, processes them to detect emotions, and displays the results in a window.

### Features
- Real-time emotion recognition from video feed.
- Supports GPU acceleration for improved performance (if available).
- Displays the recognized emotion on the captured video frames.

### Requirements
To run this script, ensure you have the following installed:
- Python 3.x
- OpenCV
- facial_emotion_recognition

You can install the required libraries using pip:

```bash
pip install opencv-python facial-emotion-recognition
```

### Usage
1. **Initialize Emotion Recognition**: The script initializes the `EmotionRecognition` class. You can set the `device` parameter to `'gpu'` for GPU acceleration or `'cpu'` for CPU processing.
   - Example:
     ```python
     er = EmotionRecognition(device='gpu')
     ```

2. **Run the Script**: Execute the script in your terminal or command prompt:
   ```bash
   python emotion_recognition.py
   ```

3. **Interact with the Output**:
   - A window will open displaying the webcam feed with recognized emotions annotated on the frames.
   - The recognized emotion will be displayed on the video feed in real-time.

4. **Exit the Program**: Press the 'q' key to quit the application.

### Code Explanation
- **Emotion Recognition Initialization**: The script initializes the emotion recognition model, specifying the device for processing (GPU or CPU).
- **Video Capture**: Captures video from the default camera.
- **Emotion Recognition**: Each frame is processed to recognize emotions using the `recognise_emotion` method of the `EmotionRecognition` class.
- **Display Output**: The processed frame with recognized emotions is displayed in a window.
- **Exit Mechanism**: The application listens for the 'q' key to terminate the loop and release resources.

### Troubleshooting
- **Camera Not Detected**: Ensure your webcam is connected and not being used by another application.
- **No Emotion Recognition**: Make sure your face is clearly visible in the camera frame. Adjust lighting conditions if necessary.
- **Performance Issues**: If using a CPU, consider switching to a GPU for better performance, or reduce the resolution of the captured frame.

## IP Camera
### Overview
This Python script utilizes the `facial_emotion_recognition` library to perform real-time facial emotion recognition from an IP camera feed. It captures images from the specified IP camera URL, processes them to detect emotions, and displays the results in a window.

### Features
- Real-time emotion recognition from an IP camera.
- Supports GPU acceleration for improved performance (if available).
- Displays recognized emotions on the captured video frames.
- Resizes the output frames for better visibility.

### Requirements
To run this script, ensure you have the following installed:
- Python 3.x
- OpenCV
- NumPy
- imutils
- facial_emotion_recognition

You can install the required libraries using pip:

```bash
pip install opencv-python numpy imutils facial-emotion-recognition
```

### Usage
1. **Set the IP Camera URL**: Modify the `url` variable to point to your IP camera's JPEG snapshot URL.
   - Example:
     ```python
     url = 'http://192.168.1.35/shot.jpg'
     ```

2. **Initialize Emotion Recognition**: The script initializes the `EmotionRecognition` class. You can set the `device` parameter to `'gpu'` for GPU acceleration or `'cpu'` for CPU processing.
   - Example:
     ```python
     er = EmotionRecognition(device='gpu')
     ```

3. **Run the Script**: Execute the script in your terminal or command prompt:
   ```bash
   python emotion_recognition_with_ip_camera.py
   ```

4. **Interact with the Output**:
   - A window will open displaying the images captured from the IP camera with recognized emotions annotated on the frames.
   - The recognized emotion will be displayed in real-time.

5. **Exit the Program**: Press the 'q' key to quit the application.

### Code Explanation
- **Library Imports**: The script imports necessary libraries for emotion recognition, image processing, and handling HTTP requests.
- **Emotion Recognition Initialization**: Initializes the emotion recognition model, specifying the device for processing (GPU or CPU).
- **Image Capture from IP Camera**:
  - Opens the specified URL to capture images from the IP camera.
  - Converts the image data into a format suitable for OpenCV processing.
- **Emotion Recognition**: Each captured frame is processed to recognize emotions using the `recognise_emotion` method of the `EmotionRecognition` class.
- **Image Resizing**: The frame is resized for better display.
- **Display Output**: The processed frame with recognized emotions is displayed in a window.
- **Exit Mechanism**: The application listens for the 'q' key to terminate the loop and release resources.

### Troubleshooting
- **Camera Connection Issues**: Ensure that the IP camera is connected to the network and the URL is correct. You can test the URL in a web browser to see if it returns an image.
- **No Emotion Recognition**: Make sure faces are clearly visible in the camera feed. Adjust lighting conditions if necessary.
- **Performance Issues**: If using a CPU, consider switching to a GPU for better performance.
sed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- OpenCV for computer vision capabilities.
- NumPy for numerical operations.
- `facial_emotion_recognition` library for emotion detection.
- imutils for simplifying image processing tasks.

Feel free to modify and enhance the code for your specific needs!