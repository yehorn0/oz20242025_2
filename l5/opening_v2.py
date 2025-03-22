import cv2
import numpy as np

shape = (256, 700)
img = np.zeros(shape, np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "TEST OPENING", (15, 125), font, 3, (255, 255, 255), 15)

noise = np.zeros(shape, np.uint8)
cv2.randn(noise, 0, 100)

img_noisy = noise + img
kernel = np.ones((3, 3), np.uint8)

img_eroded = cv2.erode(img_noisy, kernel, iterations=1)
img_opened = cv2.dilate(img_eroded, kernel, iterations=1)

cv2.imshow('Noisy', img_noisy)
cv2.imshow('Eroded', img_eroded)
cv2.imshow('Opened', img_opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
