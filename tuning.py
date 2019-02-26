import cv2
import numpy as np
import PIL

global max_value
max_value = 255
windowname = "tuning"


def pass_operation():
    pass


def createtrackbar():
    cv2.createTrackbar('thresholding_value',windowname,0,255,pass_operation)
    cv2.createTrackbar('edge_max_value',windowname,0,255,pass_operation)
    cv2.createTrackbar('edge_min_value',windowname,0,255,pass_operation)

def thresholding():
    ret , thresholded_image = cv2.threshold(blur,thresholding_value,max_value,cv2.THRESH_BINARY)
    return thresholded_image


def edgedetection_canny():
    cv2.Canny(image , minvalue , maxvalue) 


def brightness():
    capture.set(10,30)
    print(capture.get(10) )

#-----------------------------------------------------------------------------
capture = cv2.VideoCapture(0)
createtrackbar()

if(capture.isOpened == False):
    capture.open()

cv2.namedWindow(windowname)

while(capture.isOpened()):

    return_capture,image = capture.read()
    blur = cv2.GaussianBlur(image ,(7,7),1,1)
    
    #thresholding
    #image = thresholding()
    thresholding_value = cv2.getTrackbarPos('h_max',windowname)
    #cv2.imshow("thresholding" , thresholding())
    cv2.imshow(windowname , image)


    #edgedetection
    #edgedetection_canny()

    #brightness
    #brightness()

    if(cv2.waitKey(1)==27):
        capture.release()
        cv2.destroyAllWindows()
        break
    
