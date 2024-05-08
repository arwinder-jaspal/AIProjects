# import necessary library
import cv2

# open camera capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # convert image to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display camera feed
    cv2.imshow("Live Feed", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()