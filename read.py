import cv2 as cv

# img=cv.imread("C:\\Users\\Vishaal\\OneDrive\Pictures\\010 Soccer_103 Cristiano Ronaldo_1653452479754_normal.jpg")
#
# cv.imshow('Ronaldo',img)

cap=cv.VideoCapture("C:\\Users\Vishaal\Downloads\\11958122_1920_1080_24fps.mp4")

while True:
    isTrue, frame=cap.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()