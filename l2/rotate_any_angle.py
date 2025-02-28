import cv2
from functools import partial

img = cv2.imread("data/dogs.jpeg")

#rows, cols, _ = img.shape
rows, cols = img.shape[:2]
center = (cols/2, rows/2)

M_100_100_30_scale_1 = cv2.getRotationMatrix2D((100, 100), 30, 1)
M_center_45_scale_2 = cv2.getRotationMatrix2D(center, 45, 2)
M_center_minus_90_scale_1 = cv2.getRotationMatrix2D(center, -90, 1)

# print(M_center_minus_90_scale_1)

rotate_img = partial(
    cv2.warpAffine,
    src=img,
    dsize=(cols, rows)
)
img_rotated_0 = rotate_img(M=M_100_100_30_scale_1)
#img_rotated_1 = rotate_img(M=M_center_45_scale_2)
img_rotated_2 = rotate_img(M=M_center_minus_90_scale_1)
# img_rotated_0 = cv2.warpAffine(img, M_100_100_30_scale_1, (cols, rows))
img_rotated_1 = cv2.warpAffine(img, M_center_45_scale_2, (2 * cols, 2 * rows))
# img_rotated_2 = cv2.warpAffine(img, M_center_minus_90_scale_1, (cols, rows))

# cv2.imshow("Image", img)
# cv2.imshow("100_100_30", img_rotated_0)
cv2.imshow("Center 45 Scale 2", img_rotated_1)
# cv2.imshow("Center -pi/2", img_rotated_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

