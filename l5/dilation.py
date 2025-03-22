import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/l5_dilation.png', flags=cv2.IMREAD_GRAYSCALE)

img_dilated = cv2.dilate(img, kernel, iterations=1)
img_dilated_5_times = cv2.dilate(img, kernel, iterations=5)

cv2.imshow('Dilated', img_dilated_5_times)
cv2.waitKey(0)
cv2.destroyAllWindows()
