import cv2
import matplotlib.pyplot as plt

img = cv2.imread('data/l9_0.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
equalized = cv2.equalizeHist(gray_img)

hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])


# cv2.imshow('original', gray_img)
# cv2.imshow('equalized', equalized)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.plot(hist, color="blue")
plt.fill_between(range(len(hist)), hist.flatten(), color="blue")
plt.plot(hist_equalized, color="green")
plt.xlim([0, 256])
plt.show()


