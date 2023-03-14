import cv2
import numpy as np
import matplotlib.pyplot as plt
import ConversionCMYK as convCMYK
import ConversionHSV as convHSV


# Carga de la imagen 
imgO = cv2.imread("Imagenes/paisaje3.jpg")

#-------------------------------------------------
# Pasamos a plano de color HSV la imagen original
imgHSV = convHSV.rgb_hsv(imgO)

# Ciclo para binarizar el arreglo HSV, donde solo pintan de blanco los tonos cafes
# y el resto de negro
for i in range(0,imgO.shape[0]):
    for j in range(0, imgO.shape[1]):
        H = imgHSV[i, j, 0]
        S = imgHSV[i, j, 1]
        V = imgHSV[i, j, 2]
        if( (H>10 and H<50) and (S>20 and S<90) and (V>30 and V<95) ):
            imgHSV[i, j, 0] = 0
            imgHSV[i, j, 1] = 0
            imgHSV[i, j, 2] = 100
        else:
            imgHSV[i, j, 0] = 0
            imgHSV[i, j, 1] = 0
            imgHSV[i, j, 2] = 0

# Se convierte la imagen HSV resultante a RGB
imgRGB = convHSV.hsv_rgb(imgHSV )
#-------------------------------------------------

#-------------------------------------------------
# Pasamos a plano de color YMCK la imagen original
imgCMYK = convCMYK.rgb_cmyk(imgO)

# Visualizamos los planos para ver como se encuentra la distribucion de colores
# siendo el magenta el que aisla mejor el puente
convCMYK.planosCMYK(imgCMYK, imgO)

# Ciclo para binarizar el arreglo YMCK, donde solo pintan de blanco los tonos rosas del puente
# y el resto de negro
for i in range(0,imgO.shape[0]):
    for j in range(0, imgO.shape[1]):
        M = imgCMYK[i, j, 1]
        if( M>15 and M<45 and i>148 and j>210):
            imgCMYK[i, j, 0] = 0
            imgCMYK[i, j, 1] = 0
            imgCMYK[i, j, 2] = 0
            imgCMYK[i, j, 3] = 0
        else:
            imgCMYK[i, j, 0] = 0
            imgCMYK[i, j, 1] = 0
            imgCMYK[i, j, 2] = 0
            imgCMYK[i, j, 3] = 100

# Se convierte la imagen YMCK resultante a RGB         
imgRGB2 = convCMYK.cmyk_rgb(imgCMYK)
#-------------------------------------------------

#-------------------------------------------------
# Declaramos una marscara para el uso final
masFinal = np.zeros((imgO.shape[0],imgO.shape[1],3),np.uint8)

# Obtenemos la mascara realizando la operacion AND en las iamgenes YMCK y HSV que fueron
# pasadas a RGB, donde se quedan los pixeles blancos coincidentes, y el resto se manda a negro
for i in range(0,imgO.shape[0]):
    for j in range(0, imgO.shape[1]):
        if( imgRGB[i,j,0]==255 and imgRGB2[i,j,0]==255 ):
            masFinal[i,j,:] = 255

cv2.imshow("Mascara HSV", imgRGB)
cv2.imshow("MAscara YMCK", imgRGB2)
cv2.imshow("Mascara Final", masFinal)
#cv2.waitKey()
#cv2.destroyAllWindows()
#-------------------------------------------------

#-------------------------------------------------
# Cargamos la imagen Original en tonos de grises
imgO2 = cv2.imread("Imagenes/paisaje3.jpg",0)
# Creamos una arreglo de 3 planos donde almacenaremos esta imagen de tonos de grises
imgGris = np.zeros((imgO.shape[0],imgO.shape[1],3),np.uint8)

# Pasamos la imagen de grises al arreglo
for i in range(0,3):
    imgGris[:,:,i] = imgO2[:,:] 

# Ponemos la mascara final, donde los pixeles blancos de la mascar, devuelven el color RGB
# puente en iamgen gris
for i in range(0,imgO.shape[0]):
    for j in range(0, imgO.shape[1]):
        if( masFinal[i, j, 0]==255 ):
            imgGris[i, j, 0] = imgO[i, j, 0]
            imgGris[i, j, 1] = imgO[i, j, 1]
            imgGris[i, j, 2] = imgO[i, j, 2] 
#-------------------------------------------------


cv2.imshow("Resultado Final", imgGris)
cv2.waitKey()
cv2.destroyAllWindows()



