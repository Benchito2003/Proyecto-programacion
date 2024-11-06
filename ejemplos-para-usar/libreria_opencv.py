import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while(1):
    # take each frame
    _, frame = cap.read()
    
    #convert BGR tho HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    gris_oscuro = np.array([ 55, 55, 55])
    gris_claro = np.array([ 216, 216, 216 ])
    
    verde_oscuro = np.array([110,50,50])
    verde_claro = np.array([0, 0, 255])
    
    # Threshold the HSV image to get only blue colors
    #mask = cv.inRange(hsv,lower_blue, upper_blue)
    mask = cv.inRange(hsv, verde_oscuro, verde_claro)
    
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