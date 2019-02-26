import cv2
import numpy as np
import random


cap = cv2.VideoCapture(0)

while(1):


    ret , frame = cap.read()

    output = cv2.medianBlur(frame ,9)
    #arguments image and kernel or matrix size

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)


        #in hsv has values ranging from 0 to 180
        #s and v have values from 0 to 255

        #for red color hue values of red ranges from 0 to 10  and 160  to 180

    lower_red = np.array([175,100,100])
    upper_red = np.array([189,255,255])

    range_red = cv2.inRange(hsv , lower_red , upper_red)

    res = cv2.bitwise_and(frame, frame , mask = range_red)

    cv2.imshow("frame" , frame)

    cv2.imshow("range_blue" , range_red)

    cv2.imshow("result",  res)

    cv2.imshow("output",output)
    if(cv2.waitKey(1) == 27):

        break
    

cv2.destroyAllWindows()

cap.release()
