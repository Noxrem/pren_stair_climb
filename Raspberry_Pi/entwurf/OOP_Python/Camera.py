import CamServo
import cv2

class Camera:

    camServo = None

    def __init__(self):
        print("new camera created")
        self.camServo = CamServo.CamServo()

    def turn_ahead(self):
        self.camServo.turn_ahead()

    def turn_right(self):
        self.camServo.turn_right()

    def stream_video(self):
        print("video stream started")
        cap = cv2.VideoCapture(0)
        counter = 0
        while (True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            # TODO: Counter entfernen und Abbruchsbedingung an gefundenes Piktogramm koppeln
            counter += 1
            if counter % 100 == 0:
                print(counter)
            if counter >= 100 or (cv2.waitKey(1) & 0xFF == ord('q')):
                break
