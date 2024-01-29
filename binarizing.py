# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:55:56 2024

@author: Eagle
"""

import cv2
import numpy as np



img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)
print(np.unique(img))
#CREATE 2 VARS 
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)

print(np.unique(thresh))

cv2.imshow("title", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()