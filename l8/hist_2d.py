import cv2
import matplotlib.pyplot as plt

img = cv2.imread('data/house.jpg')

hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv_image)

hist = cv2.calcHist(
    [h, s],
    [0, 1],
    None,
    [50, 50],
    [0, 180, 0, 256]
)

plt.imshow(
    hist,
    origin="upper",
    aspect="auto",
    cmap="jet",
    interpolation="nearest"
)
plt.colorbar()
plt.xlabel("Hue")
plt.ylabel("Saturation")
plt.title("2d hist")

plt.show()
