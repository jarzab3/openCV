import numpy as np
import cv2
import math

# Global variables
canvas = np.ones([500,500,3],'uint8')*255

colorRed = (255, 0, 0)
colorYellow = (255, 255, 0)
colorBlue = (0, 0, 255)

colorToPaint = colorRed
# click callback

pointStart = (0, 0)
pointEnd = (0, 0)
radius = 10

line_width = 3
drawing = False
distance = 0


def click(event, x, y, flags, param):

	global canvas, pointStart, pointEnd, radius, drawing, distance


	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		pointStart = (x, y)
		# cv2.circle(canvas, pointStart, radius, colorToPaint, line_width)

	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			pointEnd = (x, y)

			diff = (pointStart[0] - pointEnd[0]), (pointStart[1] - pointEnd[1])

			distance = math.sqrt(math.pow((pointEnd[0] -  pointStart[0]),2) + math.pow((pointEnd[1] - pointStart[1]),2))

			radius = int(distance)

			canvas = np.ones([500, 500, 3], 'uint8') * 255

			cv2.circle(canvas, pointStart, radius, colorToPaint, line_width)


	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		print(distance)

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop

while True:

	cv2.imshow("canvas",canvas)

	# key capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break
	elif ch & 0xFF == ord('r'):
		colorToPaint = colorRed
	elif ch & 0xFF == ord('b'):
		colorToPaint = colorBlue
	elif ch & 0xFF == ord('y'):
		colorToPaint = colorYellow


cv2.destroyAllWindows()




