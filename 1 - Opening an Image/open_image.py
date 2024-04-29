# import opencv library
import cv2

# read an image
img = cv2.imread("test_image.jpg")

# show the image
cv2.imshow('Image', img)

# convert the image to a png
cv2.imwrite("test_image.png", img)

# Keep the image window open for 5000 ms
cv2.waitKey(5000)
cv2.destroyAllWindows()
