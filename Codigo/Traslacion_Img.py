import cv2
import numpy as np
import matplotlib.pyplot as plot

def tras(img, arr, x, y):

    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):

            if( (i+y)>0 and (j+x)>0 and (i+y)<img.shape[0] and (j+x)<img.shape[1] ):
                arr[i+y,j+x,0] = img.item(i, j,0)
                arr[i+y,j+x,1] = img.item(i, j,1)
                arr[i+y,j+x,2] = img.item(i, j,2)


img = cv2.cvtColor( cv2.imread("Imagenes/Lenna_c.png",1), cv2.COLOR_BGR2RGB )
img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

x = int(input("\nCuanto desea desplazar la imagen respecto al eje x: "))
y = int(input("\nCuanto desea desplazar la imagen respecto al eje y: "))

tras(img, img2, x, y)

fig, ax = plot.subplots(1, 2, figsize=(10,6)) 

ax[0].imshow(img)
ax[0].set_title("Imagen Original")
ax[0].get_xaxis().set_visible(False)
ax[0].get_yaxis().set_visible(False)

ax[1].imshow(img2)
ax[1].set_title("Imagen trasladada")
ax[1].get_xaxis().set_visible(False)
ax[1].get_yaxis().set_visible(False)

fig.tight_layout()
plot.show()
