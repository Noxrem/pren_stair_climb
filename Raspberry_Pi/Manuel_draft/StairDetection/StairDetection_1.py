import cv2
import numpy as np
video = cv2.VideoCapture(0)
while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture(0)
        continue
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # color1 = np.array([0, 0, 0])
    # color2 = np.array([255, 255, 255])
    # mask = cv2.inRange(hsv, color1, color2)
    edges = cv2.Canny(frame, 200, 200)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=150)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if abs(x2 - x1) > 500 and abs(y2 - y1) < 30 :
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()