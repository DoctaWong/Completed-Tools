# -*- coding: utf-8 -*-
"""
Miles to feet calculator
Created on Sun Sep 25 16:27:08 2016

@author: Anon
"""
miles = float(input("How many miles?"))

def convert2kilometers(miles):
    kilometers = 1.6 * miles
    return kilometers

print ("There are %s kilometers in %s miles." % (convert2kilometers(miles), miles))
