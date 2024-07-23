import cv2 as cv

#READING IMAGES

img = cv.imread('photos/nissan.jpg')

cv.imshow('Car', img)

cv.waitKey(0)

#READING VIDEOS

capture = cv.VideoCapture('videos/2222.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    
    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()