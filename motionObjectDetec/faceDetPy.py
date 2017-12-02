import time
import datetime
import cv2
import threading
import sys

# make this work with Python2 or Python3
# if sys.version_info[0] < 3:
#     input = raw_input

class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval=0.001):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False
    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.interval
    def peek(self):
        '''
        return the current value
        '''
        return self.value
    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value
# create the class instance
count = SecondCounter()
# start the count


# test the counter with a key board response time
# or put your own code you want to background-time in here
# you can always peek at the current counter value
# e = input("Press Enter")
# e = input("Press Enter again")
# stop the count and get elapsed time

# count.start()
# seconds = count.finish()
# print("You took {} seconds between Enter actions".format(seconds))

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

called = False

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

    if (len(faces) > 0):
        start = time.time()
        while(len(faces) > 0):
            end = time.time()
            diff = end - start
            # elapsedToPrint = time.strftime("%H:%M:%S", time.gmtime(end - start))
            elapsed = datetime.timedelta(seconds=diff)
            print("The face was detected for: {}".format(elapsed))

            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        else:
            print ("Added to total time")
            totalObservationTime = totalObservationTime + elapsed

    # elif (len(faces) < 1):
        # print ("Not detected")


    cv2.imshow('Video', frame)


        # Draw a rectangle around the faces
        # for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        print (str(totalObservationTime))
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()