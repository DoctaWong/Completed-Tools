# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 00:22:48 2016

Quiz
@author: Anon
"""
def startGame():
    difficulty()

def difficulty():
    '''Prompts user to select difficulty and outputs the first question in the corresponding difficulty'''
    
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
    '''Prompted at the end of each difficulty. Asks if user wants to play at a new difficulty'''
    
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

'''
The functions below are all used to ask different questions in the quiz.  Since the input prompt
for each question is different as is the output for an incorrect answer, I've decided to make each 
question a separate function.  Each function should be less than 18 lines each, though.
'''

score = 0

def easyQuiz1():            
    print ("Using _______  can allow a performer to hear the difference between a given pitch and the pitch he or she is producing.")
    response = input("tuners or drones?")
    count = 0

    if response == "drones":
        print ("Correct!")
        print ("Using drones can allow a performer to hear the difference between a given pitch and the pitch he or she is producing.")
        if count == 0:
            score += 1
        print ("Score: " + str(score))
        easyQuiz2()
        
    elif response == "tuners":
        print ("Incorrect.  Tuners allow us to see pitch discrepancies but do not allow us to hear them.")
        count += 1
        easyQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        easyQuiz1()
        
def easyQuiz2():
    print ("The pitch of a brass instrument ______ when temperature increases.")
    response = input("raises or lowers?")
    count = 0
    if response == "raises":
        print ("Correct!")
        print ("The pitch of a brass instrument raises when temperature increases.")
        if count == 0:
            score += 1
        print ("Score: " + str(score))
        easyQuiz3()
    elif response == "lowers":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        count += 1
        easyQuiz2()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        easyQuiz2()

def easyQuiz3():  
    print ("Higher frequencies of sound vibrations result in a ______ pitch.")
    response = input("higher or lower?")
    count = 0
    if response == "higher":
        print ("Correct!")
        print ("Higher frequencies of sound vibrations result in a higher pitch.")
        if count == 0:
            score += 1
        print ("Score: " + str(score))
        easyQuiz4()
    elif response == "lower":
        print ("Incorrect.  Higher frequencies of sound vibrations result in higher pitch.")
        count += 1
        easyQuiz3()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        easyQuiz3()
        
def easyQuiz4():     
    print ("The frequency of beats ______ as two pitches are further apart, as long as the two pitches are less than a quarter tone apart.")
    response = input("increases or decreases?")
    count = 0
    if response == "increases":
        print ("Correct!")
        print ("The frequency of beats increases as two pitches are further apart, as long as the two pitches are less than a quarter tone apart.")
        if count == 0:
            score += 1
        print ("Score: " + str(score))
        easyQuiz5()
    elif response == "decreases":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        count += 1
        easyQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        easyQuiz4()
        
        
def easyQuiz5():
    print ("Increasing the tubing length of a wind or brass instrument ______ its pitch.")
    response = input("raises or lowers?")
    count = 0
    if response == "lowers":
        print ("Correct!")
        print ("Increasing the tubing length of a wind or brass instrument lowers its pitch.")
        if count == 0:
            score += 1
        print ("You answered " + str(score) + " of 5 questions correctly at this difficulty.")
        difficultyFinished()              
    elif response == "raises":
        print ("Incorrect.  Higher temperatures causes metal to shrink, resulting in a higher pitch.")
        count += 1
        easyQuiz5()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        easyQuiz5()
        
        
def mediumQuiz1():
    print ("The seventh degree in a major scale is often referred to as the leading tone.  This pitch is usually ______")
    response = input("raised or lowered?")
    count = 0
    score = 0
    if response == "raised":
        print ("Correct!")
        print ("The seventh degree in a major scale is often referred to as the leading tone.  This pitch is usually raised.")
        if count == 0:
            score += 1
        print ("Score: " + score)
        mediumQuiz2()
    elif response == "lowered":
        print ("Incorrect.  Leading tones are typically lowered.")
        count += 1
        mediumQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        mediumQuiz1()
        

def mediumQuiz2():  
    print ("Metal instruments warm up and cool off ______ than wooden instruments.")
    response = input("faster or slower?")
    if response == "faster":
        print ("Correct!")
        print ("Metal instruments warm up and cool off faster than wooden instruments.")
        if count == 0:
            score += 1
        print ("Score: " + score)
        mediumQuiz3()
    elif response == "slower":
        print ("Incorrect.  Metal instruments contract at higher temperatures, resulting in increased pitch.")
        mediumQuiz2()
        count += 1
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz2() 
        count += 1

def mediumQuiz3():  
    print ("A minor third needs to be ______ from equal temperament to achieve just intonation.")
    response = input("raised or lowered?")
    if response == "raised":
        print ("A minor third needs to be raised from equal temperament to achieve just intonation.")
        if count == 0:
            score += 1
        print ("Score: " + score)
        mediumQuiz4()
    elif response == "lowered":
        print ("Incorrect.")
        mediumQuiz3()
        count += 1
    else:
        print ("Sorry, that was not a valid response.")
        mediumQuiz3() 
        count += 1
      
def mediumQuiz4():  
    print ("A major third needs to be ______ from equal temperament to achieve just intonation.")
    response = input("raised or lowered?")
    if response == "lowered":
        print ("A major third needs to be lowered from equal temperament to achieve just intonation.")
        if count == 0:
            score += 1
        print ("You answered " + score + " of 5 questions correctly at this difficulty.")
        difficultyFinished() 
                
    elif response == "raised":
        print ("Incorrect.")
        count += 1
        mediumQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        mediumQuiz4() 
        
def hardQuiz1():  
    print ("Developing brass players tend to play ______ when performing a crescendo.")
    response = input("sharp or flat?")
    if response == "sharp":
        print ("Correct!")
        print ("Developing brass players tend to play sharp when performing a crescendo.")
        if count == 0:
            score += 1
        print ("Score: " + score)
        hardQuiz2()
    elif response == "flat":
        print ("Incorrect.")
        count += 1
        hardQuiz1()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        hardQuiz1()

def hardQuiz2():  
    print ("Straight mutes tend to ______ pitch on brass instruments.")
    response = input("raise or lower?")
    if response == "raise":
        print ("Correct!")
        print ("Straight mutes tend to raise pitch on brass instruments.")
        if count == 0:
            score += 1
        print ("Score: " + score)
        hardQuiz3() 
    elif response == "lower":
        print ("Incorrect.")
        count += 1
        hardQuiz2()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        hardQuiz2()
    
def hardQuiz3():  
    print ("Cup mutes tend to ______  pitch in brass instruments")
    response = input("raise or lower?")
    if response == "lower":
        print ("Correct!")
        print ("Cup mutes tend to lower pitch in brass instruments")
        if count == 0:
            score += 1
        print ("Score: " + score)
        hardQuiz4() 
    elif response == "raise":
        print ("Incorrect.")
        count += 1
        hardQuiz3()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        hardQuiz3()
        
def hardQuiz4():  
    print ("In performance, higher pitched instruments sound ______ than lower pitched instruments.")
    response = input("louder or softer?")
    if response == "louder":
        print ("In performance, higher pitched instruments sound louder than lower pitched instruments.")
        print ("Congratulations! You have completed this game on the highest difficulty!") 
        if count == 0:
            score += 1
        print ("You answered " + score + " of 5 questions correctly at this difficulty.")
    elif response == "softer":
        print ("Incorrect.")
        count += 1
        hardQuiz4()
    else:
        print ("Sorry, that was not a valid response.")
        count += 1
        hardQuiz4()

startGame()     
