import numpy as np
import cv2

img = cv2.imread('images.jpg',0)
cv2.imshow("Original",img)

# Basic Binary Threshold
ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary",thresh_basic)

# Adaptive Threshold
thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Apadtive Threshold', thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()