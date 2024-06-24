import cv2

# loading haarcascade algorithm
algo = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(algo)

# initialize camera
cap = cv2. VideoCapture(0)

while True:
    break

cap.release()
cv2.destroyAllWindows()