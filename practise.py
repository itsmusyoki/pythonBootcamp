# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:16:04 2024

@author: Eagle
"""

#contour preprocessing
import cv2
import numpy as np 
from numpy.random import default_rng

#show contrast between normal and greyscale verstically
imgClear = cv2.imread("logo.png")
greyIm = cv2.imread("logo.png", cv2.IMREAD_GRAYSCALE)

#PUT  THEM VERTICALLY
Vstack = np.vstack((imgClear,greyIm), dtype=np.uint8)
Vstack = np.array(Vstack)








cv2.imshow("win logo", Vstack)
cv2.waitKey(0)
cv2.destroyAllWindows()