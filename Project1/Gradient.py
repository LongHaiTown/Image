import numpy as np
import cv2 as cv
block = np.zeros((400, 400), dtype=np.uint8)
k = 255
for row in range(400):
    color = int((255 / 255) * k)
    k = k - (255 / 400)
    block[row] = color
cv.imshow("Gradient", block)
cv.waitKey(0)
cv.destroyAllWindows()
