import cv2 as cv
import numpy as np
img = cv.imread("img/ColorSeparation.jpg",0)
th, res = cv.threshold(img, 130, 255, cv.THRESH_BINARY)
img_binary = np.where( img>th, 255, 0).astype(dtype=np.uint8)
# cv.imshow("Color Separation", res)
cv.imshow("Color Separation", img_binary)
cv.waitKey(0)
cv.destroyAllWindows()