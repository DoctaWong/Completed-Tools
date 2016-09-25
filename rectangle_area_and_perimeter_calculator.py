# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:04:24 2016

@author: Anon
"""

height = float(input("What is the height of the rectangle?"))
width = float(input("What is the width of the rectangle?"))

def perimeter(height, width):
    perimeter = 2*width + 2*height
    return perimeter

def area(height, width):
    area = width * height
    return area

print ("A rectangle with a height of %s and a width of %s has an area of %s and a perimeter of %s." % (height, width, area(height, width), perimeter(height, width)))