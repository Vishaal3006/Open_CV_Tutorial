import cv2 as cv
import numpy as np

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")

cv.imshow("Ronaldo",img)

b,g,r=cv.split(img)

blank=np.zeros(img.shape[:2],dtype='uint8')

cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Blank",blank)
cv.imshow("Blue",blue)
cv.imshow("Green",green)
cv.imshow("Red",red)

cv.waitKey(0)
