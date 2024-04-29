# import opencv library
import cv2

# open an image
img = cv2.imread("test_image.jpg")

# convert from BGR to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show image in a named window
cv2.imshow("Original", img)
# show grayscale in a new named window
cv2.imshow("Grayscale", img_gray)

# create a new image for the grayscale image in png
cv2.imwrite("test_image_gray.png", img_gray)

cv2.waitKey(5000)
cv2.destroyAllWindows()

# check img shape
print(img.shape)  # returns image height, width and depth as a tuple

print(img.size)  # returns total number of element in the image array (ie height * width * depth
