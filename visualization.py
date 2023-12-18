#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:20:54 2023

@author: musyoki
"""

import matplotlib.pyplot as plt

xAxis=[3,5,7,11,6]

yAxis=[4,22,5,5,6]
#plot scatter bar

plt.scatter(xAxis,yAxis)
plt.xlabel("no of occurrence")
plt.ylabel("day of month")


plt.show() 