import cv2

# loading haarcascade algorithm
algo = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(algo)

# initialize camera
cap = cv2. VideoCapture(0)

while True:
    # read image from caemra
    ret, frame = cap.read()

    # convert image to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # getting face coordinate
    face = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=4)


cap.release()
cv2.destroyAllWindows()