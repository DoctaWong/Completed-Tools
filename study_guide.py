# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 00:22:48 2016

Quiz
@author: Anon
"""
def startGame():
    difficulty()

def difficulty():
    user_input = input("Please select your difficulty by typing easy, medium, or hard")
    difficulty = user_input.lower()        
    if difficulty == 'easy':
        print ("The difficulty has been set to easy.")          
        return easyQuiz1()
    elif difficulty == 'medium':
        print ("The difficulty has been set to medium.")
        return mediumQuiz1()
    elif difficulty == 'hard':
        print ("The difficulty has been set to hard.")
        return hardQuiz1()
    else:
        print ("That is not a valid difficulty level")
        difficulty()
 
def difficultyFinished():
    print ("Congratulations! You have successfully answered all of the questions in this difficulty.")
    print ("Change difficulty?")    
    response = input("yes or no")
    if response == "yes" or response == "y" or response == "Y" or response == "Yes" or response == "YES":
        difficulty()
    elif response == "no" or response == "n" or response == "N" or response == "No" or response == "NO":
        print ("Thank you for playing.")
    else:
        print ("Sorry I did not understand your input")
        difficultyFinished()    

def easyQuiz1():            
    print ("Using _______  can allow a performer to hear the difference between a given pitch and the pitch he or she is producing.")
    response = input("tuners or drones?")
    if response == "drones":
        print ("Correct!")
        easyQuiz2()
    elif response == "tuners":
        print ("Incorrect.  Tuners allow us to see pitch discrepancies but do not allow us to hear them.")
        easyQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        easyQuiz1()
        
def easyQuiz2():
    print ("The pitch of a brass instrument ______ when temperature increases.")
    response = input("raises or lowers?")
    if response == "raises":
        print ("Correct!")
        easyQuiz3()
    elif response == "lowers":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        easyQuiz2()
    else:
        print ("Sorry, that was not a valid response.")
        easyQuiz2()

def easyQuiz3():  
    print ("Higher frequencies of sound vibrations result in a ______  pitch.")
    response = input("higher or lower?")
    if response == "higher":
        print ("Correct!")
        easyQuiz4()
    elif response == "lower":
        print ("Incorrect.  Higher frequencies of sound vibrations result in higher pitch.")
        easyQuiz3()
    else:
        print ("Sorry, that was not a valid response.")
        easyQuiz3()
        
def easyQuiz4():     
    print ("The frequency of beats ______ (increases or decreases) as two pitches are further apart, as long as the two pitches are less than a quarter tone apart.")
    response = input("increases or decreases?")
    if response == "increases":
        print ("Correct!")
        easyQuiz5()
    elif response == "decreases":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        easyQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        easyQuiz4()
        
def easyQuiz5():
    print ("Increasing the tubing length of a wind or brass instrument ______ its pitch.")
    response = input("raises or lowers?")
    if response == "lowers":
        print ("Correct!  Increasing tubing length results in lower frequencies")
        difficultyFinished()              
    elif response == "raises":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        easyQuiz5()
    else:
        print ("Sorry, that was not a valid response.")
        easyQuiz5()

            
def mediumQuiz1():
    print ("The seventh degree in a major scale is often referred to as the leading tone.  This pitch is usually ______")
    response = input("raised or lowered?")
    if response == "raised":
        print ("Correct!")
        mediumQuiz2()
    elif response == "lowered":
        print ("Incorrect.  Leading tones are typically lowered.")
        mediumQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz1()

def mediumQuiz2():  
    print ("Metal instruments warm up and cool off ______ than wooden instruments.")
    response = input("faster or slower?")
    if response == "faster":
        print ("Correct! Metal instruments contract at higher temperatures.  This is important to know because the pitch of flutes and brass instruments tend to rise over the course of a performance.")
        mediumQuiz3()
    elif response == "slower":
        print ("Incorrect.  Metal instruments contract at higher temperatures, resulting in increased pitch.")
        mediumQuiz2()
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz2() 

def mediumQuiz3():  
    print ("A minor third needs to be ______ from equal temperament to achieve just intonation.")
    response = input("raised or lowered?")
    if response == "raised":
        print ("Correct! Minor thirds need to be raised approximately 16 cents from equal temperament to achieve just intonation.")
        mediumQuiz4()
    elif response == "lowered":
        print ("Incorrect.")
        mediumQuiz3()
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz3() 
      
def mediumQuiz4():  
    print ("A major third needs to be ______ (raised or lowered) from equal temperament to achieve just intonation.")
    response = input("raised or lowered?")
    if response == "lowered":
        print ("Correct! Major thirds need to be lowered approximately 14 cents from equal temperament to achieve just intonation.")
        difficultyFinished() 
    elif response == "raised":
        print ("Incorrect.")
        mediumQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz4() 
        
def hardQuiz1():  
    print ("Developing brass players tend to play ______ when performing a crescendo.")
    response = input("sharp or flat?")
    if response == "sharp":
        print ("Correct! Developing players often don't increase the size of the aperture enough when performing a crescendo, resulting in a raised pitch.")
        hardQuiz2()
    elif response == "flat":
        print ("Incorrect.")
        hardQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        hardQuiz1()

def hardQuiz2():  
    print ("Straight mutes tend to ______ (raise or lower) pitch on brass instruments. ")
    response = input("raise or lower?")
    if response == "raise":
        print ("Correct!")
        hardQuiz3() 
    elif response == "lower":
        print ("Incorrect.")
        hardQuiz2()
    else:
        print ("Sorry, that was not a valid response.")
        hardQuiz2()
    
def hardQuiz3():  
    print ("Cup mutes tend to ______ (raise or lower) pitch in brass instruments")
    response = input("raise or lower?")
    if response == "lower":
        print ("Correct!")
        hardQuiz4() 
    elif response == "raise":
        print ("Incorrect.")
        hardQuiz3()
    else:
        print ("Sorry, that was not a valid response.")
        hardQuiz3()
        
def hardQuiz4():  
    print ("In performance, higher pitched instruments sound ______ (louder or softer) than lower pitched instruments.")
    response = input("louder or softer?")
    if response == "louder":
        print ("Correct!  The human ear can hear higher pitched instruments more clearly than lower pitched instruments")
        print ("Congratulations! You have completed this game on the highest difficulty!") 
    elif response == "softer":
        print ("Incorrect.")
        hardQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        hardQuiz4()

startGame()     
