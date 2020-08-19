import numpy as np
import cv2

img = cv2.imread("image.jpg",1)

#scale
img_half = cv2.resize(img,(600,600))
img_stretch = cv2.resize(img,(600,600))
img_strech_near = cv2.resize(img,(600,600),interpolation=cv2.INTER_NEAREST)

cv2.imshow("Half",img_half)
cv2.imshow("Strech",img_stretch)
cv2.imshow("Strech near",img_strech_near)

#Rotation
M = cv2.getRotationMatrix2D((0,0), -30, 1)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated",rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()