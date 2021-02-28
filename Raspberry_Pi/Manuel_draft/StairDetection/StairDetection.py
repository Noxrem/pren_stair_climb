import cv2
import numpy as np

# for displaying images in jupyter

import matplotlib as mpl
from matplotlib import pyplot as plt
from skimage.transform import hough_line, hough_line_peaks

cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# edges = cv2.Canny(frame, 100, 100)
# gray = cv2.cvtColor(edges,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
#
# lines = cv2.HoughLines(edges,1,np.pi/180,200)
# for rho,theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#
#     cv2.line(edges,(x1,y1),(x2,y2),(0,0,255),2)
#
# cv2.imwrite('houghlines3.jpg',edges)
#
while True:
    ret, frame = cap.read()
    edges = cv2.Canny(frame, 100, 100)
    cv2.imshow('Window', edges)
    # hspace, theta, distances = hough_line(edges)
    # accum, angles, dist_peaks = hough_line_peaks(hspace, theta, distances, threshold=320)
    # mpl.rcParams['figure.dpi'] = 200
    # cv2.imshow('Edges', edges)
    # ax = plt.gca()
    # for angle, dist in zip(angles, dist_peaks):
    #     y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    #     y1 = (dist - edges.shape[1] * np.cos(angle)) / np.sin(angle)
    #     ax.plot((0, edges.shape[1]), (y0, y1), '-r')
    # ax.set_xlim((0, edges.shape[1]))
    # ax.set_ylim((edges.shape[0], 0))
    # ax.set_axis_off()
    # ax.set_title('Detected lines')

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

