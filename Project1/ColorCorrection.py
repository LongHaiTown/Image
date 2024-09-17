import cv2 as cv
img = cv.imread("img/ColorCorrection.jpg", cv.IMREAD_GRAYSCALE)
# img_corrected = 255 - img
# img_corrected = cv.resize(img_corrected, (350, 350), fx=0.5, fy=0.5)
# cv.imshow("Color Correction", img_corrected)
cv.imshow("Original", b)
cv.waitKey(0)
cv.destroyAllWindows()