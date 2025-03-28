import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')

blurred_3 = cv2.blur(img, (3, 3))
blurred_7 = cv2.blur(img, (7, 7))
blurred_17 = cv2.blur(img, (17, 17))

cv2.imshow('Blurred (3, 3)', blurred_3)
cv2.imshow('Blurred (7, 7)', blurred_7)
cv2.imshow('Blurred (17, 17)', blurred_17)
cv2.waitKey(0)
cv2.destroyAllWindows()
