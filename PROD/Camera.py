import cv2
import CamServo
import logging
from picamera.array import PiRGBArray


class Camera:
    cam_servo = None
    capture = None
    cam_resolution = None
    cam_frame_rate = None
    rawCapture = None

    def __init__(self):
        logging.info("create new camera")
        self.cam_servo = CamServo.CamServo()
        self.capture = cv2.VideoCapture(0)
        self.cam_resolution = (640, 480)
        self.cam_frame_rate = 90  # TODO: define best frame rate
        self.rawCapture = PiRGBArray(self.capture, size=(640, 480))
