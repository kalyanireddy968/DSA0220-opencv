import cv2
import numpy as np
cap=cv2.VideoCapture("C:/Users/HP/Videos/3320544-hd_1920_1080_30fps.mp4")
if(cap.isOpened()== False):
    print("error opened video file")
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow("frame",frame)
        if cv2.waitKey(250)& 0xFF==ord('q'):
            break
    else:
        break
cap.release()

    
