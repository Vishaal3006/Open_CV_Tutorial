import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\Camera Roll\WIN_20240526_10_33_38_Pro.jpg")

cv.imshow("Vishwa",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)

#Laplacian

lap=cv.Laplacian(gray,cv.CV_64F)

lap=np.uint8(np.absolute(lap))

cv.imshow("Laplacian",lap)

#Sobel

sobelX=cv.Sobel(gray,cv.CV_64F,1,0)
sobelY=cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel=cv.bitwise_or(sobelX,sobelY)


cv.imshow("SobelX",sobelX)
cv.imshow("SobelY",sobelY)
cv.imshow("Combined Sobel",combined_sobel)


cv.waitKey(0)