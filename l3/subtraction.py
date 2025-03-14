import numpy as np
import cv2

img1 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]], dtype=np.uint8)
img2 = np.array([[100, 200, 150],
                 [50, 250, 100],
                 [150, 200, 50]], dtype=np.uint8)

cv2_subtract = cv2.subtract(img1, img2)
print("cv2_subtract() result:\n", cv2_subtract)

numpy_sub = img1 - img2
print("Numpy subtraction result:\n", numpy_sub)

img1 = cv2.imread('data/dogs.jpeg')
img2 = cv2.imread('data/cats.jpeg')

img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

result = cv2.subtract(img1, img2_resized)
result_weighted =  cv2.addWeighted(img1, 1., img2_resized, -1., 0)

cv2.imshow('Result', result)
cv2.imshow('Result Weighted', result_weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

