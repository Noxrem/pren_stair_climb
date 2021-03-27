import cv2
import CamServo
from picamera import PiCamera
from picamera.array import PiRGBArray


class Camera:
    cam_servo = None
    capture = None
    cam_resolution = None
    cam_frame_rate = None
    rawCapture = None

    def __init__(self):
        print("create new camera")
        self.camServo = CamServo.CamServo()
        self.capture = cv2.VideoCapture(0)
        self.cam_resolution = (640, 480)
        self.cam_frame_rate = 32
        self.rawCapture = PiRGBArray(self.capture, size=(640, 480))

    def turn_ahead(self):
        print("camera turn ahead")
        self.camServo.turn_ahead()

    def turn_right(self):
        print("camera turn right")
        self.camServo.turn_right()
