import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/l5_dilation.png', flags=cv2.IMREAD_GRAYSCALE)

img_eroded = cv2.erode(img, kernel, iterations=1)
img_opened = cv2.dilate(img_eroded, kernel, iterations=5)

cv2.imshow('Eroded', img_eroded)
cv2.imshow('Opened', img_opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
