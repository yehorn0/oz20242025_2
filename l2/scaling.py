import cv2

img = cv2.imread("data/dogs.jpeg")


resized_img_0 = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
resized_img_1 = cv2.resize(img, (640, 480), interpolation=cv2.INTER_CUBIC)

cv2.imshow("Image", img)
cv2.imshow("Resized 0", resized_img_0)
cv2.imshow("Resized 1", resized_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

