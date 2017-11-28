import numpy as np
import cv2
from random import randint



img = cv2.imread("fuzzy.png",1)
# bw = cv2.imread('fuzzy.png', 0)

thresholdValue = 45 #min = 0 max = 255

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

blur = cv2.GaussianBlur(gray, (3, 3), 0)

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205 , 1)

cv2.imshow("cv threshold", thresh)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print (len(contours))

filtrered = []

for c in contours:
    if cv2.contourArea(c) < 1000:continue
    filtrered.append(c)

print (len(filtrered))

index = -1
thickness = 4

objects = np.zeros([img.shape[0], img.shape[1],3], 'uint8')

color1 = (255, 255, 255)

for c in filtrered:

    color = (randint(0, 255), randint(0, 255), randint(0, 255))

    cv2.drawContours(objects, [c], -1, color, -1)

    cv2.drawContours(objects, c, index, color1, thickness)

    area = cv2.contourArea(c)

    perimeter = cv2.arcLength(c, True)

    M = cv2.moments(c)

    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        cx, cy = 0, 0

    cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)

    print ("Area: {}, perimeter: {}".format(area, perimeter))


cv2.imshow("Contours",objects)


cv2.waitKey(0)
cv2.destroyAllWindows()


