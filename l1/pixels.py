import cv2

img = cv2.imread("data/dogs.jpeg")

pixel_value = img[55, 50]

print(pixel_value)

img[55, 50] = 0

print(pixel_value)