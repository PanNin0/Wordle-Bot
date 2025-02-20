# ------------------------------------

# Find Optimal

# A program to find the optimal starting word in wordle

# ------------------------------------

# Modules

import os
import time
import random as rnd

# ------------------------------------

# Config

config_bestOnly = True
config_trueOptimal = True

config_nonOpNum = 64

config_bestLetter = 'e'

# ------------------------------------

# Setting up the list of words

def createList():

    global wordList
    wordList = []

    fileOpen = open('word_list.txt', 'r') # Open the word_list.txt file
    file = fileOpen.readlines()

    for line in range(2315):
        
        nextWordRaw = str(file[line]) # Select the nth line of the txt file

        nextWord = nextWordRaw[0] + nextWordRaw[1] + nextWordRaw[2] + nextWordRaw[3] + nextWordRaw[4] # Isolate the first 5 letters of the nth word to remove the \n

        wordList.append(nextWord) # Add the nth line of the txt file to wordList[]

# ------------------------------------

# Variables and Functions

global possibleWords
global selectedWord

bestWord = ''
bestLeft = 2315

if (config_trueOptimal == True):
    config_nonOpNum = 2315

# Solving

def removeWords(guess):
    
    if guess != selectedWord: # Remove the previously guessed word UNLESS the guess was right

        index = possibleWords.index(guess)
        possibleWords.pop(index)

    # Repeat code for each letter to return either gray, yellow or green

    for letter in range(5):

        popAll = [] # Reset the list | this list is used to store all words that will be removed from the list of possible words

        if guess[letter] not in selectedWord: # Check if the nth letter is not in the correct word

            for item in range(len(possibleWords)):

                if guess[letter] in possibleWords[item]: # Check if the selected word has that letter in which case...

                    popAll.append(possibleWords[item]) # Append to word to popAll
        
        elif guess[letter] in selectedWord and selectedWord[letter] != guess[letter]: # Check if the nth letter is in the correct word BUT in the wrong spot

            for item in range(len(possibleWords)):

                if guess[letter] not in possibleWords[item]: # Check if the selected word does not have that letter in which case...

                    popAll.append(possibleWords[item]) # Append to word to popAll
        
        else: # Check if the nth letter is in the right spot

            for item in range(len(possibleWords)):

                if guess[letter] != (possibleWords[item])[letter]: # Check if the selected word does not have that letter in the nth spot in which case...

                    popAll.append(possibleWords[item]) # Append to word to popAll

        for rem in range(len(popAll)): # Loop for length of the popAll list

            index = possibleWords.index(popAll[rem]) # Find the position in the possible words list of the nth word
            possibleWords.pop(index) # Remove the nth word from possible words

# ------------------------------------

# Logic

createList() # Call the function to create the list of words

for check in range(2315):

    print(check)

    guessTotal = 0

    createList() # Call the function to create the list of words
    guess = wordList[check]

    if (config_bestOnly == False or config_bestLetter in guess):
        
        if (config_trueOptimal == True):

            for check2 in range(2315):

                createList() # Call the function to create the list of words
                possibleWords = wordList # Makes another list of words for words that are yet to be eliminated

                selectedWord = wordList[check2]

                removeWords(guess)
                guessTotal += len(possibleWords)
        
        else:

            for rep in range(config_nonOpNum):

                createList() # Call the function to create the list of words
                possibleWords = wordList # Makes another list of words for words that are yet to be eliminated

                selectedWord = rnd.choice(wordList)

                removeWords(guess)
                guessTotal += len(possibleWords)
        
        guessAvg = guessTotal / config_nonOpNum

        if (guessAvg <= bestLeft):

            bestLeft = guessAvg
            bestWord = guess

            print('New best word ' + str(bestWord) + ' word left average ' + str(bestLeft))

# ------------------------------------

input('Best word found! ' + str(bestWord) + ' with a score of ' + str(bestLeft) + '!')
print('Program complete! Closing in 5 minutes!')
time.sleep(300) # Set 5 minute timer to close the program