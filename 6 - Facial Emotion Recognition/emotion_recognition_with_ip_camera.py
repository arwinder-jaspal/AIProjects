# import libraries
from facial_emotion_recognition import EmotionRecognition
import urllib.request
import cv2
import numpy as np
import imutils

# create an emotion recognition obj
er = EmotionRecognition(device='gpu')

# set the url for the ip camera
url = '192.168.1.35/shot.jpg'

while True:
    # Open camera url and get image from it
    image_path = urllib.request.urlopen(url)
    image_array = np.array(bytearray(image_path.read()), dtype=np.uint8)
    frame = cv2.imdecode(image_array, -1)

    # recognize emotion in the image and return results in BGR format
    frame = er.recognise_emotion(frame, return_type='BGR')

    # resize the image
    frame = imutils.resize(width=450)

    # display image
    cv2.imshow("Emotion", frame)

    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()
