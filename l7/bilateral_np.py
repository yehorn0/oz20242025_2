import numpy as np
import cv2
from math import exp, sqrt


def gaussian(x: float | np.ndarray, sigma: float) -> float | np.ndarray:
    return exp(-(x ** 2) / (2 * sigma ** 2))


def custom_bilateral_filter(
        img: np.ndarray,
        diameter: int,
        sigmaColor: float,
        sigmaSpace: float
):
    padded_img = np.pad(
        img.astype(np.float32),
        diameter // 2,
        mode="reflect"
    )
    filtered_img = np.zeros_like(img)

    radius = diameter // 2

    # M x N x d^2
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            i1 = i + radius
            j1 = j + radius

            wp_total = 0
            filtered_pixel = 0

            for k in range(-radius, radius + 1):
                for l in range(-radius, radius + 1):
                    neighbor_i = i1 + k
                    neighbor_j = j1 + k

                    gauss_space = gaussian(sqrt(k ** 2 + l ** 2), sigmaSpace)
                    gauss_color = gaussian(padded_img[neighbor_i, neighbor_j] - padded_img[i1, j1], sigmaColor)

                    w = gauss_color * gauss_space

                    filtered_pixel += padded_img[neighbor_i, neighbor_j] * w
                    wp_total += w

            filtered_img[i, j] = filtered_pixel / wp_total

    return filtered_img
# Cython


if __name__ == '__main__':
    shape = (256, 700)
    img = np.zeros(shape, np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "TEST OPENING", (15, 125), font, 3, (255, 255, 255), 15)

    noise = np.zeros(shape, np.uint8)
    cv2.randn(noise, 0, 100)

    img_noisy = noise + img

    filtered = custom_bilateral_filter(img, 5, 12, 12)

    cv2.imshow('Filtered', filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
