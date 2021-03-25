import cv2
import CamServo
from picamera import PiCamera
from picamera.array import PiRGBArray


class Camera:
    cam_servo = None
    cam = None
    cam_resolution = None
    cam_frame_rate = None
    rawCapture = None

    def __init__(self):
        print("create new camera")
        self.camServo = CamServo.CamServo()
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.cam_resolution = (640, 480)
        self.cam_frame_rate = 32
        self.rawCapture = PiRGBArray(self.cam, size=(640, 480))

    def turn_ahead(self):
        print("camera turn ahead")
        self.camServo.turn_ahead()

    def turn_right(self):
        print("camera turn right")
        self.camServo.turn_right()
