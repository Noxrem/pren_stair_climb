import cv2
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from skimage.transform import hough_line, hough_line_peaks

cap  = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    colored = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    blurred = cv2.GaussianBlur(colored, (5,5),0)
    flipped = cv2.flip(blurred, flipCode = -1)
    cv2.imshow("Video", flipped)
    edges = cv2.Canny(flipped,30,100)
    hspace, theta, distances = hough_line(edges)
    accum, angles, dist_peaks = hough_line_peaks(hspace, theta, distances, threshold=100)
    mpl.rcParams['figure.dpi']=200
    cv2.imshow("Edges", edges)
    cv2.imshow("",flipped)
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imwrite(edges,edges)

 
    if cv2.waitKey(1) == 13: #13 Enter Key
        break

cap.release() # camera release
cv2.destroyAllWindows()

