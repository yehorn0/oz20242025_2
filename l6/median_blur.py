import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')

#blurred_3 = cv2.medianBlur(img, 3)
#blurred_7 = cv2.medianBlur(img, 7)
median_blurred_17 = cv2.medianBlur(img, 17)
blurred_17 = cv2.blur(img, (17, 17))

cv2.imshow('Blurred Median (17, 17)', median_blurred_17)
cv2.imshow('Blurred Mean (17, 17)', blurred_17)
cv2.waitKey(0)
cv2.destroyAllWindows()
