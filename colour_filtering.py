import cv2 as cv
import numpy as np

img = cv.imread("D://medium_blogs//red_coat.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_red = np.array([160,100,50])
upper_red = np.array([180,255,255])

mask = cv.inRange(hsv, lower_red, upper_red)
mask_inv = cv.bitwise_not(mask)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
res = cv.bitwise_and(img, img, mask=mask)
background = cv.bitwise_and(gray, gray, mask = mask_inv)
background = np.stack((background,)*3, axis=-1)
added_img = cv.add(res, background)

cv.namedWindow("res", cv.WINDOW_NORMAL)
cv.namedWindow("hsv", cv.WINDOW_NORMAL)
cv.namedWindow("mask", cv.WINDOW_NORMAL)
cv.namedWindow("added", cv.WINDOW_NORMAL)
cv.namedWindow("back", cv.WINDOW_NORMAL)
cv.namedWindow("mask_inv", cv.WINDOW_NORMAL)
cv.namedWindow("gray", cv.WINDOW_NORMAL)

cv.imshow("back", background)
cv.imshow("mask_inv", mask_inv)
cv.imshow("added",added_img)
cv.imshow("mask", mask)
cv.imshow("gray", gray)
cv.imshow("hsv", hsv)
cv.imshow("res", res)

if cv.waitKey(0):
    cv.destroyAllWindows()