import time
import datetime
import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

recColor = (0, 255, 0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if (len(faces) > 0):
        print (len(faces))

    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0

    for (_x, _y, _w, _h) in faces:
        if _w * _h > maxArea:
            x = _x
            y = _y
            w = _w
            h = _h
            maxArea = w * h

        # If one or more faces are found, draw a rectangle around the
        # largest face present in the picture
        if maxArea > 0:
            cv2.rectangle(frame, (x - 10, y - 20),
                          (x + w + 10, y + h + 20),
                          recColor, 2)

    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     # print("points are: {}, {}, {}, {} \n".format(x, y, w, h))
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()