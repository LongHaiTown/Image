import numpy as np
import cv2 as cv
img = cv.imread("img/Rotate.jpg", cv.IMREAD_GRAYSCALE)
img_rotate = np.zeros((img.shape[1], img.shape[0]), dtype=np.uint8)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_rotate[j][i] = img[i][j]
cv.imshow("Rotate Image", img_rotate)
cv.waitKey(0)
cv.destroyAllWindows()