import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

cv.imshow('Blank',blank)

# img = cv.imread("C:\\Users\Vishaal\OneDrive\Pictures\\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")
#
# cv.imshow('Ronaldo',img)

# blank[:]=0,255,0
#

# cv.imshow("Green",blank)
#Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)

cv.imshow("Rectangle",blank)

#Draw a Circle
cv.circle(blank,(250,250),250,(0,0,255),thickness=3)

cv.imshow("Circle",blank)

#Draw a Line

cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,0),thickness=3)

cv.imshow("Line",blank)

#Write a Text

cv.putText(blank,'Hello',(225,225),cv.FONT_ITALIC,1.0,(0,255,0),2)
cv.imshow('Text',blank)

cv.waitKey(0)