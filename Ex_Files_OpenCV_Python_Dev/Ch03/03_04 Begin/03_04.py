import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h,s,v), axis=1)


ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)

final = cv2.bitwise_and(min_sat, max_hue)




cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.namedWindow("satFilter", cv2.WINDOW_NORMAL)
cv2.namedWindow("final", cv2.WINDOW_NORMAL)
cv2.namedWindow("max_hue", cv2.WINDOW_NORMAL)

cv2.imshow("output", hsv_split)
cv2.imshow("satFilter", min_sat)
cv2.imshow("final", final)
cv2.imshow("max_hue", max_hue)

# img_stretch = cv2.resize(hsv_split, (1200, 800))
# cv2.imshow("hsv split", img_stretch)

cv2.waitKey(0)
cv2.destroyAllWindows()