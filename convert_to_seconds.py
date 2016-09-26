# -*- coding: utf-8 -*-
"""
Hours to Seconds Converter
Created on Sun Sep 25 16:00:39 2016

@author: Anon
"""

years = int(input("How many years?"))
days = int(input("How many days?"))
hours = int(input("How many hours?"))
minutes = int(input("How many minutes?"))
seconds = int(input("How many seconds?"))

def total_seconds(years, days, hours, minutes, seconds):
    total_seconds = (years * 24 *365 *3600) + (days * 24*3600) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

print ("There are %s seconds in %s years, %s days, %s hours, %s minutes, and %s seconds" % (total_seconds(years, days, hours, minutes, seconds), years, days, hours, minutes, seconds))
