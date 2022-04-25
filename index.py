import cv2
from matplotlib import numpy, pyplot
from functions import getColors

bgr_color = numpy.uint8([[[0, 255, 255]]])

lightTom, darkTom = getColors(bgr_color)

img = cv2.imread('./cubo.png')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_seg = cv2.inRange(img_hsv, lightTom, darkTom)

yellowFilter=cv2.inRange(img_hsv, lightTom, darkTom)
result = cv2.bitwise_and(img, img, mask=yellowFilter)

# gray = cv2.cvtColor(result, cv2.COLOR_RGB2GRAY)
# _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# contours, hierarchy = cv2.findContours(yellowFilter, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# area = cv2.drawContours(img, contours, -1, (0, 255, 255), 3)

# pyplot.imshow(area)
# pyplot.show()
cv2.imshow('yellowFilter', yellowFilter)
cv2.imshow('result', result)
# cv2.imshow("original", img)

cv2.waitKey()

