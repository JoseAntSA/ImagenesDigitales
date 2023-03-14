import cv2
import numpy as np
import matplotlib.pyplot as plt

def binAnd(img, img2):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if( img.item(i,j,0)>0 and img.item(i,j,1)>0 and img.item(i,j,2)>0 and img2.item(i,j,0)>0):
                arr[i,j,0] = img.item(i, j,0)
                arr[i,j,1] = img.item(i, j,1)
                arr[i,j,2] = img.item(i, j,2)
            else:
                arr[i,j,:] = 0
    return arr
def binOr(img, img2):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if( img.item(i,j,0)==0 and img.item(i,j,1)==0 and img.item(i,j,2)==0 and img2.item(i,j,0)==0):
                arr[i,j,:] = 0
            if( (img.item(i,j,0)>0 or img.item(i,j,1)>0 or img.item(i,j,2)>0) and img2.item(i,j,0)==0):
                arr[i,j,0] = img.item(i, j,0)
                arr[i,j,1] = img.item(i, j,1)
                arr[i,j,2] = img.item(i, j,2)
            if( (img.item(i,j,0)==0 or img.item(i,j,1)==0 or img.item(i,j,2)==0) and img2.item(i,j,0)>0):
                arr[i,j,0] = img2.item(i, j,0)
                arr[i,j,1] = img2.item(i, j,1)
                arr[i,j,2] = img2.item(i, j,2)
            if( img.item(i,j,0)>0 and img.item(i,j,1)>0 and img.item(i,j,2)>0 and img2.item(i,j,0)>0):
                arr[i,j,0] = img2.item(i, j,0)
                arr[i,j,1] = img2.item(i, j,1)
                arr[i,j,2] = img2.item(i, j,2)
    return arr

def binXor(img, img2):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if( img.item(i,j,0)==0 and img.item(i,j,1)==0 and img.item(i,j,2)==0 and img2.item(i,j,0)==0):
                arr[i,j,:] = 0
            if( img.item(i,j,0)>0 and img.item(i,j,1)>0 and img.item(i,j,2)>0 and img2.item(i,j,0)>0):
                arr[i,j,:] = 0
            if( (img.item(i,j,0)>0 or img.item(i,j,1)>0 or img.item(i,j,2)>0) and img2.item(i,j,0)==0):
                arr[i,j,0] = img.item(i, j,0)
                arr[i,j,1] = img.item(i, j,1)
                arr[i,j,2] = img.item(i, j,2)
            if( (img.item(i,j,0)==0 or img.item(i,j,1)==0 or img.item(i,j,2)==0) and img2.item(i,j,0)>0):
                arr[i,j,0] = img2.item(i, j,0)
                arr[i,j,1] = img2.item(i, j,1)
                arr[i,j,2] = img2.item(i, j,2)
    return arr

def binNot(img):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if( img.item(i,j,0)==0 ):
                arr[i,j,:] = 255
            else:
                arr[i,j,:] = 0               
    return arr      


img = cv2.cvtColor( cv2.imread("Imagenes/IMG03b.png",1), cv2.COLOR_BGR2RGB )
img2 = cv2.cvtColor( cv2.imread("Imagenes/IMG03a.png",1), cv2.COLOR_BGR2RGB )

fig, ax = plt.subplots(2, 3)

ax[0, 0].imshow(img)
ax[0, 0].set_title("Imagen 1")
ax[0, 0].get_xaxis().set_visible(False)
ax[0, 0].get_yaxis().set_visible(False)

ax[1, 0].imshow(img2)
ax[1, 0].set_title("Imagen 2")
ax[1, 0].get_xaxis().set_visible(False)
ax[1, 0].get_yaxis().set_visible(False)

ax[0, 1].imshow(binAnd(img, img2))
ax[0, 1].set_title("Operacion AND")
ax[0, 1].get_xaxis().set_visible(False)
ax[0, 1].get_yaxis().set_visible(False)

ax[0, 2].imshow(binOr(img, img2))
ax[0, 2].set_title("Operacion OR")
ax[0, 2].get_xaxis().set_visible(False)
ax[0, 2].get_yaxis().set_visible(False)

ax[1, 1].imshow(binXor(img, img2))
ax[1, 1].set_title("Operacion XOR")
ax[1, 1].get_xaxis().set_visible(False)
ax[1, 1].get_yaxis().set_visible(False)

ax[1, 2].imshow(binNot(img))
ax[1, 2].set_title("Operacion NOT")
ax[1, 2].get_xaxis().set_visible(False)
ax[1, 2].get_yaxis().set_visible(False)

fig.tight_layout()
plt.show()
