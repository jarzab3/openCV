import numpy as np
import cv2

bw = cv2.imread('detect_blob.png', 0)
# bw = cv2.imread('fuzzy.png', 0)

heigh, width = bw.shape[0:2]

cv2.imshow("original BW", bw)

binary = np.zeros([heigh, width, 1], 'uint8')

thresholdValue = 85 #min = 0 max = 255

for row in range(0, heigh):
    for col in range(0, width):
        if bw[row][col] > thresholdValue:
            binary[row][col] = 255


cv2.imshow("slow binary", binary)

ret, thresholdValue = cv2.threshold(bw, thresholdValue, 255, cv2.THRESH_BINARY)

cv2.imshow("cv threshold", thresholdValue)

cv2.waitKey(0)

cv2.destroyAllWindows()


