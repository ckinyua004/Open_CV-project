import cv2 as cv

dubai_1 = cv.imread('photos/dubai.jpg')
cv.imshow('Dubai_1', dubai_1)

dubai = cv.resize(dubai_1 ,(900, 600) , interpolation = cv.INTER_CUBIC)
cv.imshow('DUBAI', dubai)

#1
blur = cv.GaussianBlur(dubai, (5,5), 0)
cv.imshow('BLUR', blur)

#2 MEDIAN_BLUR
m_blur = cv.medianBlur(dubai, 5)
cv.imshow('Median Blur', m_blur)

#3 BILATERAL FILTERING
b_filter = cv.bilateralFilter(dubai, 9,75,75)
cv.imshow('Bilateral Filter', b_filter)

#4 N0N L0CAL/ DEN0ISING
denoised =  cv.fastNlMeansDenoisingColored(dubai, None ,10, 10, 7,21)
cv.imshow('Non local',denoised)

cv.waitKey(0)