import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import camera


class App:
    def __int__(self, window=tk.Tk(), window_title="AI Camera", video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        self.counters = [1, 1]  # counters for the images
        # self.model = ....

        self.auto_predict = False  # whether to automatically predict the class of the image

        self.camera = camera.Camera()  # create the camera object

        self.init_gui()  # initialize the GUI

        self.delay = 15  # delay between frames in milliseconds
        self.update()  # start the update loop

        self.window.attributes('topmost', True)
        self.window.mainloop()  # start the GUI

    def init_gui(self):
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggle_auto = tk.Button(self.window, text="Auto Prediction", width=50,
                                         command=self.auto_predict_toggle)
        self.btn_toggle_auto.pack(anchor=tk.CENTER, expand=True)

        self.classname_one = simpledialog.askstring("Class 1", "Enter the name of the first class:",
                                                    parent=self.window)
        self.classname_two = simpledialog.askstring("Class 2", "Enter the name of the second class:",
                                                    parent=self.window)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50,
                                       command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50,
                                       command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, text="Train Model", width=50,
                                   command=lambda: self.model.train_model(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_predict = tk.Button(self.window, text="Predict", width=50, command=self.predict)
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.Button(self.window, text="Reset", width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.class_label = tk.label(self.window, text="Class")
        self.class_label.config(font=("Courier", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict

    def save_for_class(self, class_number): # save the current frame for the given class
        ret, frame = self.camera.get_frame()
        if not os.path.exists("1"):
            os.makedirs("1")
        if not os.path.exists("2"):
            os.makedirs("2")

        cv.imwrite(f'{class_number}/{self.counters[class_number - 1]}.jpg', cv.cvtColor(frame, cv.COLOR_RGB2BGR))  # save the image
        img = PIL.open(f'{class_number}/{self.counters[class_number - 1]}.jpg')
        img.thumbnail((150, 150), PIL.Image.ANTIALIAS)
        img.save(f'{class_number}/{self.counters[class_number - 1]}.jpg')

        self.counters[class_number - 1] += 1  # increment the counter

    def reset(self):
        for directory in ["1", "2"]:
            for file in os.listdir(directory):  # iterate over the files in the directory
                file_path = os.path.join(directory, file)  # get the full path of the file
                try:
                    if os.path.isfile(file_path):  # if the file is a file
                        os.unlink(file_path)  # delete the file
                except Exception as e:
                    print(e)
        self.counters = [1, 1]  # reset the counters
        # self.model = model.Model() # reset the model

    def update(self):
        if self.auto_predict:
            self.predict()
            pass

        ret, frame = self.camera.get_frame()  # get the current frame from the camera
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))  # convert the image to PIL format
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)  # add the image to the canvas in the
            # upper left corner

        self.window.after(self.delay, self.update)  # call the update function again after the delay






