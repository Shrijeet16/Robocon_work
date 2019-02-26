import cv2
import numpy as np

min_arearequire_white = 4000
Dilation_type = "square"
#kernel=1

def Pass_operation():
    pass

def kernel_type(Dilation_type , size ):

    if Dilation_type == "square" :
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(size ,size))
        return kernel
    
    elif Dilation_type == "ellipse" :
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(size ,size))
        return kernel
    
    elif Dilation_type == "cross" :
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size ,size))
        return kernel
    else:
        return None

capture = cv2.VideoCapture(0)
height_window , width_window = 3 , 4

capture.set(height_window,240)
capture.set(width_window,360)

#print(h,w)

if(capture.isOpened == False):
    capture.open()
    
windowname = "HSV_values"

cv2.namedWindow(windowname)

cv2.createTrackbar('h_max',windowname,0,179,Pass_operation)
cv2.createTrackbar('h_min',windowname,0,179,Pass_operation)
cv2.createTrackbar('s_min',windowname,0,255,Pass_operation)
cv2.createTrackbar('s_max',windowname,0,255,Pass_operation)
cv2.createTrackbar('v_min',windowname,0,255,Pass_operation)
cv2.createTrackbar('v_max',windowname,0,255,Pass_operation)


while(capture.isOpened()):

    return_capture,image = capture.read()
    #cv2.imshow("reference" , image)
    
    image = cv2.medianBlur(image ,7 )
    hsv = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
    
    h_max = cv2.getTrackbarPos('h_max',windowname)
    h_min = cv2.getTrackbarPos('h_min',windowname)
    s_max = cv2.getTrackbarPos('s_max',windowname)
    s_min = cv2.getTrackbarPos('s_min',windowname)
    v_max = cv2.getTrackbarPos('v_max',windowname)
    v_min = cv2.getTrackbarPos('v_min',windowname)

    lower_white = np.array([0,0,200],np.uint8) #values are given for white
    upper_white = np.array([180 , 20, 255],np.uint8)

    white = cv2.inRange(hsv , lower_white , upper_white)
    white = cv2.erode(white , kernel_type(Dilation_type ,7) ,iterations =2)
    white = cv2.dilate(white ,kernel_type(Dilation_type ,7) , iterations = 3)
    
    result_white = cv2.bitwise_and(image , image , mask = white)

    _,contours , hierarchy = cv2.findContours(white.copy() ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    

    if len(contours) >0:
        white_color = max(contours , key = cv2.contourArea)
    
        if (cv2.contourArea(white_color) > min_arearequire_white):
            print("white_color   " + str(cv2.contourArea(white_color)))    
    
    cv2.imshow(windowname ,result_white )        

    if(cv2.waitKey(1) == 27):
        capture.release()
        cv2.destroyAllWindows()
        break
