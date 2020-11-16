## Capturing auf Raspi

from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import numpy as np
import cv2


def object_search():
    print( "loading Cascade")
    hammer_clsfr = cv2.CascadeClassifier("/data/haar-cascade.xml")

    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    # allow the camera to warmup
    time.sleep(1.0)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        hammers = hammer_clsfr.detectMultiScale(image)
        for (x, y, w, h) in hammers:
            # going through each and every face and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, 'Hammer', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # show the frame
        cv2.imshow("Raspi-View", image)

        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    object_search()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
