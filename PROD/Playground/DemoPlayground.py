import Playground
import cv2

playground = Playground.Playground()
capture = cv2.VideoCapture(0)
playground.find_stair(capture)
