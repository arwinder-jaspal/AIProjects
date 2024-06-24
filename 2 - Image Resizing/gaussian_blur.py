# import necessary libraries
import cv2

# read an image
img = cv2.imread("../stock_images/resized_img.jpg")

# apply gaussian blur to reduce noise which can cause inaccuracy
gaussian_img = cv2.GaussianBlur(img, (41, 41), 50)
gaussian_img_mild = cv2.GaussianBlur(img, (21, 21), 0)

cv2.imshow("Original", img)
cv2.imshow("Strong Gaussian Blur", gaussian_img)
cv2.imshow("Mild Gaussian Blur", gaussian_img_mild)

cv2.waitKey(5000)
cv2.destroyAllWindows()





