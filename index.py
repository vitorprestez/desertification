import cv2
from matplotlib import numpy
from functions import getColors

#pego a cor no padrão BGR, nesse caso, a cor amarela
bgr_color = numpy.uint8([[[0, 255, 255]]])

#Pego os extremos do intervalo de cores
lightTom, darkTom = getColors(bgr_color)

#Leio a imagem de satélite
img = cv2.imread('./desertification.png')
cv2.imshow("original", img)

#converto a imagem para HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#crio um filtro HSV para filtrar a imagem
yellowMask=cv2.inRange(img_hsv, lightTom, darkTom)
cv2.imshow('segmentedImage', yellowMask)

#Primeiro parametro é correspondente à primeira imagem de entrada que a função deve aplicar
#Segundo parametro é a imagem que será aplicada a operação
#terceiro parametro é a mascara que será aplicada a imagem
result = cv2.bitwise_and(img, img, mask=yellowMask)
cv2.imshow('result', result)

cv2.waitKey()

