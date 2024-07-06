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

    # Detect the object based on HSV Range Values
    mask = cv2.inRange(hsv_image, hsv_lower, hsv_upper)

    # Erode away the boundaries of the foreground object, diminish the features of image
    # It is useful for removing small white noises, detach two connected object
    mask = cv2.erode(mask, None, iterations=2)

    # Dilation
    # increases the object area, used to accentuate feature
    # In cases like noise removal, erosion is followed by dilation.
    # Because, erosion removes white noises, but it also shrinks our object.
    # So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    # It is also useful in joining broken parts of an object.
    mask = cv2.dilate(mask, None, iterations=2)