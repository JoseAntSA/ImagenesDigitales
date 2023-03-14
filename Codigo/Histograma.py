import cv2
import numpy as np
import matplotlib.pyplot as plot

def reaGraf( lista, lista2,color):

	plot.figure("Histograma " + color, figsize=(10,6))
	plot.hist(lista2, bins=255)

	plot.figure("" + color,figsize=(10,6))
	plot.subplot(121)
	plot.title("Grafica de barras")
	plot.plot(lista,linewidth=0.5)
	plot.ylim(0, max(lista)+1000)
	plot.subplot(122) 
	plot.title("Grafica lineal")
	plot.bar(range(255), lista,width=1.4)
	plot.ylim(0, max(lista)+1000)

	plot.show()


img = cv2.imread("Imagenes/Lenna.png")
width, height, dimens = img.shape

print("Dimensiones de la imagen:")
print(img.shape)

cv2.imshow("Color BGR", img )
cv2.waitKey()
cv2.destroyAllWindows()
cB = img[:,:,0]   #B
cG = img[:,:,1]   #G
cR = img[:,:,2]   #R

cv2.imshow("Color BGR", np.hstack([cB, cG, cR]) )
cv2.waitKey()
cv2.destroyAllWindows()

pixelesB = []
pixelesG = []
pixelesR = []
frecuenciaB = []
frecuenciaG = []
frecuenciaR = []

for i in range(0,width):
    for j in range(0,height):
        pixelesB.append(img.item(i, j, 0))
        pixelesG.append(img.item(i, j, 1))
        pixelesR.append(img.item(i, j, 2))

if(pixelesR == pixelesG and pixelesR == pixelesB ):
	print("La imagen esta en escala de grises...")
	for i in range(0,255):
		frecuenciaB.append(pixelesB.count(i))

	reaGraf(frecuenciaB, "Escala de Grises")

else:	

	for i in range(0,255):
			frecuenciaB.append(pixelesB.count(i))
			frecuenciaG.append(pixelesG.count(i))
			frecuenciaR.append(pixelesR.count(i))


	reaGraf(frecuenciaB, pixelesB, "Canal Azul")
	reaGraf(frecuenciaG, pixelesG, "Canal Verde")
	reaGraf(frecuenciaR, pixelesR, "Canal Rojo")



