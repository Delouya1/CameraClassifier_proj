import cv2 as cv


class Camera:
    def __init__(self):  # constructor
        self.camera = cv.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Camera not found")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):  # destructor
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):  # get the current frame from the camera
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:  # if the frame was successfully read
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))  # convert the image to RGB
        return None


