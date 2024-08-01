import cv2 as cv

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\Camera Roll\WIN_20240526_10_33_38_Pro.jpg")

cv.imshow("Vishwa",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Simple Thresholding

threshold,thres=cv.threshold(gray,100,255,cv.THRESH_BINARY)

cv.imshow("Simple thresholding",thres)

#Threshold Inverse

threshold_inv,thres_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)

cv.imshow("Simple thresholding inverse",thres_inv)

#Adoptive Threshold

adoptive_threshold=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)

cv.imshow("Adoptive Threshold",adoptive_threshold)

cv.waitKey(0)