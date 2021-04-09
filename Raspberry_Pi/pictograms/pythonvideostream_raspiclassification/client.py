import io
import socket
import struct
import time
import picamera
import cv2

client_socket = socket.socket()

client_socket.connect(('192.168.0.18', 8000))  # ADD IP HERE
#client_socket.connect(('192.168.137.38', 8000))manus ip

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')

hammer = "hammer"
ruler = "ruler"
paintbucket = "paintbucket"
pencil = "pencil"
wrap = "wrap"
wrench = "wrench"

base_path = "../cascades/"

hammer_clsfr = cv2.CascadeClassifier(base_path + hammer + ".xml")
ruler_clsfr = cv2.CascadeClassifier(base_path + ruler + ".xml")
paintbucket_clsfr = cv2.CascadeClassifier(base_path + paintbucket + ".xml")
pencil_clsfr = cv2.CascadeClassifier(base_path + pencil + ".xml")
wrap_clsfr = cv2.CascadeClassifier(base_path + wrap + ".xml")
wrench_clsfr = cv2.CascadeClassifier(base_path + wrench + ".xml")

try:
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

        ret, buffer = cv2.imencode('.jpg',img)
        stream = io.BytesIO()
        # Write the length of the capture to the stream and flush to
        # ensure it actually gets sent
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()
        # Rewind the stream and send the image data over the wire
        stream.seek(0)
        connection.write(stream.read())
        # If we've been capturing for more than 30 seconds, quit
        if time.time() - start > 600:
            break
        # Reset the stream for the next capture
        stream.seek(0)
        stream.truncate()
    # Write a length of zero to the stream to signal we're done
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()