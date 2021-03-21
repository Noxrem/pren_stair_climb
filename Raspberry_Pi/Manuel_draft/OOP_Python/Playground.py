import cv2
import numpy as np


class PlaygroundStairDetector:
    video = cv2.VideoCapture(0)

    # Write some Text

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 100)
    fontScale = 1
    fontColor = (0, 0, 255)
    lineType = 2

    def nothing(self):
        pass

    def findstair(self):
        windowName = "Trackbar Board"

        trackbar0_name = 'NoVLines'
        trackbar1_name = 'NoHLines'
        trackbar2_name = 'NoLines'
        trackbar3_name = 'maxLineGap'
        trackbar4_name = 'lenHLine'
        trackbar5_name = 'lenVLine'
        trackbar6_name = 'lineRotation'
        trackbar7_name = 'canny1'
        trackbar8_name = 'canny2'
        cv2.namedWindow(windowName, cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar(trackbar0_name, windowName, 8, 30, self.nothing)  # third parameter = default value / best value 8
        cv2.createTrackbar(trackbar1_name, windowName, 4, 10, self.nothing)  # third parameter = default value / best value 4
        cv2.createTrackbar(trackbar2_name, windowName, 100, 200, self.nothing)  # best value 100
        cv2.createTrackbar(trackbar3_name, windowName, 40, 100, self.nothing)  # best value: 50
        cv2.createTrackbar(trackbar4_name, windowName, 313, 700, self.nothing)  # best value: 313
        cv2.createTrackbar(trackbar5_name, windowName, 50, 200, self.nothing)  # best value: 50
        cv2.createTrackbar(trackbar6_name, windowName, 1, 30, self.nothing)  # best value: 1
        cv2.createTrackbar(trackbar7_name, windowName, 100, 255, self.nothing)  # best value: 100
        cv2.createTrackbar(trackbar8_name, windowName, 120, 255, self.nothing)  # best value: 120

        while True:

            amount_v_lines = cv2.getTrackbarPos(trackbar0_name, windowName)
            amount_h_lines = cv2.getTrackbarPos(trackbar1_name, windowName)
            amount_lines = cv2.getTrackbarPos(trackbar2_name, windowName)
            max_line_gap = cv2.getTrackbarPos(trackbar3_name, windowName)
            line_h_length = cv2.getTrackbarPos(trackbar4_name, windowName)
            line_v_length = cv2.getTrackbarPos(trackbar5_name, windowName)
            line_rotation = cv2.getTrackbarPos(trackbar6_name, windowName)
            canny1 = cv2.getTrackbarPos(trackbar7_name, windowName)
            canny2 = cv2.getTrackbarPos(trackbar8_name, windowName)
            ret, orig_frame = self.video.read()
            if not ret:
                self.video = cv2.VideoCapture(0)
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
                horizontal_lines = list()
                vertical_lines = list()
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    if abs(x2 - x1) > line_h_length and abs(y2 - y1) < line_rotation:
                        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                        horizontal_lines.append(line)
                        print("h" + str(len(horizontal_lines)))
                    if abs(y2 - y1) > line_v_length and abs(x2 - x1) < 20:  # Rotation line_v
                        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
                        vertical_lines.append(line)
                        print("v" + str(len(vertical_lines)))
                    if len(horizontal_lines) >= amount_h_lines and len(vertical_lines) >= amount_v_lines and len(
                            lines) >= amount_lines:
                        print("stair detected")
                        cv2.putText(frame, 'stair detected!',
                                    self.bottomLeftCornerOfText,
                                    self.font,
                                    self.fontScale,
                                    self.fontColor,
                                    self.lineType)
            cv2.imshow("frame", frame)
            cv2.imshow("edges", edges)
            key = cv2.waitKey(1)
            if key == 27:
                break
        self.video.release()
        cv2.destroyAllWindows()

playground = PlaygroundStairDetector()
playground.findstair()
