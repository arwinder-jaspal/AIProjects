# import necessary library
import cv2
import imutils

# open camera capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # resize frame
    frame = imutils.resize(1000)
    # convert image to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply gaussian blur to smoothen image
    gaussian_blur_img = cv2.GaussianBlur(frame_gray, (21, 21),0)

    # display camera feed
    cv2.imshow("Live Feed", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()