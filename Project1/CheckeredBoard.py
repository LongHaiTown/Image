import numpy as np
import cv2 as cv
def table():
    board = np.zeros((8, 8), dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = 255
            else:
                color = 0
            board[i][j] = color
    return board
img_table = table()
img_table = cv.resize(img_table, (400, 400), interpolation=cv.INTER_NEAREST)
cv.imshow("Checkered Board", img_table)
cv.waitKey(0)
cv.destroyAllWindows()
