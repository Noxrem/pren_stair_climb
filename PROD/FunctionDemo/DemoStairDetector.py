import StairDetector
import Camera

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

stair_detector = StairDetector.StairDetector()
camera = Camera.Camera()

stair_detector.find_stair(camera.capture, True, False)
