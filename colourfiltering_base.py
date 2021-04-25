import cv2 as cv
import numpy as np

img = cv.imread("D://medium_blogs//flower.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_green = np.array([50,100,50])
upper_green = np.array([70,255,255])

mask = cv.inRange(hsv, lower_green, upper_green)
res = cv.bitwise_and(img, img, mask=mask)

cv.namedWindow("res", cv.WINDOW_NORMAL)
cv.namedWindow("hsv", cv.WINDOW_NORMAL)
cv.namedWindow("mask", cv.WINDOW_NORMAL)

cv.imshow("mask", mask)
cv.imshow("hsv", hsv)
cv.imshow("res", res)

# img = np.uint8([[[0,255,0]]])
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# print(hsv)

if cv.waitKey(0):
    cv.destroyAllWindows()