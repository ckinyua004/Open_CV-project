import cv2 as cv
import numpy as np

monac = cv.imread('photos/monaco.jpg')

monaco = cv.resize(monac, (700,400), interpolation = cv.INTER_LINEAR)
cv.imshow('Monaco', monaco)

#translation

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(monaco, 100 ,100)
cv.imshow('Translated',translated)

# ROTATION
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(monaco,45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)
    