# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:50:46 2016
Interest Calculator
@author: Wilson Wong
"""

pv = round(float(input("What is the present value in dollars?")), 2)
ar = float(input("What is the percent annual interest rate?"))
n = float(input("How many times is the interest compounded per year??"))
y = float(input("How many years?"))


def fv(pv, ar, n, y):
    '''
    Takes the parameters present value, annual interest rate,
	times compounded per year, and number of years.
    Returns the dollar value after compound interest is applied.
    '''
    try:
        finalValue = pv * (1.0 + (ar/100)/n)**(n*y)
        if n < 0:
            raise ValueError("N must be a positive number!")
        elif y < 0:
            raise ValueError("Number of years must be positive!")
        else:
            return round(finalValue, 2)
    except ZeroDivisionError:
        print("n must be a postive number!")
    except TypeError:
        print("All values must be positive numbers!")
    except OverflowError:
        print("Number is too large to compute!")
print ("$%s with an annual interest rate of %s percent"
       "compounded %s times per year will be $%s in %s years."
       % (pv, ar, n, fv(pv, ar, n, y), y))

'''
#Test Suite
print(fv(1000, 5, 1, 10))
#testing for negative numbers

print(fv(-1000, 5, 1, 10))
print(fv(1000,-5,1,10))
print(fv(1000,5,-5,10))
print(fv(1000,5,1 1,-10))

#testing for zeroes
print(fv(0, 5, 1, 10))
print(fv(1000,0,1,10))
print(fv(1000,5,0,10))
print(fv(1000,5, 1,0))

#testing for non-numbers
print(fv('a',5,1,10))
print(fv(1000,'a',1,10))
print(fv(1000, 5,'a',10))
print(fv(1000,5,1,'a'))

#testing for fractions
print(fv(0.5,5,1,10))
print(fv(1000,0.5,1,10))
print(fv(1000, 5,0.5,10))
print(fv(1000,5,1,0.5))

#testing for very large values
print(fv(10**10,5,1,10))
print(fv(1000,10**10,1,10))
print(fv(1000, 5,10**10,10))
print(fv(1000,5,1,10**10))

#testing for very small values
print(fv(1/(10**10),5,1,10))
print(fv(1000,1/(10**10),1,10))
print(fv(1000, 5,1/(10**10),10))
print(fv(1000,5,1,1/(10**10)))
'''
