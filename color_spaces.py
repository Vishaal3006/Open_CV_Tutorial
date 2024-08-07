import cv2 as cv


img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\Screenshots\Screenshot 2024-03-30 212913.png")



cv.imshow("Ronaldo",img)

#BGR to Gray

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("gray",gray)

#BGR to HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

cv.imshow("HSV",hsv)

#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)

cv.imshow("LAB",lab)

#BGR to RGB

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

cv.imshow("RGB",rgb)
cv.waitKey(0)