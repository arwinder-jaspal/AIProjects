# import necessary library
import cv2

# start video capture from built-in camera
cap = cv2.VideoCapture(0)

# display video frame by frame

while True:
    ret, frame = cap.read()

    # display frames
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# stop video capture
cap.release()
cv2.destroyAllWindows()