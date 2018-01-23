import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('../trainData/grayImage.png',0)


cap = cv2.VideoCapture('../trainData/droneVideoCars.mp4', 0)


while(cap.isOpened()):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(frame, 200, 300)


    cv2.namedWindow("Display Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Display Image", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()





# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()