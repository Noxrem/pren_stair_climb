import cv2
import numpy as np


class StairDetector:
    video = cv2.VideoCapture(0)

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottom_left_corner_of_text = (10, 100)
    font_scale = 1
    font_color = (0, 0, 255)
    line_type = 2

    def nothing(self):
        pass

    def find_stair(self):
        window_name = "Trackbar Board"

        trackbar0_name = 'NoVLines'
        trackbar1_name = 'NoHLines'
        trackbar2_name = 'NoLines'
        trackbar3_name = 'maxLineGap'
        trackbar4_name = 'lenHLine'
        trackbar5_name = 'lenVLine'
        trackbar6_name = 'lineRotation'
        trackbar7_name = 'canny1'
        trackbar8_name = 'canny2'
        cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar(trackbar0_name, window_name, 8, 30, self.nothing)  # third parameter = default value / best value 8
        cv2.createTrackbar(trackbar1_name, window_name, 4, 10, self.nothing)  # third parameter = default value / best value 4
        cv2.createTrackbar(trackbar2_name, window_name, 100, 200, self.nothing)  # best value 100
        cv2.createTrackbar(trackbar3_name, window_name, 40, 100, self.nothing)  # best value: 50
        cv2.createTrackbar(trackbar4_name, window_name, 313, 700, self.nothing)  # best value: 313
        cv2.createTrackbar(trackbar5_name, window_name, 50, 200, self.nothing)  # best value: 50
        cv2.createTrackbar(trackbar6_name, window_name, 1, 30, self.nothing)  # best value: 1
        cv2.createTrackbar(trackbar7_name, window_name, 100, 255, self.nothing)  # best value: 100
        cv2.createTrackbar(trackbar8_name, window_name, 120, 255, self.nothing)  # best value: 120

        while True:
            amount_v_lines = cv2.getTrackbarPos(trackbar0_name, window_name)
            amount_h_lines = cv2.getTrackbarPos(trackbar1_name, window_name)
            amount_lines = cv2.getTrackbarPos(trackbar2_name, window_name)
            max_line_gap = cv2.getTrackbarPos(trackbar3_name, window_name)
            line_h_length = cv2.getTrackbarPos(trackbar4_name, window_name)
            line_v_length = cv2.getTrackbarPos(trackbar5_name, window_name)
            line_rotation = cv2.getTrackbarPos(trackbar6_name, window_name)
            canny1 = cv2.getTrackbarPos(trackbar7_name, window_name)
            canny2 = cv2.getTrackbarPos(trackbar8_name, window_name)
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
                                    self.bottom_left_corner_of_text,
                                    self.font,
                                    self.font_scale,
                                    self.font_color,
                                    self.line_type)
            cv2.imshow("frame", frame)
            cv2.imshow("edges", edges)
            key = cv2.waitKey(1)
            if key == 27:
                break
        self.video.release()
        cv2.destroyAllWindows()
