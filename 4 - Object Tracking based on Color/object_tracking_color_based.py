import cv2
import imutils

# define hsv lower and upper bound for the color of your choice
hsv_lower = (0, 129, 155)
hsv_upper = (30, 255, 240)

# initialize video capture
cap = cv2.VideoCapture(0)


while True:
    # read images from camera
    _, frame = cap.read()

    # resize the image
    img_resized = imutils.resize(frame, width=1000)

    # blur the image using Gaussian blur to smoothen the image
    gaussian_blur_img = cv2.GaussianBlur(img_resized, (11, 11), 0)

    # convert color to HSV
    hsv_image = cv2.cvtColor(gaussian_blur_img, cv2.COLOR_BGR2HSV)

    # Detect the object based on HSV Range Values
    mask = cv2.inRange(hsv_image, hsv_lower, hsv_upper)

    # Erode away the boundaries of the foreground object, diminish the features of image
    # It is useful for removing small white noises, detach two connected object
    mask = cv2.erode(mask, None, iterations=2)

    # Dilation
    # increases the object area, used to accentuate feature
    # In cases like noise removal, erosion is followed by dilation.
    # Because, erosion removes white noises, but it also shrinks our object.
    # So we dilate it. Since noise is gone, they won’t come back, but our object area increases.
    # It is also useful in joining broken parts of an object.
    mask = cv2.dilate(mask, None, iterations=2)

    # get contours of the mask
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]

    center = None

    if len(contours):
        # get the contour with largest area
        max_area_contour = max(contours, key=cv2.contourArea)
        # get the center and radius of min enclosing circle for the larger area contour
        ((x, y), radius) = cv2.minEnclosingCircle(max_area_contour)
        # calculate image moment
        image_moment = cv2.moments(max_area_contour)
        # get centroid of the detect max_area_contour
        # The central moment m10 represents the x-coordinate of the centroid,
        # and m01 represents the y-coordinate of the centroid.
        centroid = (int(image_moment["m10"] / image_moment["m00"]),
                    int(image_moment["m01"] / image_moment["m00"]))

        # if the radius exceed 10, we consider the color is reliably detected
        if radius > 10:
            # draw a yellow circle to enclose the object with the matching color
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255, 255), 2)
            # draw a red dot to highlight the centroid
            cv2.circle(frame, centroid, 5, (0, 0, 255, 2))

            # if the radius is too large, the object is too close
            if radius > 250:
                print("Stop Moving")
            else:
                # if the centroid is too far to the left
                if centroid[0] < 150:
                    print("Move Right")
                # if the centroid is too far to the right
                elif centroid[0] > 450:
                    print("Move Left")
                # if the object is not too near
                elif radius < 250:
                    print("Move Forward")

    cv2.imshow("Stream", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
