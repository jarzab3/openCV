import time
import datetime
import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

called = False

def writeTotal(totalTime):
    with open("totalTime.txt", mode='w') as file:
        file.write('%s' %
                   (totalTime))

totalObservationTime = datetime.timedelta()

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

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    cv2.imshow('Video', frame)


    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()


# Tracking face

import dlib

#Create the tracker we will use
tracker = dlib.correlation_tracker()

#The variable we use to keep track of the fact whether we are
#currently using the dlib tracker
trackingFace = 0


#If we are not tracking a face, then try to detect one
if not trackingFace:

    #For the face detection, we need to make use of a gray
    #colored image so we will convert the baseImage to a
    #gray-based image
    gray = cv2.cvtColor(baseImage, cv2.COLOR_BGR2GRAY)
    #Now use the haar cascade detector to find all faces
    #in the image
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    #In the console we can show that only now we are
    #using the detector for a face
    print("Using the cascade detector to detect face")


    #For now, we are only interested in the 'largest'
    #face, and we determine this based on the largest
    #area of the found rectangle. First initialize the
    #required variables to 0
    maxArea = 0
    x = 0
    y = 0
    w = 0
    h = 0


    #Loop over all faces and check if the area for this
    #face is the largest so far
    #We need to convert it to int here because of the
    #requirement of the dlib tracker. If we omit the cast to
    #int here, you will get cast errors since the detector
    #returns numpy.int32 and the tracker requires an int
    for (_x,_y,_w,_h) in faces:
        if  _w*_h > maxArea:
            x = int(_x)
            y = int(_y)
            w = int(_w)
            h = int(_h)
            maxArea = w*h

    #If one or more faces are found, initialize the tracker
    #on the largest face in the picture
    if maxArea > 0 :

        #Initialize the tracker
        tracker.start_track(baseImage,
                            dlib.rectangle( x-10,
                                            y-20,
                                            x+w+10,
                                            y+h+20))

        #Set the indicator variable such that we know the
        #tracker is tracking a region in the image
        trackingFace = 1