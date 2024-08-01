import cv2 as cv

import numpy as np

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\Screenshots\Screenshot 2024-03-30 212913.png")

#Translation
cv.imshow("Vishaal",img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[0],img.shape[1])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(img,100,100)

cv.imshow("Translate",translated)

#Rotation

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(height,width)
    return cv.warpAffine(img,rotMat,dimensions)

cv.imshow("rotated",rotate(img,180))


#resize an image

resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

cv.imshow('Resize',resized)


#flipping an image

flip=cv.flip(img,-1)

cv.imshow("Flip",flip)

#Cropping an image

img=img[200:400,300:600]

cv.imshow("Flipped",img)

cv.waitKey(0)