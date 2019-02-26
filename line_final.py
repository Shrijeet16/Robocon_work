import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0) #read the video from the camera
# 0 for deafult camera
# 1 for external camaera and similarly

while (cap.isOpened()):

    ret , frame =  cap.read() #reading the elements of the video captured

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #converting normal image into grayscale

    blur = cv2.GaussianBlur(gray  , (5,5) , 0) #blurring the image with a 5X5 matrix without any scaling

    ret1 , th1 = cv2.threshold(blur , 35, 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #Using threshold , remove noise in the image

    ret2 , th2 = cv2.threshold(th1 , 127 , 255 , cv2.THRESH_BINARY_INV)

    #Using bianry inverse

    th2 = cv2.erode(th2 , None , iterations = 2)
    th2 = cv2.dilate(th2 , None , iterations = 2)

    h,w = frame.shape[:2]

    for i in range(0,4):
        _,contours ,hierarchy = cv2.findContours(th2[int((3-i)*h/4):int((4-i)*h/4),:],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find the contours

        if len(contours)>0 :

            contour_max = max(contours , key = cv2.contourArea) #finding the maximum contour on the basis of the area
        
            area_max_contour = cv2.contourArea(contour_max) #finding the area of the maximum contour

            if  area_max_contour >=500:
                #finding the moment and centroid
                M = cv2.moments(contour_max)
                
                cx = int(M['m10']/M['m00'])
                cy = int((M['m01']/M['m00'])+(3-i)*h/4)

                for j in contours:
                    cv2.drawContours(frame[int((3-i)*h/4):int((4-i)*h/4):],[j],-1,(0,255,0),1)


                cv2.circle(frame,(int(w/2),cy),5, (255,255,0), -1) #determining centre of each frame/4 according to the moment cy

                d = cx-int(w/2) #calculating offset for each part of the frame
                #offset is calculated between the x cordinate of centroid of the largest contour and centre of the frame
            
                
                cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
                cv2.circle(frame,(cx,cy),30,(255,0,0),2)
                
                print(d)

                #time.sleep(2)
            
                
    cv2.imshow("window1", frame)    
    #cv2.imshow("window" , th2)

    

    if cv2.waitKey(1) == 27 :
        print(h,w)
        break



cv2.destroyAllWindows()

cap.release()
    

