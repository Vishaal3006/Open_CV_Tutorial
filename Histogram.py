import cv2 as cv

import numpy as np

import matplotlib.pyplot as plt

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")


cv.imshow("image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)

gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("GrayScale Histogram")

plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.plot(gray_hist)

plt.xlim([0,256])
plt.show()

#Colored Histogram

plt.figure()
plt.title("Colored Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors=('b','g','r')

for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)