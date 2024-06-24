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

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
    cv2.imshow("FaceDetection", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()