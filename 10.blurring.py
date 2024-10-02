import cv2 as cv

image = cv.imread('photos/nissan.jpg')
img = cv.resize(image, (500, 300), interpolation = cv.INTER_AREA)
cv.imshow('Original', img)

# AVERAGING
average = cv.blur(img,(3,3))
cv.imshow('Averaging', average)

# GAUSSIAN BLUR
gauss = cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# MEDIAN BLUR
median = cv.medianBlur(img,3)
cv.imshow('Median Blur', median)

#BILATERAL FILTERING
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Filter', bilateral)

cv.waitKey(0)