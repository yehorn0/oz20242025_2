import cv2
import numpy as np

kernel = np.ones((3, 3), np.uint8)

img = cv2.imread('data/l6_gradient.png', flags=cv2.IMREAD_GRAYSCALE)

img_eroded = cv2.erode(img, kernel, iterations=1)
img_dilated = cv2.dilate(img, kernel, iterations=1)
gradient = img_dilated - img_eroded

gradient_ex = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# cv2.imshow('Eroded', img_eroded)
# cv2.imshow('Dilated', img_dilated)
cv2.imshow('Gradient', gradient)
cv2.imshow('Gradient Ex', gradient_ex)
cv2.waitKey(0)
cv2.destroyAllWindows()
