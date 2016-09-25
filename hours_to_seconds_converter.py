# -*- coding: utf-8 -*-
"""
Hours to Seconds Converter
Created on Sun Sep 25 16:00:39 2016

@author: Anon
"""


hours = int(input("How many hours?"))
minutes = int(input("Minutes?"))
seconds = int(input("Seconds?"))

def total_seconds(hours,minutes,seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

print ("There are %s seconds in %s hours, %s minutes, and %s seconds" % (total_seconds(hours, minutes, seconds), hours, minutes, seconds))
