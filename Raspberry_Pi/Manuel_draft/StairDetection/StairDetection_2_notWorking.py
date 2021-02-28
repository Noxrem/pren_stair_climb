import cv2
import numpy as np

# for displaying images in jupyter

import matplotlib as mpl
from matplotlib import pyplot as plt
from skimage.transform import hough_line, hough_line_peaks

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

canny = "Canny"
cv2.namedWindow(canny)
cv2.createTrackbar('Threshold 1', canny, 0, 255, nothing)
cv2.createTrackbar('Threshold 2', canny, 0, 255, nothing)

while True:
    ret, frame = cap.read()

    t1 = cv2.getTrackbarPos('Threshold 1', canny)
    t2 = cv2.getTrackbarPos('Threshold 2', canny)
    gb = cv2.GaussianBlur(frame, (5, 5), 0)
    can = cv2.Canny(gb, t1, t2)

    edges = cv2.Canny(gb, t1, t2)
    hspace, theta, distances = hough_line(edges)
    accum, angles, dist_peaks = hough_line_peaks(hspace, theta, distances, threshold=320)
    mpl.rcParams['figure.dpi'] = 200
    cv2.imshow('Edges', edges)
    ax = plt.gca()
    for angle, dist in zip(angles, dist_peaks):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - edges.shape[1] * np.cos(angle)) / np.sin(angle)
        ax.plot((0, edges.shape[1]), (y0, y1), '-r')
    ax.set_xlim((0, edges.shape[1]))
    ax.set_ylim((edges.shape[0], 0))
    ax.set_axis_off()
    ax.set_title('Detected lines')

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

