import cv2

img_bgr = cv2.imread('data/cats.jpeg')

img_grayscale = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)


cv2.imshow('Original', img_bgr)
cv2.imshow('GrayScale', img_grayscale)
# gs = 0.114 * Blue + 0.587 * Green + 0.2989 * Red
cv2.imshow('HSV', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

