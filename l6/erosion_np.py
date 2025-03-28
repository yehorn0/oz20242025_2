import cv2
import numpy as np


def custom_erode(img: np.ndarray, kernel: np.ndarray, iterations: int = 1) -> np.ndarray:
    k_h, k_w = kernel.shape
    pad_h, pad_w = k_h // 2, k_w // 2

    output = img.copy()

    for _ in range(iterations):
        padded_img = np.pad(
            output,
            ((pad_h, pad_h), (pad_w, pad_w)),
            mode="constant"
        )

        new_image = np.zeros_like(output)

        for i in range(output.shape[0]):
            for j in range(output.shape[1]):
                region = padded_img[i:i + k_h, j:j + k_w]

                if np.all(region[kernel == 1] == 255):
                    new_image[i, j] = 255
                else:
                    new_image[i, j] = np.min(region[kernel == 1])

        output = new_image.copy()

    return output


if __name__ == '__main__':
    kernel = np.ones((3, 3), np.uint8)

    img = cv2.imread('data/l5_erosion.png', flags=cv2.IMREAD_GRAYSCALE)

    eroded = custom_erode(img, kernel)

    cv2.imshow('Eroded', eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
