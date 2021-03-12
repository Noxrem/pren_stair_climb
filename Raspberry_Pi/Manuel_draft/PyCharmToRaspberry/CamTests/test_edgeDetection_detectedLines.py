#!/usr/bin/env python
# coding: utf-8
import matplotlib as mpl
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.transform import hough_line, hough_line_peaks
mpl.rcParams['figure.dpi']= 400

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
    frame2D = LiveCamEdgeDetection_canny(frame)
    hspace, theta, distances = hough_line(frame2D)
    accum, angles, dist_peaks = hough_line_peaks(hspace, theta, distances, threshold=100)
    mpl.rcParams['figure.dpi']=200
    plt.imshow(frame2D)
    ax = plt.gca() #gca: get current axes
    for angle, dist in zip(angles, dist_peaks):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - frame2D.shape[1] * np.cos(angle)) / np.sin(angle)
        ax.plot((0, frame2D.shape[1]), (y0, y1), '-r')
    ax.set_xlim((0, frame2D.shape[1]))
    ax.set_ylim((frame2D.shape[0], 0))
    ax.set_axis_off()
    ax.set_title('Detected lines')
    cv2.imshow('Live Edge Detection', LiveCamEdgeDetection_canny(frame))
    cv2.imshow('Webcam Video', frame)
    if cv2.waitKey(1) == 13: #13 Enter Key
        break
        
cap.release() # camera release
cv2.destroyAllWindows()
