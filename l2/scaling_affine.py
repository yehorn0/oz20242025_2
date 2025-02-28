import cv2
import numpy as np

img = cv2.imread("data/dogs.jpeg")

new_size = (640, 480)

fx = new_size[0] / img.shape[1]
fy = new_size[1] / img.shape[0]

m = np.float32([[fx, 0., 0.], [0., fy, 0.]])

rows, cols, _ = img.shape

resized_image = cv2.warpAffine(img, m, new_size)
#
# M_center_0_scale_1 = cv2.getRotationMatrix2D((new_size[1] / 2, new_size[0] / 2), 0, fx)
# print(M_center_0_scale_1)

cv2.imshow("Resized", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
