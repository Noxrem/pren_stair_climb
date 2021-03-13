import cv2
import numpy as np

video = cv2.VideoCapture(0)

# Write some Text

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 100)
fontScale = 1
fontColor = (0, 255, 0)
lineType = 2


def nothing(x):
    pass


windowName = "Trackbar Board"
trackbar0_name = 'NoHLines'
trackbar1_name = 'NoLines'
trackbar2_name = 'maxLineGap'
trackbar3_name = 'lineLength'
trackbar4_name = 'lineRotation'
trackbar5_name = 'canny1'
trackbar6_name = 'canny2'
cv2.namedWindow(windowName, cv2.WINDOW_GUI_NORMAL)
cv2.createTrackbar(trackbar0_name, windowName, 4, 10, nothing)  # third parameter = default value / best value 4
cv2.createTrackbar(trackbar1_name, windowName, 100, 200, nothing)  # best value 100
cv2.createTrackbar(trackbar2_name, windowName, 40, 100, nothing)  # best value: 50
cv2.createTrackbar(trackbar3_name, windowName, 313, 700, nothing)  # best value: 313
cv2.createTrackbar(trackbar4_name, windowName, 1, 30, nothing)  # best value: 1
cv2.createTrackbar(trackbar5_name, windowName, 100, 255, nothing)  # best value: 100
cv2.createTrackbar(trackbar6_name, windowName, 120, 255, nothing)  # best value: 120


while True:

    amount_h_lines = cv2.getTrackbarPos(trackbar0_name, windowName)
    amount_lines = cv2.getTrackbarPos(trackbar1_name, windowName)
    max_line_gap = cv2.getTrackbarPos(trackbar2_name, windowName)
    line_length = cv2.getTrackbarPos(trackbar3_name, windowName)
    line_rotation = cv2.getTrackbarPos(trackbar4_name, windowName)
    canny1 = cv2.getTrackbarPos(trackbar5_name, windowName)
    canny2 = cv2.getTrackbarPos(trackbar6_name, windowName)
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture(0)
        continue
    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # color1 = np.array([0, 0, 0])
    # color2 = np.array([255, 255, 255])
    # mask = cv2.inRange(hsv, color1, color2)
    edges = cv2.Canny(frame, canny1, canny2)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=max_line_gap)
    horizontal_lines = list()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if abs(x2 - x1) > line_length and abs(y2 - y1) < line_rotation:
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                horizontal_lines.append(line)
                print("h" + str(len(horizontal_lines)))
                if len(horizontal_lines) >= amount_h_lines and len(lines) >= amount_lines:
                    print("stair detected")
                    cv2.putText(frame, 'stair detected!',
                                bottomLeftCornerOfText,
                                font,
                                fontScale,
                                fontColor,
                                lineType)
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
