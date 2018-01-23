import cv2
import numpy as np

# If need to read as gray add 0 to imread function
e1 = cv2.getTickCount()
# your code execution

img = cv2.imread('../trainData/grayImage.png', 0)
img1 = cv2.imread('../trainData/colorImage.png')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)
print(img1.shape)

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print("Time taken: {}".format(time))
while 1:

    cv2.imshow('frame', img)
    cv2.imshow('frame1', img1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

