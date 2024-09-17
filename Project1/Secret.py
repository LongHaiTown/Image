import cv2 as cv
img = cv.imread("img/img.png")
img1 = cv.imread("img/img1.png")
img = cv.resize(img,(500,500))
img1 = cv.resize(img1,(500,500))
img_sub = img1 - img
cv.imshow("Secret",img_sub)
cv.waitKey(0)
cv.destroyAllWindows()