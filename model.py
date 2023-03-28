from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL


class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = []
        class_list = []

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:, :, 0]
            img = cv.resize(img, (140, 120)).reshape(16800)
            img_list.append(img)
            class_list.append(1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')[:, :, 0]
            img = img = cv.resize(img, (140, 120)).reshape(16800)
            img_list.append(img)
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        self.model.fit(img_list, class_list)
        print("Model successfully trained!")

    def predict(self, frame):
        # convert frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

        # resize frame to match training data
        resized = cv.resize(gray, (120, 140))

        # flatten frame to 1-dimensional array
        flattened = resized.flatten()

        # make prediction
        prediction = self.model.predict([flattened])

        return prediction[0]
