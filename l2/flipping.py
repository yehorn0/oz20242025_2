import cv2

img = cv2.imread("data/dogs.jpeg")


flipped_x = cv2.flip(img, flipCode=0)
flipped_y = cv2.flip(img, flipCode=1)
flipped_both = cv2.flip(img, flipCode=-1)

cv2.imshow("Image", img)
cv2.imshow("x", flipped_x)
cv2.imshow("y", flipped_y)
cv2.imshow("xy", flipped_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
