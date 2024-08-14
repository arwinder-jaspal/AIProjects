import cv2, os
# start the camera capture
cap = cv2.VideoCapture(0)

while True:
    # read frame by frame
    _, frame = cap.read()
    
    # convert each frame to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display each frame
    cv2.imshow("Camera Grayscale", frame_grayscale)

    # terminate the window when 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


