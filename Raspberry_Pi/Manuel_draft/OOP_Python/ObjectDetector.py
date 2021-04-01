import Camera
import time
import cv2

class ObjectDetector:
    camera = None

    def __init__(self):
        print("new object detector created")
        self.camera = Camera.Camera()

    def find_pictogram(self):
        print("find pictogram")
        is_found, found_pictogram = self.do_haarcascade()
        return is_found, found_pictogram

    def do_haarcascade(self):
        print("do haar cascade")

        # TODO: Hier HaarCascade einbauen und is_found und found_object setzen
        is_found = True
        found_object = "paint bucket"
        return is_found, found_object

