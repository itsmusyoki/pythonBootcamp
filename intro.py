# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:54:54 2024

@author: Eagle
"""

import cv2

img = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

#grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("logo name", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
