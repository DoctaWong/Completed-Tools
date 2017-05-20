# -*- coding: utf-8 -*-
"""
Opens a user specified web link after a user specified amount of time.
Created on Sat Sep 24 20:49:34 2016

@author: Anon
"""
import time
import webbrowser

breakInterval = int(input("How many minutes between each break?"))
numberOfBreaks = int(input("How many breaks?"))
link = input("Please enter the URL of the webpage you wish to open")

breaks = 0
while breaks < numberOfBreaks:
    '''forces program to wait 10 seconds'''
    time.sleep(breakInterval * 60)

    '''opens the page on your default webbrowser'''
    webbrowser.open(link)
    breaks += 1
    print ("this program started " + time.ctime())
    print ("number of breaks: " + breaks)

