import cv2 as cv

img=cv.imread(r"C:\Users\Vishaal\OneDrive\Pictures\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")

# cv.imshow("Ronaldo",img)

#convert to grayscale

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow("gray",gray)

#blur an image
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)

cv.imshow("blur",blur)

cv.waitKey(0)

#Edge Cascade = find the edges present in the image

canny = cv.Canny(blur, 175 , 175)

cv.imshow("canny" , canny)

#Dilating the image

dilate=cv.dilate(canny,(7,7),iterations=1)

cv.imshow("dilate",dilate)

# eroding the image

erode=cv.erode(dilate,(3,3),iterations=2)

cv.imshow("erode",erode)

#resize an image

resized=cv.resize(img,(300,300),interpolation=cv.INTER_LINEAR)

cv.imshow("Resized",resized)

#Crop an image

crop=img[200:400,100:300]

cv.imshow("Crop",crop)

cv.waitKey(0)