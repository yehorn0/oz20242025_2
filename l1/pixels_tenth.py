import cv2

img = cv2.imread("data/dogs.jpeg")

print(img.shape)

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        if col % 10 == 0:
            img[row, col] = [0, 255, 0]
        if row % 15 == 0:
            img[row, col] = [255, 0, 0]

cv2.imshow("Changed", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
# pixel_value = img[55, 50]
#
# print(pixel_value)
#
# img[55, 50] = 0
#
# print(pixel_value)