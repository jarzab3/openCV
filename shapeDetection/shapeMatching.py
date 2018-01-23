import cv2
import numpy as np

img = cv2.imread('star.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

_, contours, hierarchy= cv2.findContours(thresh, 2, 1)

cnt = contours[0]

# print(cnt)

hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)

# img = cv2.drawContours(img, contours, -1, (0,255,0), 3)


# cnt = contours[4]

# img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

# points = cv2.CHAIN_APPROX_SIMPLE(img1)
#
# imgray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#
# ret,thresh = cv2.threshold(imgray,127,255,0)
#
# contours, hierarchy, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)

    cv2.circle(img, far, 5, [0, 0, 255], -1)


# cv2.namedWindow('Image to compare',cv2.WINDOW_NORMAL)
# cv2.imshow('Image to compare', img)


# Image comparison

imgTemplate = cv2.imread('red-car-top-view.png', 0)
imgToCompare = cv2.imread('carToCompare.png', 0)

retTemplate, threshTemplate = cv2.threshold(imgTemplate, 127, 255, 0)
retToComapre, threshToCompare = cv2.threshold(imgToCompare, 127, 255, 0)

_, contoursTemplate, hierarchy = cv2.findContours(threshTemplate, 2, 1)
_, contoursToCompare, hierarchy1 = cv2.findContours(threshToCompare, 2, 1)


cntTemplate = contoursTemplate[0]
cntToComapre = contoursToCompare[0]


# cnt = contours[4]

# img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

imgTemplate = cv2.drawContours(imgTemplate, cntTemplate, -1, (0,255,0), 3)

ret = cv2.matchShapes(cntToComapre, cntTemplate, 1, 0.0)

print(ret)

# Display these images
cv2.namedWindow('Template',cv2.WINDOW_NORMAL)
cv2.imshow('Template', imgTemplate)

cv2.namedWindow('To Compare',cv2.WINDOW_NORMAL)
cv2.imshow('To Compare', imgToCompare)



cv2.waitKey(0)
cv2.destroyAllWindows()