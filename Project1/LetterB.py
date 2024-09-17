import numpy as np
import cv2 as cv
block = np.zeros((300,250), dtype=np.uint8)
# 3 cai ben phai
block[0:30, 170:250] = 255
block[270:300, 170:250] = 255
block[125:155, 170:250] = 255
# 2 cai o giua
block[55:120, 70:160] = 255
block[180:245, 70:160] = 255
cv.imshow("Letter B", block)
cv.waitKey(0)
cv.destroyAllWindows()