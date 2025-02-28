import cv2
import numpy as np

img = cv2.imread("data/dogs.jpeg")

shearing_factor_x = .2
shearing_factor_y = .3

m_shear_x = np.float32([[1., shearing_factor_x, 0.],
                        [0., 1., 0]])
m_shear_y = np.float32([[1., 0., 0.],
                        [shearing_factor_y, 1., 0]])


rows, cols, _ = img.shape

sheared_img_x = cv2.warpAffine(img, m_shear_x, (cols + int(rows * shearing_factor_x), rows))
sheared_img_xy = cv2.warpAffine(img, m_shear_y, (cols + int(rows * shearing_factor_x), rows + int(cols * shearing_factor_y)))


cv2.imshow("Sheared x", sheared_img_x)
cv2.imshow("Sheared xy", sheared_img_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
