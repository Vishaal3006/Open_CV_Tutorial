import cv2 as cv

import numpy as np

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")

blank=np.zeros(img.shape[:2],dtype='uint8')

cv.imshow("Blank",blank)

#Masking

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

cv.imshow("mask",mask)

#Masked Image

masked=cv.bitwise_and(img,img,mask=mask)

cv.imshow("Masked",masked)

cv.waitKey(0)