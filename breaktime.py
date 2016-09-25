# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:49:34 2016

@author: Anon
"""
import time
import webbrowser

breakInterval = int(input("How many minutes between each break?"))
numberOfBreaks = int(input("How many breaks?"))

breaks = 0
while breaks < numberOfBreaks:
    '''forces program to wait 10 seconds'''
    time.sleep(breakInterval * 60)

    '''opens the page on your default webbrowser'''
    webbrowser.open("https://www.youtube.com/watch?v=qe1ScoePqVA")
    breaks += 1
    print ("this program started " + time.ctime())
    print ("number of breaks: " + breaks)


