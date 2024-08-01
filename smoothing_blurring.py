import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")

cv.imshow("Ronaldo",img)

#Averaging

# low blur=3 and high blur=7

average=cv.blur(img,(3,3))

cv.imshow("Average",average)

#Gaussian blur

GaussianBlur=cv.GaussianBlur(img,(3,3),0)

cv.imshow("Gaussian",GaussianBlur)

#Median blur

MedianBlur=cv.medianBlur(img,3,0)
cv.imshow("MedianBlur",MedianBlur)

#Bilateral- applies the blur but retain the edges

Bilateral=cv.bilateralFilter(img,10,30,25)

cv.imshow("Bilateral",Bilateral)


cv.waitKey(0)