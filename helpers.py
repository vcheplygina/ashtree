# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 09:58:17 2021

@author: vcheplyg
"""
import math  
from random import sample 
import numpy as np

# Converts degrees to radians. For illustratory purposes, #we use math.radians(degree) instead
#def radians(degree):
#    return 2 * math.pi * degree / 360   


# Adjusts the length of a segment
def adjust_scale(s, scales):
    s2 = sample(scales, 1) 
    s3 = s * s2[0]
    print(s3)
    return s3
    
# Adjusts the orientation of a segment
def adjust_angle(a, angles):
    a = a + sample(angles, 1)
    return a[0]
    

# Adjusts the x co-ordinate
def adjust_x(x, scale, angle):
    return x + scale * math.cos(math.radians(angle))


# Adjusts the y co-ordinate
def adjust_y(y, scale, angle):
    return y + scale * math.sin(math.radians(angle))
    