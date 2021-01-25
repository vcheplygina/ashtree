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
    s = np.array(s)                     #a stupid Python thing I guess I don't have a better solution for
    s2 = s * sample(scales, s.size) 
    
    return s2
    
# Adjusts the orientation of a segment
def adjust_angle(a, angles):
    a = np.array(a)
    a = a + sample(angles, a.size)
    return a
    

# Adjusts the x co-ordinate
def adjust_x(x, scale, angle):
    return x + scale * math.cos(math.radians(angle))


# Adjusts the y co-ordinate
def adjust_y(y, scale, angle):
    return y + scale * math.sin(math.radians(angle))
    