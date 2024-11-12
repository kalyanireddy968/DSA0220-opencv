import cv2
import numpy as np
kernel =np.zeros((5,5),np.uint8)
print(kernel)
path="C:/Users/HP/OneDrive/Pictures/pic1.jpg"
img=cv2.imread(path)
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",grayscale)
cv2.waitKey(0)


