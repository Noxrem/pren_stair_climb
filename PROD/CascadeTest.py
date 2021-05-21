import cv2
from picamera.array import PiRGBArray

hammer = "hammer"
ruler = "ruler"
paintbucket = "paintbucket"
pencil = "pencil"
wrap = "wrap"
wrench = "wrench"

hammer_clsfr = cv2.CascadeClassifier("/cascades/alt/hammer.xml")
ruler_clsfr = cv2.CascadeClassifier("/cascades/alt/ruler.xml")
paintbucket_clsfr = cv2.CascadeClassifier("/cascades/alt/paintbuckeet.xml")
pencil_clsfr = cv2.CascadeClassifier("/cascades/alt/pencil.xml")
wrap_clsfr = cv2.CascadeClassifier("/cascades/alt/wrap.xml")

frameWidth = 640
frameHeight = 480
# loading the cascade classifier

camera = cv2.VideoCapture(0)
# initializing the video object (0 for default webcam)
#camera.set(3, frameWidth)
#camera.set(4, frameHeight)


def empty(a):
    pass


# CREATE TRACKBAR
#cv2.namedWindow("Result")
#cv2.resizeWindow("Result", frameWidth, frameHeight + 100)
#cv2.createTrackbar("Scale", "Result", 150, 1000, empty)
#cv2.createTrackbar("Neighbor", "Result", 3, 50, empty)
#cv2.createTrackbar("Min Area", "Result", 400, 100000, empty)
#cv2.createTrackbar("Brightness", "Result", 100, 255, empty)
# cv2.createTrackbar("BinaryThreshold", "Result", 123, 255, empty)

while (True):
    # infinite loop to read continuous frames from the camera object
    # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
    #cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
    # binaryThreshold = cv2.getTrackbarPos("BinaryThreshold", "Result")
    #camera.set(10, cameraBrightness)
    # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE

    ret, img = camera.read()
    # reading a single frame from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # converting the color image to a gray scale image

    # ret, thresh1 = cv2.threshold(gray, binaryThreshold, 255, cv2.THRESH_BINARY)
    # DETECT THE OBJECT USING THE CASCADE
    scaleVal = 1.15 #+ (cv2.getTrackbarPos("Scale", "Result") / 1000)
    neighbor = 3 #cv2.getTrackbarPos("Neighbor", "Result")

    hammers = hammer_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    rulers = ruler_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    paintbuckets = paintbucket_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    pencils = pencil_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    wraps = wrap_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    # wrenchs=wrench_clsfr.detectMultiScale(gray, scaleVal, neighbor)
    # detecting in the gray scale
    # hammers is a 2D array contaning n number of rows (n= number of hammers in the frame), 4 columns (x,y,w,h)
    for (x, y, w, h) in hammers:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, hammer, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    for (x, y, w, h) in rulers:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, ruler, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    for (x, y, w, h) in paintbuckets:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, paintbucket, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    for (x, y, w, h) in pencils:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, pencil, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    for (x, y, w, h) in wraps:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, wrap, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # for (x,y,w,h) in wrenchs:
    # #going through each and assigning the x,y,w,h
    #
    #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    #     #Drawing a rectangle bounding the faces
    #     cv2.putText(img,wrench,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    cv2.imshow('LIVE', img)
    cv2.waitKey(1)
    # showing the frame