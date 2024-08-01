import cv2 as cv

# cv.imshow('Ronaldo', img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[1]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    cap.set(3,width)
    cap.set(4,height)


cap=cv.VideoCapture("C:\\Users\Vishaal\Downloads\\11958122_1920_1080_24fps.mp4")

while True:
    isTrue, frame=cap.read()

    resize_frame=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video_resize',resize_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()
