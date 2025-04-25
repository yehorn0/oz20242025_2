# CLAHE
# Contrast Limited Adaptive Histogram Equalization
import cv2

img = cv2.imread('data/l9_0.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe_2_8_8 = cv2.createCLAHE(clipLimit=2., tileGridSize=(8, 8))
clahe_40_8_8 = cv2.createCLAHE(clipLimit=40, tileGridSize=(8, 8))
clahe_2_24_24 = cv2.createCLAHE(clipLimit=2, tileGridSize=(24, 24))

clahe_imgs = [
    clahe_2_8_8.apply(gray_img),
    clahe_40_8_8.apply(gray_img),
    clahe_2_24_24.apply(gray_img)
]

equalized = cv2.equalizeHist(gray_img)

for title, clahe_img in zip(["2_8_8", "40_8_8", "2_24_24"], clahe_imgs):
    cv2.imshow(f'clahe {title}', clahe_img)

cv2.imshow('equalized', equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
