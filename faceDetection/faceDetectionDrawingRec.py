import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

path = "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(path)


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors = 8, minSize= (45, 45))

print (len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


cv2.imshow("faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()