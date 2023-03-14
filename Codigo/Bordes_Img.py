import cv2
import numpy as np
import matplotlib.pyplot as plt

def bordesV(img, arr):
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if(j>0 and j<img.shape[1]-1):
                res = img.item(i, j-1,0) - img.item(i, j+1,0)
                if(res!=0):
                    res = 255 
                arr[i,j,:] = res

def bordesH(img, arr):
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if(i>0 and i<img.shape[0]-1):
                res = img.item(i-1, j,0) - img.item(i+1, j,0)
                if(res!=0):
                    res = 255 
                arr[i,j,:] = res

def bordesVH(img, arr):
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if(i>0 and i<img.shape[0]-1 and j>0 and j<img.shape[1]-1):
                res = img.item(i-1, j,0) - img.item(i+1, j,0) + img.item(i, j-1,0) - img.item(i, j+1,0)
                if(res!=0):
                    res = 255 
                arr[i,j,:] = res


img = cv2.cvtColor( cv2.imread("Imagenes/B8.png",3), cv2.COLOR_BGR2RGB )
img2 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
img3 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
img4 = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

bordesH(img, img2)
bordesV(img, img3)
bordesVH(img, img4)

fig, ax = plt.subplots(2, 2)

ax[0, 0].imshow(img)
ax[0, 0].set_title("Imagen Original")
ax[0, 0].get_xaxis().set_visible(False)
ax[0, 0].get_yaxis().set_visible(False)

ax[0, 1].imshow(img2)
ax[0, 1].set_title("Bordes Horizontales")
ax[0, 1].get_xaxis().set_visible(False)
ax[0, 1].get_yaxis().set_visible(False)

ax[1, 0].imshow(img3)
ax[1, 0].set_title("Bordes Verticales")
ax[1, 0].get_xaxis().set_visible(False)
ax[1, 0].get_yaxis().set_visible(False)

ax[1, 1].imshow(img4)
ax[1, 1].set_title("Bordes Ver-Hor")
ax[1, 1].get_xaxis().set_visible(False)
ax[1, 1].get_yaxis().set_visible(False)

fig.tight_layout()
plt.show()
