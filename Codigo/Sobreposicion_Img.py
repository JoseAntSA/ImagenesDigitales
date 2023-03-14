import cv2
import numpy as np

def sobre(img, imgBase, arr):

    # 1° FOR, Usado para cargar la imagen fondo en la matriz
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            arr[i,j,0] = imgBase.item(i, j,0)
            arr[i,j,1] = imgBase.item(i, j,1)
            arr[i,j,2] = imgBase.item(i, j,2)

    # 2° FOR, Usado para cargar la imagen de la flor en la matriz
    #         pero solo aquello pixeles que tiene una intensidad de rojo mayor a 52
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if(img.item(i, j,2)>52):
                    arr[i,j,0] = img.item(i, j,0)
                    arr[i,j,1] = img.item(i, j,1)
                    arr[i,j,2] = img.item(i, j,2)

    # 3° FOR, Usado para cargar la imagen de la flor en la matriz pero solo
    #    para rellenar mejor la hoja ubicado entre la dimesion 540x370 a 600x500
    for i in range(540,img.shape[0]):
        for j in range(370,500):
            if(img.item(i, j,2)>20):
                    arr[i,j,0] = img.item(i, j,0)
                    arr[i,j,1] = img.item(i, j,1)
                    arr[i,j,2] = img.item(i, j,2)

    # 4° FOR, Usado para cargar la imagen de fondo en la matriz pero solo
    #    para rellenar mejor la seccion ubicada entre la dimesion 0x0 a 192x390
    #    debido al ¿ruido? de la imagen de la flor
    for i in range(0,192):
        for j in range(0,380):
            arr[i,j,0] = imgBase.item(i, j,0)
            arr[i,j,1] = imgBase.item(i, j,1)
            arr[i,j,2] = imgBase.item(i, j,2)

img = cv2.imread("Imagenes/IMG03a.png",1)         # Carga de la imagen usada como fondo
imgBase = cv2.imread("Imagenes/IMG03b.png",1)     # Carga de la imagen a superponer

img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8) #Creacion de la matriz donde se almacenara el resultado

sobre(img, imgBase, img2)

#Impresion de la imagen resultado
cv2.imshow("Resultados", img2)
cv2.waitKey()
cv2.destroyAllWindows()

