import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

shape = (256, 700)
img = np.zeros(shape, np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "TEST OPENING", (15, 125), font, 3, (255, 255, 255), 15)

noise = np.zeros(shape, np.uint8)
cv2.randn(noise, 0, 100)

img_noisy = noise + img


img_opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('Opened', img_opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
