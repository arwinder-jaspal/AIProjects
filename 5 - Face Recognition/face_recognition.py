import cv2, numpy, os, datetime

# we will start by training the model
haar_file = "haarcascade_frontalface_default.xml"
dataset_dir = "datasets"
(width, height) = (100, 130)

# images are the images inside the each sub directory in dataset_dir
# label is the index of the subdir inside dataset_dir
# names is the mapping (using dict) of the label and the name of the subdir
# id is current index of the subdir
(images, labels, names, id) = ([], [], {}, 0)

for (subdirs, dirs, files) in os.walk(dataset_dir):
    for subdir in dirs:
        names[id] = subdir
        image_path = os.path.join(dataset_dir, subdir)
        for filename in os.listdir(image_path):
            image_filename = image_path + '/' + filename
            label = id
            images.append(cv2.imread(image_filename, 0))
            labels.append(int(label))
        id += 1

# List comprehension to convert to NumPy arrays
(images, labels) = [numpy.array(lis) for lis in [images, labels]]

# train the model to be able to recognize the given images
model = cv2.face.FisherFaceRecognizer.create()
model.train(images, labels)

# load haar cascade classifier algorithm
face_cascade = cv2.CascadeClassifier(haar_file)

# take in the frames from the camera live feed and compare with the datasets
cap = cv2.VideoCapture(0)

unknown_count = 0
while True:
    _, frame = cap.read()
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # apply haar cascade frontal face algo here
    faces = face_cascade.detectMultiScale(frame_grayscale, 1.3, 5)

    for (x ,y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # start recognizing face
        # crop the face
        face_gray = frame_grayscale[y:y+w, x:x+h]
        # resize the image
        face_resize = cv2.resize(face_gray, (width, height))
        # predict the face
        # outputs a tuple with first element being the id and second is the confidence level
        prediction = model.predict(face_resize)

        # if the face is a face from the dataset
        if prediction[1]<2000:
            cv2.putText(frame, "{} - {}".format(names[prediction[0]], prediction[1]), (x-10, y-10),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
            unknown_count = 0
        else:
            cv2.putText(frame,"Unknown Person", (x-10, y-10), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 0, 255), 1)
            unknown_count+=1
            if unknown_count >100:
                cv2.imwrite("datasets/Unknown_person_{}.png".format(datetime.datetime.now().isoformat()), frame)
                unknown_count = 0
    cv2.imshow("Face", frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

