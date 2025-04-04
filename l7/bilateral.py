import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')

filtered_img_200 = cv2.bilateralFilter(img, 5, sigmaColor=500, sigmaSpace=500)
filtered_img_50 = cv2.bilateralFilter(img, 5, sigmaColor=50, sigmaSpace=50)

cv2.imshow('Original', img)
cv2.imshow('Filtered 200', filtered_img_200)
cv2.imshow('Filtered 50', filtered_img_50)
cv2.waitKey(0)
cv2.destroyAllWindows()
