import numpy as np


def manual_equalize_hist(gray_img: np.ndarray) -> np.ndarray:
    hist, _ = np.histogram(gray_img.flatten(), bins=256, range=(0., 256.))

    # n = [0, 10, 15, 2, 3] => cumul sum = [0, 10, 25, 27, 30]
    # cdf = np.copy(gray_img.flatten())
    # current_sum = 0
    # for idx, h in enumerate(cdf):
    #     current_sum += h
    #     cdf[idx] = current_sum
    # reduce -> [0, 10, 15, 2, 3], sum -> 30

    cdf = hist.cumsum()
    cdf_normalized = cdf / cdf[-1]

    equalized = np.floor(255. * cdf_normalized[gray_img]).astype(np.uint8)

    return equalized


if __name__ == '__main__':
    import cv2
    import matplotlib.pyplot as plt

    img = cv2.imread('data/l9_0.jpg')

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized_cv2 = cv2.equalizeHist(gray_img)
    equalized = manual_equalize_hist(gray_img)

    hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])
    hist_equalized_cv2 = cv2.calcHist([equalized_cv2], [0], None, [256], [0, 256])
    plt.plot(hist_equalized_cv2, color="blue")
    # plt.fill_between(range(len(hist)), hist.flatten(), color="blue")
    plt.plot(hist_equalized, color="green")
    plt.xlim([0, 256])
    plt.show()
    # cv2.imshow('original', gray_img)
    # cv2.imshow('equalized', equalized)
    # cv2.imshow('equalized cv2', equalized_cv2)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # print(np.allclose(equalized, equalized_cv2))

