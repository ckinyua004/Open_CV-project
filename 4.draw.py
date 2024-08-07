import cv2 as cv
import numpy as np

# CREATING A BLANK IMAGE
blank = np.zeros((500,900,3), dtype='uint8')
cv.imshow('Blankkk',blank)

#PAINTING THE INAGE A CERTAIN COLOR
blank[:] = 180,25,76
cv.imshow('Green', blank)

#DRAWING A RECTANGLE
cv.rectangle(blank ,(0,0) ,(250,250) ,(24,34,6) ,thickness=3)
cv.imshow('Rectangle',blank)

#DRAW A CIRCLE
cv.circle(blank ,(blank.shape[1]//2, blank.shape[0]//2), 75,(255,0,76), thickness=3)
cv.imshow('Circle',blank)

#DRAW A LINE
cv.line(blank, (30,30), (180,180) , (0,45,180),thickness=3)
cv.imshow('Line',blank)

#DISPLAYING TEXT
cv.putText(blank, 'HALLO', (125,0), cv.FONT_HERSHEY_TRIPLEX, 1.2, (35,6,6), thickness=3)
cv.imshow('Text',blank)

cv.waitKey(0)