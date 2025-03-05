import numpy as np
import cv2

img1 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]], dtype=np.uint8)
img2 = np.array([[100, 200, 150],
                 [50, 250, 100],
                 [150, 200, 50]], dtype=np.uint8)

cv2_substract = cv2.subtract(img1, img2)
print("cv2_substract() result:\n", cv2_substract)

numpy_add = img1 - img2
print("Numpy substraction result:\n", numpy_add)
