from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL


class Model:
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])

        for i in range(1, counters[0]):  # for each image in the first class
            img = cv.imread(f'1/frame{i}.jpg')[:, :, 0]  # read the image
            img = img.reshape(16800)  # reshape the image
            img_list = np.append(img_list, [img])  # add the image to the list
            class_list = np.append(class_list, [1])  # add the class to the list

        for i in range(1, counters[1]):  # for each image in the second class
            img = cv.imread(f'2/frame{i}.jpg')[:, :, 0]
            img = img.reshape(16800)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, [2])

        img_list = img_list.reshape(counters[0] - 1 + counters[1] - 1, 16800)  # reshape the list of images
        self.model.fit(img_list, class_list)  # train the model
        print("Model Successfully Trained")

    def predict(self, frame):
        frame = frame[1]
        cv.imwrite("frame.jpg", cv.cvtColor(frame, cv.COLOR_RGB2BGR))  # save the image
        img = PIL.Image.open("frame.jpg")
        img.thumbnail((150, 150), PIL.Image.ANTIALIAS)
        img.save("frame.jpg")

        img = cv.imread("frame.jpg")[:, :, 0]  # read the image
        img = img.reshape(16800)  # reshape the image
        prediction = self.model.predict([img])  # predict the class

        return prediction[0]
