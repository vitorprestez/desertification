import cv2
from matplotlib import numpy
from functions import getColors

#Pego a cor no padrão BGR, nesse caso, a cor amarela
bgr_color = numpy.uint8([[[0, 255, 255]]])

#Pego os extremos do intervalo de cores
lightTom, darkTom = getColors(bgr_color)

#Leio a imagem de satélite
img = cv2.imread('./desertification.png')
cv2.imshow("original", img)

#Pego as dimensões da imagem para calcular a área mais tarde
width = img.shape[1]
height = img.shape[0]
size = width*height

#Converto a imagem para HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#Crio um filtro HSV para filtrar a imagem
yellowMask=cv2.inRange(img_hsv, lightTom, darkTom)

#Encontro os contornos das áreas desertificadas
contours, hierarchy  = cv2.findContours(yellowMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contourned = cv2.drawContours(img, contours, -1, (0,0,255),1)

#Soma as áreas dos contornos
total_contourns = 0
for contour in contours:
    total_contourns+=cv2.contourArea(contour)

percent_area = (total_contourns/size)*100

#Adiciono o texto contendo a porcentagem na imagem
cv2.putText(contourned, f'{round(percent_area,2)}% desertified', (20,40), cv2.FONT_HERSHEY_PLAIN, 2,(255, 255,255))
cv2.imshow("contourned", contourned)

cv2.waitKey()

