# TODO: create test class
import time

import cv2
import logging


class ObjectDetector:
    base_path = "cascades/"
    item_dict = {"hammer": 1, "ruler": 2, "paintbucket": 3, "wrap": 4, "wrench": 5, "pencil": 6}
    hammer = "hammer"
    ruler = "ruler"
    paintbucket = "paintbucket"
    pencil = "pencil"
    wrap = "wrap"
    wrench = "wrench"
    scale_factor = 1.15
    cascade_producer = "mau/"  # stofi/ # mau/
    threshold = 5
    timeout = 30  # in seconds

    def __init__(self):
        logging.info("create new object detector")

    def find_pictogram_start_platform(self, video_capture):
        logging.info("find pictogram start platform")
        is_found, found_pictogram, position_x, position_y = self._do_haar_cascade(video_capture)
        return is_found, found_pictogram

    def find_pictogram_target_platform(self, video_capture):
        logging.info("find pictogram target platform")
        is_found, found_pictogram, position_x, position_y = self._do_haar_cascade(video_capture)
        return is_found, found_pictogram, position_x, position_y

    # Below: private methods
    # ugly but do the job
    def _do_haar_cascade(self, video_capture):
        logging.info("do haar cascade")
        is_found = False
        found_object = None
        position_x = None
        position_y = None
        timeout_start = time.time()

        logging.info("init classifier")
        hammer_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.hammer + ".xml")
        ruler_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.ruler + ".xml")
        paintbucket_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.paintbucket + ".xml")
        wrap_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.wrap + ".xml")
        wrench_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.wrench + ".xml")
        # pencil_clsfr = cv2.CascadeClassifier(self.base_path + self.cascade_producer + self.pencil + ".xml")

        threshold_hammer = threshold_ruler = threshold_paintbucket = threshold_wrap = threshold_wrench = threshold_pencil = 0

        while not is_found and time.time() < timeout_start + self.timeout:
            # get capture frames
            ret, frame = video_capture.read()
            # converting the color image to a gray scale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detecting in the gray scale
            # if detection is still unstable, add scale parameter (2nd position)
            hammers = hammer_clsfr.detectMultiScale(gray, self.scale_factor)
            rulers = ruler_clsfr.detectMultiScale(gray, self.scale_factor)
            paintbuckets = paintbucket_clsfr.detectMultiScale(gray, self.scale_factor)
            wraps = wrap_clsfr.detectMultiScale(gray, self.scale_factor)
            wrenches = wrench_clsfr.detectMultiScale(gray, self.scale_factor)
            # pencils = pencil_clsfr.detectMultiScale(gray, self.scale_factor)

            if len(hammers) >= 1:
                threshold_hammer += len(hammers)
                logging.info("saw some hammers")

            if len(rulers) >= 1:
                threshold_ruler += len(rulers)
                logging.info("saw some rulers")

            if len(paintbuckets) >= 1:
                threshold_paintbucket += len(paintbuckets)
                logging.info("saw some paintbuckets")

            if len(wraps) >= 1:
                threshold_wrap += len(wraps)
                logging.info("saw some wraps")

            if len(wrenches) >= 1:
                threshold_wrench += len(wrenches)
                logging.info("saw some wrenches")

            # if len(pencils) >= 1:
            #     threshold_pencil += len(pencils)
            #     logging.info("saw some pencils")

            if threshold_hammer >= self.threshold:
                is_found = True
                found_object = self.hammer
                position_x, position_y, w, h = hammers[0]
                logging.info("finally, it must be the hammer")
                break

            if threshold_ruler >= self.threshold:
                is_found = True
                found_object = self.ruler
                position_x, position_y, w, h = rulers[0]
                logging.info("finally, it must be the ruler")
                break

            if threshold_paintbucket >= self.threshold:
                is_found = True
                found_object = self.paintbucket
                position_x, position_y, w, h = paintbuckets[0]
                logging.info("finally, it must be the paintbucket")
                break

            if threshold_wrap >= self.threshold:
                is_found = True
                found_object = self.wrap
                position_x, position_y, w, h = wraps[0]
                logging.info("finally, it must be the wrap")
                break

            if threshold_wrench >= self.threshold:
                is_found = True
                found_object = self.wrench
                position_x, position_y, w, h = wrenches[0]
                logging.info("finally, it must be the wrench")
                break

            # if threshold_pencil >= self.threshold:
            #     is_found = True
            #     found_object = self.pencil
            #     position_x, position_y, w, h = pencils[0]
            #     logging.info("finally, it must be the pencil")
            #     break

            timediff = timeout_start + self.timeout - time.time()
            logging.warning("nothing found, try again for max " + timediff.__str__() + " seconds..")

        return is_found, found_object, position_x, position_y
