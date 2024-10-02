import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        if not self.camera.isOpened():
            raise Exception("Error: Could not open camera.")

    def get_frame(self):
        ret, frame = self.camera.read()
        if not ret:
            raise Exception("Error: Could not read frame.")
        return frame

    def release(self):
        self.camera.release()
