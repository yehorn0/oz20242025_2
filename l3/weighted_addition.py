import cv2

img1 = cv2.imread('data/dogs.jpeg')
img2 = cv2.imread('data/cats.jpeg')

result = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
