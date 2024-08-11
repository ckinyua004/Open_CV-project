import cv2 as cv
import numpy as np

nissan_1 = cv.imread('photos/nissan.jpg')
nissan = cv.resize(nissan_1, (700,400), interpolation = cv.INTER_AREA)
cv.imshow('NISSAN', nissan)

gray = cv.cvtColor(nissan, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY' ,gray)

canny = cv.Canny(nissan_1, 125, 175)
cv.imshow('CANNY', canny)

ret,thresh = cv.threshold(nissan,125,255, cv.THRESH_BINARY)
cv.imshow('THRESH', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.waitKey(0)