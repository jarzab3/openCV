import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = "haarcascade_eye.xml"

eyes_cascade = cv2.CascadeClassifier(path)


eyes = eyes_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors = 20, minSize= (10, 10))

print (len(eyes))

# print (eyes[1])
# print (eyes[2])
# print (eyes[3])

for (x, y, w, h) in eyes:
    cv2.circle(img, (x + int(w/2), y + int(h/2)), 8, (0, 255, 0), 2)

cv2.namedWindow("faces",cv2.WINDOW_NORMAL)

cv2.imshow("faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()