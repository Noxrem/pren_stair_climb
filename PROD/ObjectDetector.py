# TODO: create test class
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
    target = None
    threshold = 10

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

    def _do_haar_cascade(self, video_capture):
        logging.info("do haar cascade")
        is_found = False
        found_object = None
        position_x = None
        position_y = None

        print("init classifier")
        hammer_clsfr = cv2.CascadeClassifier(self.base_path + self.hammer + ".xml")
        ruler_clsfr = cv2.CascadeClassifier(self.base_path + self.ruler + ".xml")
        paintbucket_clsfr = cv2.CascadeClassifier(self.base_path + self.paintbucket + ".xml")
        wrap_clsfr = cv2.CascadeClassifier(self.base_path + self.wrap + ".xml")
        wrench_clsfr = cv2.CascadeClassifier(self.base_path + self.wrench + ".xml")
        pencil_clsfr = cv2.CascadeClassifier(self.base_path + self.pencil + ".xml")

        threshold_hammer = threshold_ruler = threshold_paintbucket = threshold_wrap = threshold_wrench = threshold_pencil = 0

        while not is_found:
            # get capture frames
            ret, frame = video_capture.read()
            # converting the color image to a gray scale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # detecting in the gray scale
            hammers = hammer_clsfr.detectMultiScale(gray)
            rulers = ruler_clsfr.detectMultiScale(gray)
            paintbuckets = paintbucket_clsfr.detectMultiScale(gray)
            wraps = wrap_clsfr.detectMultiScale(gray)
            wrenches = wrench_clsfr.detectMultiScale(gray)
            pencils = pencil_clsfr.detectMultiScale(gray)

            if len(hammers > 1):
                threshold_hammer += len(hammers)
                logging.info("saw some hammers")

            if len(rulers > 1):
                threshold_ruler += len(rulers)
                logging.info("saw some rulers")

            if len(paintbuckets > 1):
                threshold_paintbucket += len(paintbuckets)
                logging.info("saw some paintbuckets")

            if len(wraps > 1):
                threshold_wrap += len(wraps)
                logging.info("saw some wraps")

            if len(wrenches > 1):
                threshold_wrench += len(wrenches)
                logging.info("saw some wrenches")

            if len(pencils > 1):
                threshold_pencil += len(pencils)
                logging.info("saw some pencils")

            if threshold_hammer >= self.threshold:
                is_found = True
                found_object = self.hammer
                position_x, position_y, w, h = hammers[0]
                logging.info("finally, it must be the hammer")

            if threshold_ruler >= self.threshold:
                is_found = True
                found_object = self.ruler
                position_x, position_y, w, h = rulers[0]
                logging.info("finally, it must be the ruler")

            if threshold_paintbucket >= self.threshold:
                is_found = True
                found_object = self.paintbucket
                position_x, position_y, w, h = paintbuckets[0]
                logging.info("finally, it must be the paintbucket")

            if threshold_wrap >= self.threshold:
                is_found = True
                found_object = self.wrap
                position_x, position_y, w, h = wraps[0]
                logging.info("finally, it must be the wrap")

            if threshold_wrench >= self.threshold:
                is_found = True
                found_object = self.wrench
                position_x, position_y, w, h = wrenches[0]
                logging.info("finally, it must be the wrench")

            if threshold_pencil >= self.threshold:
                is_found = True
                found_object = self.pencil
                position_x, position_y, w, h = pencils[0]
                logging.info("finally, it must be the pencil")

            logging.info("nothing found, try again..")

        return is_found, found_object, position_x, position_y
