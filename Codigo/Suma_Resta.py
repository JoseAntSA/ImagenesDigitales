import cv2
import numpy as np
import matplotlib.pyplot as plot
import random

def Operacion(im1, im2, arr, op):
    alto, ancho = im1.shape
    for i in range(0,alto):
        for j in range(0,ancho):
            if op==1:
                val = im1.item(i, j) + im2.item(i, j)
            else:
                val = im1.item(i, j) - im2.item(i, j)
            
            if val>255:
                val=255
            if val<0:
                val=0
            arr[i,j] = val


img = cv2.imread("Imagenes\Zelda3.png",0)
img2 = cv2.imread("Imagenes\Zelda4.png",0)
img3 = cv2.imread("Imagenes\Cuadro1.png",0)

alto, ancho = img.shape
suma = np.zeros((alto,ancho,1),np.uint8)
resta = np.zeros((alto,ancho,1),np.uint8)

Operacion(img2, img3, suma, 1)
Operacion(img2, img3, resta, 2)

imgs = cv2.hconcat([img2,img3])
cv2.imshow("Imagenes a sumar y restar", imgs)
cv2.imshow("Resultado de la suma", suma)
cv2.imshow("Resultado de la resta", resta)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------------------

Operacion(img, img2, suma, 1)
Operacion(img, img2, resta, 2)

imgs = cv2.hconcat([img2,img2]) 
cv2.imshow("Imagenes a sumar y restar", imgs)
cv2.imshow("Resultado de la suma", suma)
cv2.imshow("Resultado de la resta", resta)
cv2.waitKey(0)
cv2.destroyAllWindows()