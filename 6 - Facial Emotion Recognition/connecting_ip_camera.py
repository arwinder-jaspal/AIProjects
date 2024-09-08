# import libraries
import urllib.request #library to get information from the internet
import cv2
import numpy as np
import imutils

# set the ip of camera the camera
url = "http://192.168.1.33:8080/shot.jpg"

while True:
    # get an image from the camera
    image_path = urllib.request.urlopen(url)
    # convert image data to a numpy array
    image_array = np.array(bytearray(image_path.read()), dtype=np.uint8)
    # convert image data into a picture we can display
    frame = cv2.imdecode(image_array, -1)

    # resize the image
    frame = imutils.resize(frame, 450)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()