import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(1):
    # take each frame
    _, frame = cap.read()
    
    #convert BGR tho HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of bliue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    gris_claro = np.array([ 216, 216, 216 ])
    gris_oscuro = np.array([ 55, 55, 55])
    
    # Threshold the HSV image to get only blue colors
    #mask = cv.inRange(hsv,lower_blue, upper_blue)
    mask = cv.inRange(hsv, gris_claro, gris_oscuro)
    
    # Bitwise-AND mask anf original image
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)
    #k = cv.waitkey(5) & 0xFF
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()