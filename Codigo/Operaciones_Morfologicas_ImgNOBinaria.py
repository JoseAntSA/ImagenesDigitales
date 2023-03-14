# Aplicado a imagenes NO binarias a excepcion de Hit & Miss

import cv2
import numpy as np
import matplotlib.pyplot as plot

def dilat(img, tamMasc):

    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    pixel = []

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):  

            for m in range(-tamMasc, tamMasc+1):
                for n in range(-tamMasc, tamMasc+1):
                    if(m+i>=0 and n+j>=0 and m+i<img.shape[0] and n+j<img.shape[1]):
                        pixel.append(img.item(m+i,n+j,0))

            pMax = max(pixel)
            arr[i,j,:] = pMax
            pixel.clear()    
    
    return arr

def eros(img, tamMasc):

    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    pixel = []

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):  

            for m in range(-tamMasc, tamMasc+1):
                for n in range(-tamMasc, tamMasc+1):
                    if(m+i>=0 and n+j>=0 and m+i<img.shape[0] and n+j<img.shape[1]):
                        pixel.append(img.item(m+i,n+j,0))

            pMin = min(pixel)
            arr[i,j,:] = pMin
            pixel.clear()    
    
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

def operHat(img, tamMasc, opc):

    # Top Hat
    if(opc==0):
        tmp = operMorf(img, tamMasc,1)
        imgS = img - tmp
          
    # Black Hat
    if(opc==1):
        tmp = operMorf(img, tamMasc,0)
        imgS = tmp - img           

    return imgS

def operHitMiss(img, masc, tamMasc):

    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    pixel = []

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):  

            cont = np.count_nonzero(masc == 1) + np.count_nonzero(masc == -1)
            for m in range(-tamMasc, tamMasc+1):
                for n in range(-tamMasc, tamMasc+1):
                    if(m+i>=0 and n+j>=0 and m+i<img.shape[0] and n+j<img.shape[1]):
                        if(img.item(m+i,n+j,0) == 255 and masc[m+1,n+1] == 1 ):
                            pixel.append(img.item(m+i,n+j,0))
                            cont -= 1
                        if(img.item(m+i,n+j,0) == 0 and masc[m+1,n+1] == -1 ):
                            pixel.append(img.item(m+i,n+j,0))
                            cont -= 1
                            
            if(cont==0):
                arr[i,j,:] = 255
            pixel.clear()    

    return arr

def gradiente(img, tamMasc):

    imgS = dilat(img, tamMasc) - eros(img, tamMasc)
          
    return imgS

def imprimirImgs(imgO, img1, img2, img3, img4, tit1, tit2):
    fig = plot.figure(figsize=(10,6))

    #----------------------------------------------------------------------

    ax1 = plot.subplot2grid((10,6), (3,0),colspan=2, rowspan=5)
    ax1.imshow(imgO)
    ax1.set_title("Imagen Original")#
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)

    #----------------------------------------------------------------------

    axT1 = plot.subplot2grid((10,6), (0,2), colspan=6)
    axT1.text(0.5, 0, tit1, fontsize=14,  ha="center")
    axT1.get_xaxis().set_visible(False)
    axT1.get_yaxis().set_visible(False)
    axT1.spines['right'].set_visible(False)
    axT1.spines['top'].set_visible(False)
    axT1.spines['left'].set_visible(False)
    axT1.spines['bottom'].set_visible(False)

    ax2 = plot.subplot2grid((10,6), (1,2),colspan=2, rowspan=4)
    ax2.imshow(img1)
    ax2.set_title("Mascara 3x3")
    ax2.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

    ax3 = plot.subplot2grid((10,6), (1,4),colspan=2, rowspan=4)
    ax3.imshow(img2)
    ax3.set_title("Mascara 5x5")
    ax3.get_xaxis().set_visible(False)
    ax3.get_yaxis().set_visible(False)

    #----------------------------------------------------------------------

    axT2 = plot.subplot2grid((10,6), (5,2), colspan=6)
    axT2.text(0.5, 0, tit2, fontsize=14,  ha="center")
    axT2.get_xaxis().set_visible(False)
    axT2.get_yaxis().set_visible(False)
    axT2.spines['right'].set_visible(False)
    axT2.spines['top'].set_visible(False)
    axT2.spines['left'].set_visible(False)
    axT2.spines['bottom'].set_visible(False)

    ax5 = plot.subplot2grid((10,6), (6,2),colspan=2, rowspan=4)
    ax5.imshow(img3)
    ax5.set_title("Mascara 3x3")
    ax5.get_xaxis().set_visible(False)
    ax5.get_yaxis().set_visible(False)

    ax6 = plot.subplot2grid((10,6), (6,4),colspan=2, rowspan=4)
    ax6.imshow(img4)
    ax6.set_title("Mascara 5x5")
    ax6.get_xaxis().set_visible(False)
    ax6.get_yaxis().set_visible(False)

    #----------------------------------------------------------------------

    fig.tight_layout()
    plot.show()

def imprimirImgs2(imgO, img1, tit1):
    fig, (ax1, ax2) = plot.subplots(1, 2, figsize=(12,5))

    plot.suptitle(tit1)
    ax1.imshow(imgO)
    ax1.set_title("Imagen Original")
    ax1.get_xaxis().set_visible(False)
    ax1.get_yaxis().set_visible(False)

    ax2.imshow(img1)
    ax2.set_title("Imagen Resultado")
    ax2.get_xaxis().set_visible(False)
    ax2.get_yaxis().set_visible(False)

    fig.tight_layout()
    plot.show()



imgO1 = cv2.cvtColor( cv2.imread("Imagenes/cameraman.png",0), cv2.COLOR_BGR2RGB )
imgO2 = cv2.cvtColor( cv2.imread("Imagenes/B14.png",0), cv2.COLOR_BGR2RGB )

img1 = dilat(imgO1, 1)
img2 = dilat(imgO1, 2)
img3 = eros(imgO1, 1)
img4 = eros(imgO1, 2)
imprimirImgs( imgO1, img1, img2, img3, img4, "Dilatacion", "Erosion")

img1 = operMorf(imgO1, 1,0)
img2 = operMorf(imgO1, 2,0)
img3 = operMorf(imgO1, 1,1)
img4 = operMorf(imgO1, 2,1)
imprimirImgs( imgO1, img1, img2, img3, img4, "Cierre", "Apertura")

img1 = operHat(imgO1, 1,0)
img2 = operHat(imgO1, 2,0)
img3 = operHat(imgO1, 1,1)
img4 = operHat(imgO1, 2,1)
imprimirImgs( imgO1, img1, img2, img3, img4, "Top Hat", "Black Hat")

masc = np.array( [[0,1,1]
                ,[-1,-1,1]
                ,[0,-1,0]], dtype = "int")

img1 = operHitMiss(imgO2, masc,1)
imprimirImgs2(imgO2, img1, "Filtrado Hit & Miss")

img1 = gradiente(imgO1,1)
imprimirImgs2(imgO1, img1, "Gradiente")
