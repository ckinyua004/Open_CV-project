import cv2 as cv

image = cv.imread('photos/NISSAN.jpg')
cv.imshow('Image', image)

img = cv.resize(image, (700,400) , interpolation = cv.INTER_CUBIC)
cv.imshow('Img', img)

# RGB TO B&W
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR TO LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# RGB TO HSV
rgb2bgr = cv.cvtColor(rgb , cv.COLOR_RGB2BGR)
bgr2hsv = cv.cvtColor(rgb2bgr, cv.COLOR_BGR2HSV)
cv.imshow('RGB TO HSV' ,bgr2hsv)

cv.waitKey(0)