import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="C:/Users/HP/OneDrive/Pictures/pic1.jpg"
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),0)
canny=cv2.Canny(blur,100,200)
img_dilate=cv2.dilate(canny,kernel,iterations=10)
img_eroded=cv2.erode(img_dilate,kernel,iterations=5)
cv2.imshow("erode",img_eroded)
cv2.waitKey(0)


                      
                  
