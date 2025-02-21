import cv2

img = cv2.imread("data/dogs.jpeg")

x = 30
y = 40
w = 75
h = 100

roi = img[y:y+h, x:x+w]

print(roi.shape)

img[75:150, 100:250] = [0, 255, 255]

cv2.imshow("ROI", roi)
cv2.imshow("Changed image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(list_)
#
# chunk = list_[1:5:2] # [begin=0:end=len(l):step=1]
# print(chunk)
#
# print(list_[:10])
# print(list_[5:])
# print(list_[4::3])
#
# print(list_[::-1])
# print(list_[3:4:-1])  # []
# print(list_[4:3:-1])  # [5]

