import numpy as np
import cv2
import matplotlib.pyplot as plt


def calc_hist_np(
        image: np.ndarray,
        bins: int = 256,
        range_: tuple[int, int] = (0, 256),
        mask: np.ndarray | None = None,
) -> np.ndarray:
    hist = np.zeros(bins, dtype=int)

    bin_size = (range_[1] - range_[0]) / bins

    h, w = image.shape

    for y in range(h):
        for x in range(w):
            if mask is None or mask[y, x] == 255:
                bin_idx = int((image[y, x] - range_[0]) / bin_size)
                bin_idx = min(bin_idx, bins - 1)

                hist[bin_idx] += 1

    return hist


img = cv2.imread('data/house.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bins = 10
ranges = (0, 256)
mask = np.zeros_like(gray_img)
mask[300:900, 500:1100] = 255

hist_manual = calc_hist_np(gray_img, bins, ranges, mask)
hist_cv2 = cv2.calcHist([gray_img], [0], mask, [bins], ranges)

assert np.allclose(hist_manual, hist_cv2.flatten())

_, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

axes[0].plot(hist_manual)
axes[0].set_xlim([0, bins-1])
axes[0].set_title('Manual')
axes[0].set_xlabel('Bin')
axes[0].set_ylabel('Quantity')

axes[1].plot(hist_cv2)
axes[1].set_title('Cv2')
axes[1].set_xlim([0, bins-1])
axes[1].set_xlabel('Bin')
axes[1].set_ylabel('Quantity')

plt.show()
