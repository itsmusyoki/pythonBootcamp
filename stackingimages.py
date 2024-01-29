# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:42:29 2024

@author: Eagle
"""

import numpy as np
import cv2

img = cv2.imread("logo.png")
original = cv2.imread("logo.png")
#gray
grayIm = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
npth = np.array(grayIm)
#Binarizing
ret, thresh = cv2.threshold(grayIm, 0,255, cv2.THRESH_BINARY)
npth = np.array(thresh)


#extracting contours
contours, h = cv2.findContours(thresh, cv2.RETR_CCOMP , cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255,0,255),1)


#stack vertically
vstack = np.vstack((img,original))
vstack = np.array(vstack)


cv2.imshow("windows", vstack)
cv2.waitKey(0)
cv2.destroyAllWindows()
