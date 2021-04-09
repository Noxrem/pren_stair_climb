# TODO: create test class
import cv2


class ObjectDetector:
    base_path = "cascades/"
    hammer = "hammer"
    ruler = "ruler"
    paintbucket = "paintbucket"
    pencil = "pencil"
    wrap = "wrap"
    wrench = "wrench"

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

    def _init_haar_cascades(self):

        for cascade in base_path:
            print(cascade)
        hammer_clsfr = cv2.CascadeClassifier(base_path + hammer + ".xml")
        ruler_clsfr = cv2.CascadeClassifier(base_path + ruler + ".xml")
        paintbucket_clsfr = cv2.CascadeClassifier(base_path + paintbucket + ".xml")
        pencil_clsfr = cv2.CascadeClassifier(base_path + pencil + ".xml")
        wrap_clsfr = cv2.CascadeClassifier(base_path + wrap + ".xml")
        wrench_clsfr = cv2.CascadeClassifier(base_path + wrench + ".xml")






base_path ="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training/"



#item_clsfr = cv2.CascadeClassifier("../" + classifier + "/cascade.xml")
#hammer_clsfr = cv2.CascadeClassifier(hammer_path)
#ruler_clsfr = cv2.CascadeClassifier(ruler_path)
try:
    img = None
    while True:
        camera = picamera.PiCamera()
        camera.vflip = True
        camera.hflip = True
        camera.resolution = (640, 480)
        camera.iso = 100
        # Start a preview and let the camera warm up for 2 seconds
        camera.start_preview()
        time.sleep(2)

        # Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
        start = time.time()
        while (True):
            # infinite loop to read continuous frames from the camera object

            ret, img = camera.read()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # converting the color image to a gray scale image
        hammers = hammer_clsfr.detectMultiScale(gray)
        rulers = ruler_clsfr.detectMultiScale(gray)
        paintbuckets = paintbucket_clsfr.detectMultiScale(gray)
        pencils = pencil_clsfr.detectMultiScale(gray)
        wraps = wrap_clsfr.detectMultiScale(gray)
        wrenchs = wrench_clsfr.detectMultiScale(gray)
        # detecting in the gray scale
        # hammers is a 2D array contaning n number of rows (n= number of hammers in the frame), 4 columns (x,y,w,h)
        for (x, y, w, h) in hammers:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, hammer, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for (x, y, w, h) in rulers:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, ruler, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        for (x, y, w, h) in paintbuckets:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, paintbucket, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        for (x, y, w, h) in pencils:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, pencil, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        for (x, y, w, h) in wraps:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, wrap, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        for (x, y, w, h) in wrenchs:
            # going through each and assigning the x,y,w,h

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Drawing a rectangle bounding the faces
            cv2.putText(image, wrench, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)