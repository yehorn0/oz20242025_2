import cv2
from functools import partial
import matplotlib.pyplot as plt


img = cv2.imread('data/house.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)

v_eq = cv2.equalizeHist(v)

img_hsv_eq = cv2.merge((h, s, v_eq))
img_eq = cv2.cvtColor(img_hsv_eq, cv2.COLOR_HSV2BGR)

# cv2.imshow('original', img)
# cv2.imshow('equalized', img_eq)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
histSize = 256
ranges = [0, 256]
hist_256_bin = partial(
    cv2.calcHist,
    channels=[0],
    mask=None,
    histSize=[histSize],
    ranges=ranges
)


def plot_hist(img) -> None:
    b, g, r = cv2.split(img)

    b_hist, g_hist, r_hist = hist_256_bin([b]), hist_256_bin([g]), hist_256_bin([r])

    for hist, color in zip((b_hist, g_hist, r_hist), ['b', 'g', 'r']):
        plt.plot(hist, color=color)


plot_hist(img_eq)
plt.xlim(ranges)
plt.show()
