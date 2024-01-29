# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:17:00 2024

@author: Eagle
"""

#numpy nos to convert to open cv
#artificial data images
import numpy as np
import cv2
from numpy.random import default_rng

img = np.random.default_rng().integers(2, size=(200,200), dtype=np.uint8)
img = np.array(img*255)
print(img)



cv2.imshow("window logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
