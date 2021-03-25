import Camera


# TODO: create test class

class ObjectDetector:
    camera = None
    video = None

    def __init__(self):
        print("create new stair detector")
        self.camera = Camera.Camera()
        self.video = self.camera.cam


    def find_pictogram(self):
        print("find pictogram")
        is_found, found_pictogram, position = self.do_haar_cascade()
        return is_found, found_pictogram

    def do_haar_cascade(self):
        print("do haar cascade")
        # TODO: define haar cascade. Attributes is_found and found_object have to be assigned
        is_found = None
        found_object = None
        position = None
        return is_found, found_object, position
