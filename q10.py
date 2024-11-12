import cv2
import numpy as np
path="C:/Users/HP/OneDrive/Pictures/pic1.jpg"
img=cv2.imread(path)
rotate=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("rot",rotate)
cv2.waitKey(0)
