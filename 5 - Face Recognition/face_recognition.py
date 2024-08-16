import cv2, numpy, os

# we will start by training the model
haar_file = "haarcascade_frontalface_default.xml"
dataset_dir = "datasets"

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

# train the model to be able recognize the given images
model = cv2.face.FisherFaceRecognizer.create()
model.train(images, labels)


