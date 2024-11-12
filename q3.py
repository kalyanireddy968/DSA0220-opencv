import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="C:/Users/HP/OneDrive/Pictures/pic1.jpg"
img=cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(7,7),0)
canny=cv2.Canny(blur,100,200)
cv2.imshow("canny",canny)
cv2.waitKey(0)
