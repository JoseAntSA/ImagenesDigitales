import cv2
import numpy as np
import matplotlib.pyplot as plot
import random

def RuidoSP(img, prob):
    salida = np.zeros(img.shape,np.uint8)
    thres = 1 - prob

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                salida[i][j] = 0
            elif rdn > thres:
                salida[i][j] = 255
            else:
                salida[i][j] = img[i][j]

    return salida

def RuidoGauss(img, mean, var):
    img = np.array(img/255, dtype=float)

    # Parámetro loc (float): El valor medio de la distribución normal, correspondiente al 
    # centro de esta distribución.

    # Escala de parámetro (flotante): la desviación estándar de la distribución normal,
    # correspondiente al ancho de la distribución, cuanto mayor es la escala, más corta es 
    # la curva de la distribución normal, cuanto menor es la escala, más delgada es la curva.

    # Tamaño del parámetro (int o tupla entera): el valor de salida se asigna a la forma y 
    # el valor predeterminado es Ninguno
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    salida = img + noise
    if salida.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    salida = np.clip(salida, low_clip, 1.0)
    salida = np.uint8(salida*255)

    return salida




img = cv2.imread("Imagenes/Lenna_C.png",0)

# Agregar Ruido Sal y Pimienta.
imgSP = RuidoSP(img, 0.02)

# Agregar Ruido Gaussiano.
imgGa = RuidoGauss(img, 0, 0.01)
cv2.imshow("Ruido Sal y Pimienta - Gaussiano", np.hstack((img, imgSP, imgGa)))
cv2.waitKey(0)
cv2.destroyAllWindows()


# Filtro filter2D
# Mantiene el kernel por encima de un píxel, agrega todos los píxeles por debajo de este kernel, 
# toma el promedio y reemplaza el píxel central con el nuevo valor promedio. 
tam = 5
kernel = np.ones ((tam,tam), np.float32)/(tam**2)

img2 = cv2.filter2D(imgGa, -1, kernel)
cv2.imshow("Filtro2D", np.hstack((imgGa, img2)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtro blur.
# Convoluciona una imagen con un filtro de caja normalizado. Simplemente toma 
# el promedio de todos los píxeles debajo del área del kernel y reemplaza el
# elemento central.
img3 = cv2.blur(imgGa, (5,5))
cv2.imshow("Filtro blur", np.hstack((imgGa, img3)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtro GaussianBlur.
# En este método, en lugar de un filtro de caja, se usa un kernel gaussiano.
img3 = cv2.GaussianBlur(imgGa, (5,5),0)
cv2.imshow("Filtro GaussianBlur", np.hstack((imgGa, img3)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtro medianBlur.
# Toma la mediana de todos los píxeles debajo del área del kernel y el elemento
# central se reemplaza con este valor mediano. Esto es muy eficaz contra el ruido
# de sal y pimienta en una imagen.
img5 = cv2.medianBlur(imgGa, 5)
cv2.imshow("Filtro medianBlur", np.hstack((imgGa, img5)))
cv2.waitKey(0)
cv2.destroyAllWindows()

img6 = cv2.medianBlur(imgSP, 5)
cv2.imshow("Filtro medianBlur", np.hstack((imgSP, img6)))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Filtro bilateralFilter.
# Es muy eficaz en la eliminación de ruido manteniendo los bordes nítidos.
# Este filtro gaussiano es una función del espacio únicamente, es decir, los
# píxeles cercanos se consideran durante el filtrado. No tiene en cuenta si los 
# píxeles tienen casi la misma intensidad. No tiene en cuenta si un píxel es
# un píxel de borde o no.
img7 = cv2.bilateralFilter (imgSP, 9,75,75)
cv2.imshow("Filtro bilateralFilter", np.hstack((imgSP, img7)))
cv2.waitKey(0)
cv2.destroyAllWindows()
