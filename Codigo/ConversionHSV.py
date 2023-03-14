import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_hsv(img):
    arr = np.zeros((img.shape[0],img.shape[1],3))
    
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):

            pxR = img[i,j,2] / 255.0
            pxG = img[i,j,1] / 255.0
            pxB = img[i,j,0] / 255.0

            pxMin = min(pxR, pxG, pxB)
            pxMax = max(pxR, pxG, pxB)

            S = 0
            if( pxMax!=0 ):
                S = ( pxMax-pxMin ) / pxMax
            V = pxMax
            H = 0

            if( ( pxMax-pxMin )!=0 ):
                Rp = ( pxMax-pxR ) / ( pxMax-pxMin )
                Gp = ( pxMax-pxG ) / ( pxMax-pxMin )
                Bp = ( pxMax-pxB ) / ( pxMax-pxMin )
                
                if( pxR==pxMax and pxG==pxMin ):
                    H = 5 + Bp
                elif( pxR==pxMax and pxG!=pxMin ):
                    H = 1 - Gp
                elif( pxG==pxMax and pxB==pxMin ):
                    H = 1 + Rp
                elif( pxG==pxMax and pxB!=pxMin ):
                    H = 3 - Bp
                elif( pxR==pxMax ):
                    H = 3 + Gp
                else:
                    H = 5 - Rp


            arr[i,j,0] = round( H*60.0 )
            arr[i,j,1] = ( S*100.0 )
            arr[i,j,2] = ( V*100.0 )

    return arr

def hsv_rgb(img):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):

            H = img[i,j,0] / 60.0 
            S = img[i,j,1] / 100.0
            V = img[i,j,2] / 100.0

            R = 0
            G = 0
            B = 0

            colorSec = soloDec(H)
            colorPrim = H-colorSec
            
            a = ( 1-S )*V 
            b = ( 1-(S*colorSec) )*V
            c = ( 1-( S*(1-colorSec) ) )*V

            if( colorPrim==0.0 ):
                R = V
                G = c
                B = a
            elif( colorPrim==1.0 ):
                R = b
                G = V
                B = a
            elif( colorPrim==2.0 ):
                R = a
                G = V
                B = c
            elif( colorPrim==3.0 ):
                R = a
                G = b
                B = V
            elif( colorPrim==4.0 ):
                R = c
                G = a
                B = V
            elif( colorPrim==5.0 ):
                R = V
                G = a
                B = b


            arr[i,j,0] = round(B*255)
            arr[i,j,1] = round(G*255)
            arr[i,j,2] = round(R*255)

    
    return arr

def soloDec(num):
    while(num>1.0):
        num -= 1.0

    return num

def planosHSV(img, img2):
    arrH = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    arrS = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    arrV = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

    arrH[:, :, 0] = img[:, :, 0]
    arrS[:, :, 1] = img[:, :, 1]
    arrV[:, :, 2] = img[:, :, 2]

    planoH = hsv_rgb(arrH)
    planoS = hsv_rgb(arrS)
    planoV = hsv_rgb(arrV)
    
    cv2.imshow("H", planoH)
    cv2.imshow("S", planoS)
    cv2.imshow("V", planoV)
    cv2.imshow("Original", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


