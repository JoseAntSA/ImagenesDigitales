import cv2
import numpy as np
import matplotlib.pyplot as plot

def escaladoMas(img, arr):
    for i in range(0,arr.shape[0]):
        i0 = (float(img.shape[0])/float(arr.shape[0]))*float(i)
        di0 = sinDec(i0)
        ni0 = round(i0-di0)

        for j in range(0,arr.shape[1]):
            j0 = (float(img.shape[1])/float(arr.shape[1]))*float(j)
            dj0 = sinDec(j0)
            nj0 = round(j0-dj0)

            cantA = di0 * dj0
            cantB = di0 * (1-dj0)
            cantC = (1-di0) * dj0
            cantD = (1-di0) * (1-dj0)

            if( (ni0+1)<img.shape[0] and (nj0+1)<img.shape[1] ):
                pixA0 = img.item(ni0+1, nj0+1,0)
                pixA1 = img.item(ni0+1, nj0+1,1)
                pixA2 = img.item(ni0+1, nj0+1,2)
            else:
                pixA0 = 0
                pixA1 = 0
                pixA2 = 0
            if( (ni0+1)<img.shape[0] and nj0<(img.shape[1]-1) ):
                pixB0 = img.item(ni0+1, nj0,0)
                pixB1 = img.item(ni0+1, nj0,1)
                pixB2 = img.item(ni0+1, nj0,2)
            else:
                pixB0 = 0
                pixB1 = 0
                pixB2 = 0
            if( ni0<(img.shape[0]-1) and (nj0+1)<img.shape[1] ):
                pixC0 = img.item(ni0, nj0+1,0)
                pixC1 = img.item(ni0, nj0+1,1)
                pixC2 = img.item(ni0, nj0+1,2)
            else:
                pixC0 = 0
                pixC1 = 0
                pixC2 = 0
            pixD0 = img.item(ni0, nj0,0)
            pixD1 = img.item(ni0, nj0,1)
            pixD2 = img.item(ni0, nj0,2)

            arr[i,j,0] = (cantA*pixA0) + (cantB*pixB0) + (cantC*pixC0) + (cantD*pixD0)
            arr[i,j,1] = (cantA*pixA1) + (cantB*pixB1) + (cantC*pixC1) + (cantD*pixD1)
            arr[i,j,2] = (cantA*pixA2) + (cantB*pixB2) + (cantC*pixC2) + (cantD*pixD2)

def sinDec(num):
	while(num>1.0):
		num -= 1.0

	return num


img = cv2.imread("Imagenes/P1.png",1)

x = int(input("\nCuanto desea de ancho: "))
y = int(input("\nCuanto desea de alto: "))

img2 = np.zeros((y,x,3),np.uint8)

escaladoMas(img, img2)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Escalada", img2)
cv2.waitKey()
cv2.destroyAllWindows()