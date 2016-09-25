# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:20:11 2016
Distance Calculator
@author: Anon
"""

#10.
import math


x0 = int(input("Please enter x coordinate of first point."))
y0 = int(input("Please enter y coordinate of first point."))
x1 = int(input("Please enter x coordinate of second point."))
y1 = int(input("Please enter y coordinate of second point."))


distance = math.sqrt((x0-x1)**2 + (y0 - y1)**2)
print ("The distance between (%s, %s) and (%s, %s) is %s" % (x0, x1, y0, y1, distance))2