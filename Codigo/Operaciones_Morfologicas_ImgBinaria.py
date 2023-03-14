# Aplicado a imagenes binarias

import cv2
import numpy as np
import matplotlib.pyplot as plot

def eros(img, tamMasc):

    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
 
            if(img.item(i, j,0)==255):
                for m in range(-tamMasc, tamMasc+1):
                    for n in range(-tamMasc, tamMasc+1):
                        if(m+i>=0 and n+j>=0 and m+i<img.shape[0] and n+j<img.shape[0]):
                            arr[m+i,n+j,:]=255        

    return arr

def dilat(img, tamMasc):

    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            arr[i,j,:]=255

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]): 
            if(img.item(i, j,0)==0):   
                for m in range(-tamMasc, tamMasc+1):
                    for n in range(-tamMasc, tamMasc+1):
                        if(m+i>=0 and n+j>=0 and m+i<img.shape[0] and n+j<img.shape[0]):
                            arr[m+i,n+j,:]=0
    
    return arr

def operMorf(img, tamMasc, opc):

    # Operacion de Cierre
    if(opc==0):
        tmp = dilat(img, tamMasc)
        imgS = eros(tmp, tamMasc)
          
    # Operacion de Apertura
    if(opc==1):
        tmp = eros(img, tamMasc)
        imgS = dilat(tmp, tamMasc)           

    return imgS


imgO1 = cv2.cvtColor( cv2.imread("Imagenes/B12.png",0), cv2.COLOR_BGR2RGB )
imgO2 = cv2.cvtColor( cv2.imread("Imagenes/B11.png",0), cv2.COLOR_BGR2RGB )

img1 = operMorf(imgO1, 1,0)
img2 = operMorf(imgO1, 3,0)
img3 = operMorf(imgO2, 1,1)
img4 = operMorf(imgO2, 3,1)


fig = plot.figure(figsize=(10,6))

axT1 = plot.subplot2grid((10,6), (0,0), colspan=6)
axT1.text(0.475, 0.5, "Cierre", fontsize=14)
axT1.get_xaxis().set_visible(False)
axT1.get_yaxis().set_visible(False)
axT1.spines['right'].set_visible(False)
axT1.spines['top'].set_visible(False)
axT1.spines['left'].set_visible(False)
axT1.spines['bottom'].set_visible(False)

ax1 = plot.subplot2grid((10,6), (1,0),colspan=2, rowspan=4)
ax1.imshow(imgO1)
ax1.set_title("Imagen Original")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2 = plot.subplot2grid((10,6), (1,2),colspan=2, rowspan=4)
ax2.imshow(img1)
ax2.set_title("Mascara 3x3")
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

ax3 = plot.subplot2grid((10,6), (1,4),colspan=2, rowspan=4)
ax3.imshow(img2)
ax3.set_title("Mascara 7x7")
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)

axT2 = plot.subplot2grid((10,6), (5,0), colspan=6)
axT2.text(0.46, 0.5, "Apertura", fontsize=14)
axT2.get_xaxis().set_visible(False)
axT2.get_yaxis().set_visible(False)
axT2.spines['right'].set_visible(False)
axT2.spines['top'].set_visible(False)
axT2.spines['left'].set_visible(False)
axT2.spines['bottom'].set_visible(False)

ax4 = plot.subplot2grid((10,6), (6,0),colspan=2, rowspan=4)
ax4.imshow(imgO2)
ax4.set_title("Imagen Original")
ax4.get_xaxis().set_visible(False)
ax4.get_yaxis().set_visible(False)

ax5 = plot.subplot2grid((10,6), (6,2),colspan=2, rowspan=4)
ax5.imshow(img3)
ax5.set_title("Mascara 3x3")
ax5.get_xaxis().set_visible(False)
ax5.get_yaxis().set_visible(False)

ax6 = plot.subplot2grid((10,6), (6,4),colspan=2, rowspan=4)
ax6.imshow(img4)
ax6.set_title("Mascara 7x7")
ax6.get_xaxis().set_visible(False)
ax6.get_yaxis().set_visible(False)

fig.tight_layout()
plot.show()   
