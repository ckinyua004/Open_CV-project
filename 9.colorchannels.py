import cv2 as cv
import numpy as np

image = cv.imread('photos/nissan.jpg')
img = cv.resize(image, (500, 300), interpolation = cv.INTER_AREA)
cv.imshow('Original', img)

r,g,b = cv.split(img)
cv.imshow('Red', r)
cv.imshow('Green', g)
cv.imshow('Blue', b)

print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

merged = cv.merge([b,g,r])
blank = np.zeros(img.shape[:2] ,dtype='uint8')
cv.imshow('Blank image', blank)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('BLue', blue)
cv.imshow('GReen', green)
cv.imshow('REd', red)

cv.waitKey(0)