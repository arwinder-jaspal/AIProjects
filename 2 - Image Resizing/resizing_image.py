# import necessary libraries
import cv2
import imutils

img = cv2.imread("../stock_images/pexels-joerg-hartmann-626385254-17815054.jpg")

# resize the image to maintain the ascpect ration and have a width of 100 px
resized_img = imutils.resize(img, width=100)

# display the image
cv2.imshow("Original", img)
cv2.imshow("Resized Image", resized_img)

# print the size of the images
print("Original Image Size: ", img.shape)
print("Resized Image Size: ", resized_img.shape)

# write the image to a file
cv2.imwrite("resized_img.jpg", resized_img)

cv2.waitKey(5000)
cv2.destroyAllWindows()