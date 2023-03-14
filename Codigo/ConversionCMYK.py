import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_cmyk(img):
    arr = np.zeros((img.shape[0],img.shape[1],4),np.uint8)
    
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):

            pxR = img[i,j,2] / 255.0
            pxG = img[i,j,1] / 255.0
            pxB = img[i,j,0] / 255.0

            C = 1 - pxR
            M = 1 - pxG
            Y = 1 - pxB

            K = min( C,M,Y )

            if( K==1 ):
                C = 0
                M = 0
                Y = 0
            else:  
                C = ( C-K ) / ( 1-K )
                M = ( M-K ) / ( 1-K )
                Y = ( Y-K ) / ( 1-K )

            arr[i,j,0] = round( C*100.0 )
            arr[i,j,1] = round( M*100.0 )
            arr[i,j,2] = round( Y*100.0 )
            arr[i,j,3] = round( K*100.0 )

    return arr

def cmyk_rgb(img):
    arr = np.zeros((img.shape[0],img.shape[1],3),np.uint8)
    
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):

            C = img[i,j,0] / 100.0 
            M = img[i,j,1] / 100.0
            Y = img[i,j,2] / 100.0
            K = img[i,j,3] / 100.0

            C = min( 1, ( C*( 1-K ) )+K )
            M = min( 1, ( M*( 1-K ) )+K )
            Y = min( 1, ( Y*( 1-K ) )+K )

            R = round((1-C)*255)
            G = round((1-M)*255)
            B = round((1-Y)*255)

            arr[i,j,0] = B
            arr[i,j,1] = G
            arr[i,j,2] = R

    
    return arr

def planosCMYK(img, img2):
    arrC = np.zeros((img.shape[0],img.shape[1],4),np.uint8)
    arrM = np.zeros((img.shape[0],img.shape[1],4),np.uint8)
    arrY = np.zeros((img.shape[0],img.shape[1],4),np.uint8)
    arrK = np.zeros((img.shape[0],img.shape[1],4),np.uint8)

    arrC[:, :, 0] = img[:, :, 0]
    arrM[:, :, 1] = img[:, :, 1]
    arrY[:, :, 2] = img[:, :, 2]
    arrK[:, :, 3] = img[:, :, 3]

    planoC = cmyk_rgb(arrC)
    planoM = cmyk_rgb(arrM)
    planoY = cmyk_rgb(arrY)
    planoK = cmyk_rgb(arrK)
    

    cv2.imshow("C", planoC)
    cv2.imshow("M", planoM)
    cv2.imshow("Y", planoY)
    cv2.imshow("K", planoK)
    cv2.imshow("Orignal", img2)
    cv2.waitKey()
    cv2.destroyAllWindows()






