import cv2
import numpy as np
import matplotlib.pyplot as plot

def brillo(img, arr, const):
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            b = img.item(i, j,0) + const
            g = img.item(i, j,1) + const
            r = img.item(i, j,2) + const
            arr[i,j,0] = b
            arr[i,j,1] = g
            arr[i,j,2] = r
            if (b < 0):
                arr[i,j,0] = 0
            if (g < 0):
                arr[i,j,1] = 0
            if (r < 0):
                arr[i,j,2] = 0
            if (b > 255):
                arr[i,j,0] = 255
            if (g > 255):
                arr[i,j,1] = 255
            if (r > 255):
                arr[i,j,2] = 255
                
def reaGraf( imgOrig, img):
    pixelesBOrig = []
    pixelesGOrig = []
    pixelesROrig = []
    pixelesB2 = []
    pixelesG2 = []
    pixelesR2 = []
    freGenOrig = []
    freGen = []

    for i in range(0,imgOrig.shape[0]):
        for j in range(0,imgOrig.shape[1]):
            pixelesBOrig.append(imgOrig.item(i, j, 0))
            pixelesGOrig.append(imgOrig.item(i, j, 1))
            pixelesROrig.append(imgOrig.item(i, j, 2))
            pixelesB2.append(img2.item(i, j, 0))
            pixelesG2.append(img2.item(i, j, 1))
            pixelesR2.append(img2.item(i, j, 2))
    
    for i in range(0,255):
        freGenOrig.append(pixelesBOrig.count(i) + pixelesGOrig.count(i) + pixelesROrig.count(i))
        freGen.append(pixelesB2.count(i) + pixelesG2.count(i) + pixelesR2.count(i))

    fig, ax = plot.subplots(2, 2, figsize=(12,6))

    ax[0, 0].imshow(imgOrig)
    ax[0, 0].set_title("Imagen Orig.")
    ax[0, 0].get_xaxis().set_visible(False)
    ax[0, 0].get_yaxis().set_visible(False)

    ax[0, 1].imshow(img)
    ax[0, 1].set_title("Imagen Mod.")
    ax[0, 1].get_xaxis().set_visible(False)
    ax[0, 1].get_yaxis().set_visible(False)

    ax[1, 0].set_title("Histograma Orig.")
    ax[1, 0].plot(freGenOrig,"k-",linewidth=0.5)
    ax[1, 0].set_ylim(0, max(freGenOrig)+1000)

    ax[1, 1].set_title("Histograma Mod.")
    ax[1, 1].plot(freGen,"k-",linewidth=0.5)
    ax[1, 1].set_ylim(0, max(freGenOrig)+1000)

    fig.tight_layout()
    plot.show()


img = cv2.cvtColor( cv2.imread("Imagenes/lennaLB_C.png",1), cv2.COLOR_BGR2RGB )

img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

const=1

while(True):
    const = int(input("\n  Brillo a dar a la imagen: "))
    if(const<-255 or const>255):
        break
    brillo(img, img2, const)
    reaGraf(img,img2)
