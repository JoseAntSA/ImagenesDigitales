# Aplicado a imagenes binarias

import cv2
import numpy as np
import matplotlib.pyplot as plt

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


img = cv2.cvtColor( cv2.imread("Imagenes/B10.png",0), cv2.COLOR_BGR2RGB )

img2 = eros(img, 1)
img3 = eros(img, 3)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,5))

fig.suptitle("Erosion")
ax1.imshow(img)
ax1.set_title("Imagen Original")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2.imshow(img2)
ax2.set_title("Mascara 3x3")
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

ax3.imshow(img3)
ax3.set_title("Mascara 7x7")
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)


fig.tight_layout()
plt.show()
