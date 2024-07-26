import cv2 as cv

img = cv.imread('photos/dubai.jpg')
cv.imshow('Dubai',img)

#RESIZING AN IMAGE
resized = cv.resize(img,(800,500),interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#GRAYSCALING AN IMAGE
grayscale = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('GrayScaling', grayscale)

#BLURRING AN IMAGE
blur = cv.GaussianBlur(resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blurred',blur)

#EDGE CASCADING
canny = cv.Canny(resized,125,175)
cv.imshow('Canny',canny)

#DILATING AN IMAGE
dilated = cv.dilate(resized,(3,3),iterations = 7)
cv.imshow('Dilated', dilated)

#ERODING AN IMAGE
eroded = cv.erode(dilated,(3,3),iterations=7)
cv.imshow('Eroded', eroded)

#CROPPING AN IMAGE
cropped = resized[50:200,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)