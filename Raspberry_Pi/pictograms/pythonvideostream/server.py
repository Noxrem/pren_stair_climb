import io
import socket
import struct
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as pl

server_socket = socket.socket()
server_socket.bind(('192.168.137.38', 8000))  # ADD IP HERE
server_socket.listen(0)

# Accept a single connection and make a file-like object out of it
connection = server_socket.accept()[0].makefile('rb')

# loading the cascade classifier
# hammer = "hammer"
# ruler = "ruler"
# hammer_path = "/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training/hammer/cascade.xml"
# ruler_path = "/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training/ruler/cascade.xml"
hammer = "hammer"
ruler = "ruler"
paintbucket = "paintbucket"
pencil = "pencil"
wrap = "wrap"
wrench = "wrench"

base_path ="/Users/stofers/Development/HSLU/PREN/pren_stair_climb/Raspberry_Pi/pictograms/training/"

hammer_clsfr=cv2.CascadeClassifier(base_path+hammer+"/cascade.xml")
ruler_clsfr=cv2.CascadeClassifier(base_path+ruler+"/cascade.xml")
paintbucket_clsfr=cv2.CascadeClassifier(base_path+paintbucket+"/cascade.xml")
pencil_clsfr=cv2.CascadeClassifier(base_path+pencil+"/cascade.xml")
wrap_clsfr=cv2.CascadeClassifier(base_path+wrap+"/cascade.xml")
wrench_clsfr=cv2.CascadeClassifier(base_path+wrench+"/cascade.xml")

#item_clsfr = cv2.CascadeClassifier("../" + classifier + "/cascade.xml")
#hammer_clsfr = cv2.CascadeClassifier(hammer_path)
#ruler_clsfr = cv2.CascadeClassifier(ruler_path)
try:
    img = None
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the
        # length is zero, quit the loop
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        #image = cv2.imread(image_stream)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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

        if img is None:
            img = pl.imshow(image)
        else:
            img.set_data(image)

        pl.pause(0.01)
        pl.draw()

        #print('Image is ' % image.data)
        #image.verify()
        print('Got Image')
finally:
    connection.close()
    server_socket.close()