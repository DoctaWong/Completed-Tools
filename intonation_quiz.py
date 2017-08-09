# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 00:22:48 2016

Quiz
@author: Anon
"""

'''
The functions below are all used to ask different questions in the quiz.  Since the input prompt
for each question is different as is the output for an incorrect answer, I've decided to make each
question a separate function.  Each function should be less than 18 lines each, though.
'''

questions = [['A performer to hear the difference between a given pitch and the pitch he or she is producing using ______.',
              'When temperature increases, the pitch of a brass instrument ______.',
              'Higher frequencies of sound vibrations result in a ______ pitch.',
              'The frequency of beats ______ as two pitches are further apart, as long as the two pitches are less than a quarter tone apart.',
  "Increasing the tubing length of a wind or brass instrument ______ its pitch."],
['The seventh degree in a major scale is often referred to as the leading tone.  This pitch is usually ______.',
 'Metal instruments warm up and cool off ______ than wooden instruments.',
 'A minor third needs to be ______ from equal temperament to achieve just intonation.',
 'A major third needs to be ______ from equal temperament to achieve just intonation.'],
 ['Developing brass players tend to play ______ when performing a crescendo.',
  'Straight mutes tend to ______ pitch on brass instruments.',
  'Cup mutes tend to ______  pitch in brass instruments',
  'In performance, higher pitched instruments sound ______ than lower pitched instruments.']]

answers = [['drones', 'raises', 'higher', 'increases', 'lowers'],
           ['raised', 'faster', 'raised', 'lowered'],
           ['sharp', 'raise', 'lower', 'louder']]

choices = [['tuners or drones?', 'rises or falls?', 'higher or lower?', 'increases or decreases?', 'raises or lowers?'],
           ['raised or lowered?', 'faster or slower?', 'raised or lowered?', 'raised or lowered?'],
           ['sharp or flat?', 'raise or lower?', 'raise or lower?', 'louder or softer?']]

difficulty_levels = ['easy', 'medium', 'hard']


def startGame():
    difficulty()


def difficulty():
    '''
    Prompts user to select difficulty
    Runs the game loop for the corresponding difficulty
    '''
    user_input = input("Please select your difficulty by typing easy, medium, or hard: ")
    difficulty = user_input.lower()
    if difficulty == 'easy':
        print ("The difficulty has been set to easy.")
        return playGame(questions[0], answers[0], choices[0])
    elif difficulty == 'medium':
        print ("The difficulty has been set to medium.")
        return playGame(questions[1], answers[1], choices[1])
    elif difficulty == 'hard':
        print ("The difficulty has been set to hard.")
        return playGame(questions[2], answers[2], choices[2])
    else:
        print ("That is not a valid difficulty level")
        difficulty()


def difficultyFinished():
    '''Prompted at the end of each difficulty. Asks if user wants to play at a new difficulty'''
    print ("Play again?")    
    response = input("yes or no")
    accept_yes = ['y', 'yes']
    accept_no = ['n', 'no']
    if response.lower() in accept_yes:
        difficulty()
    elif response.lower() in accept_no:
        print ("Thank you for playing.")
    else:
        print ("Sorry I did not understand your input")
        difficultyFinished()


def playGame(questions, answers, choices):
    '''Runs the game loop for the selected difficulty'''
    n = 0
    correct = 0
    for e in questions:
        print(e)
        response = input(choices[n])
        if response.lower() == answers[n]:
            print("Correct!")
            correct += 1
            n += 1
        else:
            print("Incorrect.")
            n += 1
    print("You answered " + str(correct) + " questions correctly.")
    difficultyFinished()


startGame()
