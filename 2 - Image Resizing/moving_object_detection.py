# import necessary library
import cv2
import imutils

# open camera capture
cap = cv2.VideoCapture(0)

first_frame = None

while True:
    ret, frame = cap.read()
    # resize frame
    frame = imutils.resize(frame, 1000)
    # convert image to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # apply gaussian blur to smoothen image
    gaussian_blur_img = cv2.GaussianBlur(frame_gray, (21, 21),0)

    # if the first frame is not assigned, assign the gaussian blurred image
    if first_frame is None:
        first_frame = gaussian_blur_img
        continue

    # calculate absolute difference between first frame and current frame
    # this will show only the difference in the image
    image_diff = cv2.absdiff(first_frame, gaussian_blur_img)

    # apply binary thresholding to the difference
    # we apply thresholding on the different to highlight the difference so that it easier to draw a bounding box
    _, threshold_img = cv2.threshold(image_diff, 180, 255, cv2.THRESH_BINARY)

    # apply dilation to fill up the images after binary threshold
    dilated_img = cv2.dilate(threshold_img, None, iterations=2)

    # find contours of the dilated image
    contour = cv2.findContours(dilated_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # display camera feed
    cv2.imshow("Live Feed", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()