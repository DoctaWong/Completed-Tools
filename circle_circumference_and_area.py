# -*- coding: utf-8 -*-
"""
Circle Circumference and Area
Created on Sun Sep 25 16:23:51 2016

@author: Anon
"""

import math

#5
radius = int(input("What is the radius of the circle?"))

def circumference(radius):
    circumference = (radius * 2) * math.pi
    return circumference

def area(radius):
    area = (radius ** 2) * math.pi
    return area

print ("A circle with a of radius of %s has a circumference of %s and an area of %s." % (radius, circumference(radius), area(radius)))