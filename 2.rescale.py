import cv2 as cv

def rescaleFrame(frame,scale = 0.4):
    width = int(frame.shape[0]*scale)
    height = int(frame.shape[1]*scale)
    
    dimensions = (width,height)
    
    return cv.resize(frame ,dimensions ,interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('videos/2222.mp4')
while True:
    isTrue,frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xff==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()


def changeRes(width,height):
    capture.set(3,width)
    capture.set(3,height)


img = cv.imread('photos/dubai.jpg')
cv.imshow('dubai', img)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)     