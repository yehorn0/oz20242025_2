import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('data/house.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(img)


mask[300:900, 500:1100] = 255

masked_image = cv2.bitwise_and(img, mask)
masked_once_again = cv2.bitwise_and(img, masked_image)

# print(masked_image == masked_once_again) True

hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_masked = cv2.calcHist([img], [0], mask, [256], [0, 256])
hist_masked_v2 = cv2.calcHist([img], [0], masked_image, [256], [0, 256])


plt.plot(hist_full, color="b")
plt.plot(hist_masked, color="g")
# plt.plot(hist_masked_v2, color="r")
plt.xlim([0, 256])

plt.show()
