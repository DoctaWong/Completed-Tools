# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:50:46 2016
Interest Calculator
@author: DoctaWong
"""

pv = round(float(input("What is the present value in dollars?")), 2)
ar = float(input("What is the percent annual interest rate?"))
n = float(input("How many times is the interest compounded per year??"))
y = float(input("How many years?"))

def fv(pv, ar, y):
    fv = pv * (1.0 + (ar/100)/n)**(n*y)
    return fv

A = round(fv(pv, ar, y), 2)

print ("$%s with an annual interest rate of %s percent compounded %s times per year will be $%s in %s years." % (pv, ar, n, A, y))
