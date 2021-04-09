import cv2

hammer = "hammer"
ruler = "ruler"
paintbucket = "paintbucket"
pencil = "pencil"
wrap = "wrap"
wrench = "wrench"
hammer_clsfr = cv2.CascadeClassifier("../training/" + hammer + "/cascade.xml")
ruler_clsfr = cv2.CascadeClassifier("../training/" + ruler + "/cascade.xml")
paintbucket_clsfr = cv2.CascadeClassifier("../training/" + paintbucket + "/cascade.xml")
pencil_clsfr = cv2.CascadeClassifier("../training/" + pencil + "/cascade.xml")
wrap_clsfr = cv2.CascadeClassifier("../training/" + wrap + "/cascade.xml")
wrench_clsfr = cv2.CascadeClassifier("../training/" + wrench + "/cascade.xml")
# loading the cascade classifier

camera = cv2.VideoCapture(0)
# initializing the video object (0 for default webcam)

while (True):
    # infinite loop to read continuous frames from the camera object

    ret, img = camera.read()
    # reading a single frame from the camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
    for (x, y, w, h) in wrenchs:
        # going through each and assigning the x,y,w,h

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Drawing a rectangle bounding the faces
        cv2.putText(img, wrench, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('LIVE', img)
    cv2.waitKey(1)
    # showing the frame