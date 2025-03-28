import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/galaxy.jpg', flags=cv2.IMREAD_GRAYSCALE)
# img_opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
img_black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# cv2.imshow('TopHat', img_opened - img)
cv2.imshow('TopHat ex', img_top_hat)
cv2.imshow('Black ex', img_black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
