import cv2
import numpy as np
import matplotlib.pyplot as plt

def prom(img, tamMasc):

    masc = float((2*tamMasc+1)*(2*tamMasc+1))
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            pro = 0.0
            
            for k in range(-tamMasc, tamMasc):
                for l in range(-tamMasc, tamMasc):
                    if(k+i>0 and l+j>0 and k+i<img.shape[0] and l+j<img.shape[0]):
                        pro += ( float(img.item(k+i, l+j,0)) / masc )

            arr[i,j,:]=int(round(pro))            

    return arr


img = cv2.cvtColor( cv2.imread("Imagenes/Lenna_c.png",0), cv2.COLOR_BGR2RGB )

img2 = prom(img, 3)
img3 = prom(img, 5)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,5))

ax1.imshow(img)
ax1.set_title("Imagen Original")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)

ax2.imshow(img2)
ax2.set_title("Mascara 3x3")
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)

ax3.imshow(img3)
ax3.set_title("Mascara 5x5")
ax3.get_xaxis().set_visible(False)
ax3.get_yaxis().set_visible(False)


fig.tight_layout()
plt.show()
