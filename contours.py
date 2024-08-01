import cv2 as cv


img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\Screenshots\Screenshot 2024-03-30 212913.png")

cv.imshow("Ronaldo",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow('Gray',gray)

Canny=cv.Canny(img,125,175)

cv.imshow("Canny",Canny)

ret, thres=cv.threshold(gray,125,255,cv.THRESH_BINARY) #used for binarizing the image

contours,hierarchies=cv.findContours(thres,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} found')


cv.waitKey(0)