import cv2
import numpy as np

img = cv2.imread("data/dogs.jpeg")

tx = 100.
ty = 50.

m = np.float32([[1., 0., tx], [0., 1., ty]])

rows, cols, _ = img.shape

translated_img = cv2.warpAffine(img, m, (cols, rows))

cv2.imshow("Translation", translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
