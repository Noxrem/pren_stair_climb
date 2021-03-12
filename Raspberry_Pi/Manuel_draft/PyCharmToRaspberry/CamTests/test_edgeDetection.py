#!/usr/bin/env python
# coding: utf-8
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

def Cartoon(image_color):
    output_image = cv2.stylization(image_color, sigma_s=100, sigma_r=0.3)
    return output_image

def LiveCamEdgeDetection_canny(image_color):
    threshold_1 = 30
    threshold_2 = 80
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, threshold_1, threshold_2)
    return canny
# Main calling function to initialize webcam and apply edge detection

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Edge Detection', LiveCamEdgeDetection_canny(frame))
    cv2.imshow('Webcam Video', frame)
    if cv2.waitKey(1) == 13: #13 Enter Key
        break
        
cap.release() # camera release
cv2.destroyAllWindows()
