import cv2
import numpy as np
import matplotlib.pyplot as plot

color = 1
img = cv2.imread("Imagenes/Kodim23_2.png",color)


if(color==0):
	alto, ancho = img.shape
	img2 = np.zeros((alto,ancho,1),np.uint8)
	for i in range(0,alto):
	    for j in range(0,ancho):
	        img2[i,j] = (255-img.item(i, j))
else:
	alto, ancho, dim = img.shape
	img2 = np.zeros((alto,ancho,3),np.uint8)
	for i in range(0,alto):
		for j in range(0,ancho):
			img2[i,j,0] = (255-img.item(i, j,0))
			img2[i,j,1] = (255-img.item(i, j,1))
			img2[i,j,2] = (255-img.item(i, j,2))


cont = cv2.hconcat([img, img2])
cv2.imshow("Complemento de una imagen", cont)
cv2.waitKey(0)


