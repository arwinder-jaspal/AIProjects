"""
 The function is typically used to get a bi-level (binary) image out of a grayscale image or for removing a noise,
 that is, filtering out pixels with too small or too large valuesThe first argument is the source image, which should
 be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. The third
 argument is the maximum value which is assigned to pixel values exceeding the threshold. OpenCV provides different
 types of thresholding which is given by the fourth parameter of the function
"""

import cv2

img = cv2.imread("../stock_images/resized_img.jpg",0)

# apply binary thresholding
threshold_img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)[1]

# display images
cv2.imshow("Grayscale", img)
cv2.imshow("Threshold Image", threshold_img)

cv2.waitKey(1000)
cv2.destroyAllWindows()