import cv2
import numpy as np
import matplotlib.pyplot as plt

from functools import partial

kernel = np.ones((5, 5), np.uint8)

img = cv2.imread('data/house.jpg')

b, g, r = cv2.split(img)
histSize = 256
ranges = [0, 256]

hist_256_bin = partial(
    cv2.calcHist,
    channels=[0],
    mask=None,
    histSize=[histSize],
    ranges=ranges
)
b_hist, g_hist, r_hist = hist_256_bin([b]), hist_256_bin([g]), hist_256_bin([r])

for hist, color in zip((b_hist, g_hist, r_hist), ['b', 'g', 'r']):
    plt.plot(hist, color=color)

plt.xlim(ranges)

plt.show()
