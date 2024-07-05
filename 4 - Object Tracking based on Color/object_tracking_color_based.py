import cv2
import imutils

# define hsv lower and upper bound for the color of your choice
hsv_lower = (0, 129, 155)
hsv_upper = (30, 255, 240)

# initialize video capture
cap = cv2.VideoCapture(6)


while True:
    # read images from camera
    _, frame = cap.read()

    # resize the image
    img_resized = imutils.resize(frame, width=1000)

    # blur the image using Gaussian blur to smoothen the image
    gaussian_blur_img = cv2.GaussianBlur(img_resized, (11, 11), 0)

    # convert color to HSV
    hsv_image = cv2.cvtColor(gaussian_blur_img, cv2.COLOR_BGR2HSV)
