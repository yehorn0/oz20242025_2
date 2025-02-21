import numpy as np
import cv2


canvas = np.zeros((480, 640, 3), dtype=np.uint8)

text = "Obrobka zobrazhen Lecture 1"

color = (155, 155, 0)
position = (100, 100)

cv2.putText(
    canvas, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3
)

cv2.imshow("Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
