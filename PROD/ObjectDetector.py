# TODO: create test class
import cv2


class ObjectDetector:

    def __init__(self):
        print("create new object detector")

    def find_pictogram_start_platform(self, video_capture):
        print("find pictogram start platform")
        is_found, found_pictogram, position_x, position_y = self._do_haar_cascade(video_capture)
        return is_found, found_pictogram

    def find_pictogram_target_platform(self, video_capture):
        print("find pictogram target platform")
        is_found, found_pictogram, position_x, position_y = self._do_haar_cascade(video_capture)
        return is_found, found_pictogram, position_x, position_y

    # Below: private methods

    def _do_haar_cascade(self, video_capture):
        print("do haar cascade")
        # TODO: define haar cascade. Attributes is_found and found_object have to be assigned
        is_found = False
        found_object = None
        position_x = None
        position_y = None
        return is_found, found_object, position_x, position_y
