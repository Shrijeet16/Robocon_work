import cv2
import numpy as np


def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('clicked')
        print((x,y))
        print(frame[x][y])

cap = cv2.VideoCapture(0)




while(cap.isOpened()):
        
    ret , img = cap.read()

    img1 = cv2.medianBlur(img , 7)

    #21200
    #at 33 cm height of camera

    hsv = cv2.cvtColor(img1 , cv2.COLOR_BGR2HSV)

    lower_red = np.array([136,87,111] , np.uint8)

    upper_red = np.array([180,255,255] , np.uint8)

    red_range = cv2.inRange(hsv , lower_red ,upper_red)

    cv2.imshow("frame" , img)
    
    kernel = np.ones((5,5) , np.uint8)    

    img2 = cv2.bitwise_and(img1 , img1 , mask = red_range)

    res_closing = cv2.morphologyEx(img2 , cv2.MORPH_CLOSE , kernel) 

    _,contours , hierarchy = cv2.findContours(red_range ,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    


    if len(contours) >0:
        red_color = max(contours , key = cv2.contourArea)
    
        if (cv2.contourArea(red_color) > 17000):
            print("red_color   " + str(cv2.contourArea(red_color)))    
    
    

    

    cv2.imshow("result_closing" , res_closing)

    cv2.imshow("result" , img2)

        
    if(cv2.waitKey(1) == 27):
        break



cap.release()

cv2.destroyAllWindows()


