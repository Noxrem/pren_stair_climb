import cv2
import numpy as np
import time
import logging


class StairDetector:

    def __init__(self):
        logging.info("create new stair detector")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.bottom_left_corner_of_text = (10, 100)
        self.font_scale = 1
        self.font_color = (0, 0, 255)
        self.line_type = 2
        self.detection_counter = 0
        self.amount_v_lines = 50  # TODO: define best values
        self.amount_h_lines = 50
        self.amount_lines = 100
        self.max_line_gap = 40
        self.line_h_length = 313
        self.line_v_length = 50
        self.line_rotation = 1
        self.canny1 = 18
        self.canny2 = 43
        self.target_amount_detections = 60
        self.window_trackbar_name = "Trackbar Board"
        self.trackbar0_name = 'NoVLines'
        self.trackbar1_name = 'NoHLines'
        self.trackbar2_name = 'NoLines'
        self.trackbar3_name = 'maxLineGap'
        self.trackbar4_name = 'lenHLine'
        self.trackbar5_name = 'lenVLine'
        self.trackbar6_name = 'lineRotation'
        self.trackbar7_name = 'canny1'
        self.trackbar8_name = 'canny2'
        self.trackbar9_name = 'NoDetect'
        self.max_time_stair_detection = 200  # TODO: define max duration
        self.is_stair_found = False

    def nothing(self, nothing):
        pass

    def _create_trackbar_window(self):
        cv2.namedWindow(self.window_trackbar_name, cv2.WINDOW_GUI_NORMAL)
        cv2.createTrackbar(self.trackbar0_name, self.window_trackbar_name, self.amount_v_lines, 30, self.nothing)
        cv2.createTrackbar(self.trackbar1_name, self.window_trackbar_name, self.amount_h_lines, 10, self.nothing)
        cv2.createTrackbar(self.trackbar2_name, self.window_trackbar_name, self.amount_lines, 200, self.nothing)
        cv2.createTrackbar(self.trackbar3_name, self.window_trackbar_name, self.max_line_gap, 100, self.nothing)
        cv2.createTrackbar(self.trackbar4_name, self.window_trackbar_name, self.line_h_length, 700, self.nothing)
        cv2.createTrackbar(self.trackbar5_name, self.window_trackbar_name, self.line_v_length, 200, self.nothing)
        cv2.createTrackbar(self.trackbar6_name, self.window_trackbar_name, self.line_rotation, 200, self.nothing)
        cv2.createTrackbar(self.trackbar7_name, self.window_trackbar_name, self.canny1, 255, self.nothing)
        cv2.createTrackbar(self.trackbar8_name, self.window_trackbar_name, self.canny2, 255, self.nothing)
        cv2.createTrackbar(self.trackbar9_name, self.window_trackbar_name, self.target_amount_detections, 300, self.nothing)

    def find_stair(self, video_capture, is_running_on_a_display):
        logging.info("find stair")
        start_time = time.time()
        logging.debug("start time of stair detection: " + str(start_time))
        if is_running_on_a_display:
            self._create_trackbar_window()
        while True:
            if is_running_on_a_display:
                self.amount_v_lines = cv2.getTrackbarPos(self.trackbar0_name, self.window_trackbar_name)
                self.amount_h_lines = cv2.getTrackbarPos(self.trackbar1_name, self.window_trackbar_name)
                self.amount_lines = cv2.getTrackbarPos(self.trackbar2_name, self.window_trackbar_name)
                self.max_line_gap = cv2.getTrackbarPos(self.trackbar3_name, self.window_trackbar_name)
                self.line_h_length = cv2.getTrackbarPos(self.trackbar4_name, self.window_trackbar_name)
                self.line_v_length = cv2.getTrackbarPos(self.trackbar5_name, self.window_trackbar_name)
                self.line_rotation = cv2.getTrackbarPos(self.trackbar6_name, self.window_trackbar_name)
                self.canny1 = cv2.getTrackbarPos(self.trackbar7_name, self.window_trackbar_name)
                self.canny2 = cv2.getTrackbarPos(self.trackbar8_name, self.window_trackbar_name)
                self.target_amount_detections = cv2.getTrackbarPos(self.trackbar9_name, self.window_trackbar_name)
            video = video_capture
            ret, orig_frame = video.read()
            frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
            # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # TODO: Remove Code
            # color1 = np.array([0, 0, 0])
            # color2 = np.array([255, 255, 255])
            # mask = cv2.inRange(hsv, color1, color2)
            edges = cv2.Canny(frame, self.canny1, self.canny2)
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=self.max_line_gap)
            if lines is not None:
                horizontal_lines = list()
                vertical_lines = list()
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    if abs(x2 - x1) > self.line_h_length and abs(y2 - y1) < self.line_rotation:
                        if is_running_on_a_display:
                            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                        horizontal_lines.append(line)
                        logging.debug("h" + str(len(horizontal_lines)))
                    if abs(y2 - y1) > self.line_v_length and abs(x2 - x1) < 20:  # Rotation line_v
                        if is_running_on_a_display:
                            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
                        vertical_lines.append(line)
                        logging.debug("v" + str(len(vertical_lines)))
                    if len(horizontal_lines) >= self.amount_h_lines and len(vertical_lines) >= self.amount_v_lines and len(
                            lines) >= self.amount_lines:
                        logging.info("stair detected")
                        if is_running_on_a_display:
                            cv2.putText(frame, 'stair detected!',
                                        self.bottom_left_corner_of_text,
                                        self.font,
                                        self.font_scale,
                                        self.font_color,
                                        self.line_type)
                        self.detection_counter = self.detection_counter + 1
            if is_running_on_a_display:
                cv2.imshow("frame", frame)
                cv2.imshow("edges", edges)
            diff_time = time.time() - start_time
            logging.debug("used time: " + str(diff_time))
            key = cv2.waitKey(1)
            if self.detection_counter >= self.target_amount_detections or key == 27:
                self.is_stair_found = True
                break
            if self.max_time_stair_detection <= diff_time:
                logging.warning("stair could not be found")
                self.is_stair_found = False
                break
        video_capture.release()
        if is_running_on_a_display:
            cv2.destroyAllWindows()
        return self.is_stair_found
