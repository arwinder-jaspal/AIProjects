import cv2, os

# specify xml for haarcascade
haar_file = 'haarcascade_frontalface_default.xml'

# create the path for dataset
dataset_dir = 'datasets'
sub_data_dir = 'arwinder'

dataset_dir_path = os.path.join(dataset_dir, sub_data_dir)
if not os.path.isdir(dataset_dir_path):
    os.mkdir(dataset_dir_path)

# Set the dimensional for the output image
(width, height) = (130, 100)

# load haar cascade classifier algorithm
face_cascade = cv2.CascadeClassifier(haar_file)

# start the camera capture
cap = cv2.VideoCapture(0)

num_captured = 0
while num_captured < 50:
    # read frame by frame
    _, frame = cap.read()

    # convert each frame to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # get the coordinates of the face
    face_coordinates = face_cascade.detectMultiScale(frame_grayscale, 1.3, 4)
    # draw a bounding box around the detected face
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0 ,255), 2)
        # slice the image to have the content of the bounding box only
        face = frame_grayscale[y:y+h, x:x+w]
        # resize image to desired size
        face_resized = cv2.resize(face, (width,height))
        # write resized face to a file
        cv2.imwrite("{}/{}.png".format(dataset_dir_path, num_captured), face_resized)
        num_captured += 1
    # display each frame
    cv2.imshow("Face", frame)

    # terminate the window when 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()