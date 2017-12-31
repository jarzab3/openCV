import numpy as np
import cv2

cap = cv2.VideoCapture("motorway.mp4")

fgbg = cv2.createBackgroundSubtractorMOG2()

video_capture = cv2.VideoCapture(0)

while(1):
    ret, frame = video_capture.read()
    # ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()