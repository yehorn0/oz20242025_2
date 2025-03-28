import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')

gauss_blurred_17 = cv2.GaussianBlur(img, (15, 15), 1.5)


cv2.imshow('Gauss Blur 5', gauss_blurred_17)
cv2.waitKey(0)
cv2.destroyAllWindows()
