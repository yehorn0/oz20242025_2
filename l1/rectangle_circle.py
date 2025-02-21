import numpy as np
import cv2


canvas = np.zeros((640, 480, 3), dtype=np.uint8)

upper_left = (100, 100)
bottom_right = (400, 300)

cv2.rectangle(canvas, upper_left, bottom_right, (255, 255, 0), 5)

center = (200, 200)
radius = 50

cv2.circle(canvas, center, radius, (0, 0, 255), 2)
cv2.circle(canvas, center, radius // 2, (0, 0, 255), -1)

cv2.imshow("Rectangle & Circle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
