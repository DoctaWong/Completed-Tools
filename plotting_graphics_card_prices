# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:52:57 2016

@author: DoctaWong
"""
'''
x = cards 
y = performance
'''

import pylab

#assigns x and y to price and performance values, and plots their values
x = [90, 130, 160, 240, 380, 580]
y = [3253, 5209, 5872, 8875, 11065, 12048]

pylab.plot(x,y)
pylab.title('Video Card Performance per Dollar, 2016')
pylab.ylabel('PassMark Score')
pylab.xlabel('Dollars Spent')
a, b = pylab.polyfit(x, y, 1)
predicted_performance = a*pylab.array(x) + b
pylab.plot(x, predicted_performance)

