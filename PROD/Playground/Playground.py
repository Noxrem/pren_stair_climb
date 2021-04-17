import cv2
import numpy as np
import logging


class StairDetector:
    font = None
    bottom_left_corner_of_text = None
    font_scale = None
    font_color = None
    line_type = None
    detection_counter = None

    def __init__(self):
        logging.info("create new stair detector")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.bottom_left_corner_of_text = (10, 100)
        self.font_scale = 1
        self.font_color = (0, 0, 255)
        self.line_type = 2
        self.detection_counter = 0

    def nothing(self):
        pass

    def find_stair(self, video_capture):
        logging.info("find stair")
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
        trackbar9_name = 'NoDetect'
        cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar(trackbar0_name, window_name, 8, 30,
                           self.nothing)  # third parameter = default value / best value 8
        cv2.createTrackbar(trackbar1_name, window_name, 8, 10,
                           self.nothing)  # third parameter = default value / best value 8
        cv2.createTrackbar(trackbar2_name, window_name, 100, 200, self.nothing)  # best value 100
        cv2.createTrackbar(trackbar3_name, window_name, 40, 100, self.nothing)  # best value: 40
        cv2.createTrackbar(trackbar4_name, window_name, 313, 700, self.nothing)  # best value: 313
        cv2.createTrackbar(trackbar5_name, window_name, 50, 200, self.nothing)  # best value: 50
        cv2.createTrackbar(trackbar6_name, window_name, 1, 200, self.nothing)  # best value: 1
        cv2.createTrackbar(trackbar7_name, window_name, 18, 255,
                           self.nothing)  # best value: 100  # TODO: define best value
        cv2.createTrackbar(trackbar8_name, window_name, 43, 255,
                           self.nothing)  # best value: 120  # TODO: define best value
        cv2.createTrackbar(trackbar9_name, window_name, 60, 300,
                           self.nothing)  # best value: ?  # TODO: define best value. Depends on frame rate

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
            target_amount_detections = cv2.getTrackbarPos(trackbar9_name, window_name)
            video = video_capture
            ret, orig_frame = video.read()
            frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
            # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # TODO: Remove Code
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
                        logging.debug("h" + str(len(horizontal_lines)))
                    if abs(y2 - y1) > line_v_length and abs(x2 - x1) < 20:  # Rotation line_v
                        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
                        vertical_lines.append(line)
                        logging.debug("v" + str(len(vertical_lines)))
                    if len(horizontal_lines) >= amount_h_lines and len(vertical_lines) >= amount_v_lines and len(
                            lines) >= amount_lines:
                        logging.info("stair detected")
                        cv2.putText(frame, 'stair detected!',
                                    self.bottom_left_corner_of_text,
                                    self.font,
                                    self.font_scale,
                                    self.font_color,
                                    self.line_type)
                        self.detection_counter = self.detection_counter + 1
            cv2.imshow("frame", frame)
            cv2.imshow("edges", edges)
            key = cv2.waitKey(1)
            if self.detection_counter >= target_amount_detections or key == 27:
                break
        video_capture.release()
        cv2.destroyAllWindows()