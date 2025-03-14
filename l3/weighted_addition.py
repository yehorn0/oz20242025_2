import cv2

img1 = cv2.imread('data/dogs.jpeg')
img2 = cv2.imread('data/cats.jpeg')
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))


result = cv2.add(img1, img2_resized)
result_weighted =  cv2.addWeighted(img1, 0.7, img2_resized, 0.3, 0)
cv2.imshow('Result', result)
cv2.imshow('Result Weighted', result_weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# result[i,j] = 0.5 * img1[i, j] + 0.5 * img2[i, j] <-- cv2.add
# result[i,j] = 0.3 * img1[i, j] + 0.7 * img2[i, j] <-- cv2.addWeighted
