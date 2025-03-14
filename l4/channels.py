import cv2

img = cv2.imread('data/cats.jpeg')

img_red = img.copy()
img_green = img.copy()
img_blue = img.copy()

print(img.shape)  # (843, 1280, 3)
img_red[:, :, 0] = 0
img_red[:, :, 1] = 0

img_green[:, :, 0] = 0
img_green[:, :, 2] = 0

img_blue[:, :, 1] = 0
img_blue[:, :, 2] = 0

cv2.imshow('Original', img)
cv2.imshow('Red', img_red)
cv2.imshow('Green', img_green)
cv2.imshow('Blue', img_blue)
cv2.waitKey(0)
cv2.destroyAllWindows()

