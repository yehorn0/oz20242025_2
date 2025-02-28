import cv2

img = cv2.imread("data/dogs.jpeg")


rotated_img_pi_2_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_img_pi_2_ccw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_img_pi = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("Image", img)
cv2.imshow("PI/2 CW", rotated_img_pi_2_cw)
cv2.imshow("PI/2 CCW", rotated_img_pi_2_ccw)
cv2.imshow("PI", rotated_img_pi)
cv2.waitKey(0)
cv2.destroyAllWindows()

