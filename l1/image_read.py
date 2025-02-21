import cv2

#cv2.IMREAD_GRAYSCALE
#cv2.IMREAD_UNCHANGED
img = cv2.imread("data/dogs.jpeg", flags=cv2.IMREAD_GRAYSCALE)


cv2.imwrite("data/dogs_grayscale.jpg", img)


# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
