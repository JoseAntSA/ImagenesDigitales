import cv2
import numpy as np
import matplotlib.pyplot as plot

def rot(img, arr, b):
    midx = round(img.shape[1]/2)
    midy = round(img.shape[0]/2)
    b = (b*(np.pi /180.0))

    for x in range(0,img.shape[1]):
        for y in range(0, img.shape[0]):

            xn = int(((x-midx)*np.cos(b))-((y-midy)*np.sin(b))+midx)
            yn = int(((y-midy)*np.cos(b))+((x-midx)*np.sin(b))+midy)

            if(xn<img.shape[1] and yn<img.shape[0] and xn>=0 and yn>=0):
                arr[yn, xn, 0] = img.item(y, x, 0)
                arr[yn, xn, 1] = img.item(y, x, 1)
                arr[yn, xn, 2] = img.item(y, x, 2)

def sinDec(num):
    while(num>1.0):
        num -= 1.0

    return num

def elim(img):

    prom = 0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if(img.item(i,j,0)==0):
                if(i>0 and i<img.shape[0]-1 and j>0 and j<img.shape[1]-1):
                    for k in range(0,3):
                        prom += img.item(i+1,j,k)
                        prom += img.item(i-1,j,k)
                        prom += img.item(i,j+1,k)
                        prom += img.item(i,j-1,k)
                        prom += img.item(i+1,j+1,k)
                        prom += img.item(i+1,j-1,k)
                        prom += img.item(i-1,j+1,k)
                        prom += img.item(i-1,j-1,k)
                        prom /= 8
                        img[i,j,k] = prom
                        prom = 0


img = cv2.cvtColor( cv2.imread("Imagenes/Zelda2.png",1), cv2.COLOR_BGR2RGB )
img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

grad = float(input("\nA cuanto grados(en sexagesimal) desea rotar la imagen: "))
rot(img, img2, -grad)
elim(img2)

fig, (ax1, ax2) = plot.subplots(1, 2, figsize=(12,5))

ax1.imshow(img)
ax1.set_title("Imagen Original")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2.imshow(img2)
ax2.set_title("Imagen Rotada")
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

fig.tight_layout()
plot.show()
