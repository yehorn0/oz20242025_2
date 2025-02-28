import cv2

img = cv2.imread("data/dogs.jpeg")


x1, y1 = 50, 100
x2, y2 = 250, 300

cropped_img = img[y1:y2, x1:y2]

cv2.imshow("Image", img)
cv2.imshow("Cropped", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
