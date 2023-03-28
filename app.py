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

        # self.init_gui()  # initialize the GUI

        self.delay = 15  # delay between frames in milliseconds
        self.update()  # start the update loop

        self.window.attributes('topmost', True)
        self.window.mainloop()  # start the GUI

    def init_gui(self):
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack()

        self.btn_toggle_auto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.auto_predict_toggle)
        self.btn_toggle_auto.pack(anchor=tk.CENTER, expand=True)

        self.classname_one = simpledialog.askstring("Class 1", "Enter the name of the first class:",
                                                    parent=self.window)
        self.classname_two = simpledialog.askstring("Class 2", "Enter the name of the second class:",
                                                    parent=self.window)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50, command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50, command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.Button(self.window, text="Train Model", width=50, command=lambda : self.model.train_model(self.counters))
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
