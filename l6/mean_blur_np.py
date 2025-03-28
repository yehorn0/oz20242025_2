import cv2
import numpy as np


def average_blur(image: np.ndarray, kernel_size: tuple[int, int]) -> np.ndarray:
    output = img.copy()

    """
    Insert your code here
    """

    return output


if __name__ == '__main__':
    img = cv2.imread('data/house.jpg')

    blured = average_blur(img, (3, 3))

    cv2.imshow('Blured', blured)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
