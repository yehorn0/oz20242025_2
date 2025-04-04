import cv2
import numpy as np
import matplotlib.pyplot as plt

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bin_range = [0, 256]

hist_one = cv2.calcHist(
    [gray_img],
    [0],
    None,
    [256],
    bin_range
)

hist_two = cv2.calcHist(
    [gray_img],
    [0],
    None,
    [10],
    bin_range
)

# print(hist_one.shape)
#
# cv2.imshow('histogram', hist_one)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
_, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))


axes[0].plot(hist_one)
axes[0].set_xlim(bin_range)
axes[0].set_title('Histogram 256 bins')
axes[0].set_xlabel('Bin')
axes[0].set_ylabel('Quantity')

axes[1].plot(hist_two)
axes[0].set_title('Histogram 10 bins')
axes[1].set_xlim([0, 9])
axes[1].set_xlabel('Bin')
axes[1].set_ylabel('Quantity')

plt.show()
