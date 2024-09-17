import numpy as np
import cv2 as cv
img = cv.imread("img/CornerLine.jpg")
h,w,c = img.shape
row1 = int(w/6) # == 121
col1 = int(h/4) # == 121
row2 = int(w/6)+35 # == 156
col2 = int(h/4)+35 # == 156
for i in range(h):
    for j in range(w):
        if col1 - 1 <= i + j <= col2-1:
            img[i][j] = 0
cv.imshow("Corner Line", img)
cv.waitKey(0)
cv.destroyAllWindows()


