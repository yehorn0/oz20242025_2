import numpy as np
import cv2


canvas = np.zeros((640, 480, 3), dtype=np.uint8)

p1 = (100, 250)
p2 = (150, 400)
p3 = (200, 350)

cv2.line(canvas, p1, p2, (0, 255, 0), 3)
cv2.line(canvas, p1, p3, (255, 0, 0), 9)
cv2.line(canvas, p3, p2, (0, 0, 255), 15)

cv2.imshow("Triangle", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
