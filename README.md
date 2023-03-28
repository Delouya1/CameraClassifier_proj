Camera Classifier

This project is a simple Python application that uses a machine learning model to classify camera frames into two categories based on the image content. 
The model is trained using a set of sample images provided by the user, and then used to classify frames captured by a camera in real-time.

Prerequisites
To use this application, 
you will need to have the following installed on your computer:
Python 3
tkinter
OpenCV
Pillow
NumPy
scikit-learn
Running the application
To run the application, simply execute the app.py file in your Python environment. The application will open a GUI window that displays the live video feed from your camera. You can then use the following buttons to interact with the application:

Auto Prediction: 
Toggle automatic prediction mode. 
When enabled, the application will continuously predict the class of the current camera frame and display the result in the GUI.
[Class Name One]: Save the current camera frame to the folder for Class One. You will be prompted to enter the name of the first class when you run the application.
[Class Name Two]: Save the current camera frame to the folder for Class Two. You will be prompted to enter the name of the second class when you run the application.
Train Model: Train the machine learning model using the saved images in the Class One and Class Two folders.
Predict: Predict the class of the current camera frame and display the result in the GUI.
Reset: Delete all saved images and reset the machine learning model.
Files
The project contains the following files:

app.py: The main application file that defines the GUI and connects to the camera and machine learning model.
camera.py: A module that handles camera input and provides frames to the application.
model.py: A module that defines the machine learning model and provides methods for training and prediction.

Acknowledgments
inspiered by neaural nine - used a diffrent modle i wrote myself.
