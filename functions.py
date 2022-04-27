import cv2
from matplotlib import numpy

def getColors(vet_bgr):
    vet_hsv = cv2.cvtColor(vet_bgr, cv2.COLOR_BGR2HSV)
    color = vet_hsv[0][0][0]
    min = color - 30
    max = color
    if(min < 0):
        min = 0
    if(max>255):
        max = 255
    hsv_inf = numpy.array([min, 100, 100])
    hsv_sup = numpy.array([max, 255, 255])
    return hsv_inf, hsv_sup