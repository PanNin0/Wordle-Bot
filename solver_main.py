# ------------------------------------

# Wordle Solver v1.0

# A program to solve and emulate wordle

# ------------------------------------

# Modules

import random as rnd
import os
import time

# ------------------------------------

# Config

config_manual = False # Manual mode of the program
config_possible = False # Whether or not the program will print all current possible words
config_optimal = True # Whether or not the bot will start with the most optimal word
config_keyboard = True # Whether or not the keyboard of each letters state will be shown

config_repeat = 1 # The number of times the program will run through
config_maxGuesses = 6 # The number of guesses you're allowed to make
config_speed = 1 # How long the program will wait before guessing again
global config_skin
config_skin = 0 # Current selected skin

config_optimalWord = 'raise' # The most optimal word for the bot to start with

global skin

class skin: # Skins are the colors displayed on the keyboard

    neutral = ['\033[0m', '\033[0m']
    green = ['\033[32m', '\033[32m']
    yellow = ['\033[33m', '\033[32m']
    gray = ['\033[30m', '\033[31m']

# ------------------------------------

# Setting up the list of words

def createList():

    global wordList
    wordList = []

    global guessList
    guessList = []

    fileOpen = open('word_list.txt', 'r') # Open the word_list.txt file
    file = fileOpen.readlines()

    for line in range(2315):
        
        nextWordRaw = str(file[line]) # Select the nth line of the txt file

        nextWord = nextWordRaw[0] + nextWordRaw[1] + nextWordRaw[2] + nextWordRaw[3] + nextWordRaw[4] # Isolate the first 5 letters of the nth word to remove the \n

        wordList.append(nextWord) # Add the nth line of the txt file to wordList[]
    
    fileOpen = open('guessable.txt', 'r') # Open the word_list.txt file
    file = fileOpen.readlines()

    for line in range(14855):
        
        nextWordRaw = str(file[line]) # Select the nth line of the txt file

        nextWord = nextWordRaw[0] + nextWordRaw[1] + nextWordRaw[2] + nextWordRaw[3] + nextWordRaw[4] # Isolate the first 5 letters of the nth word to remove the \n

        guessList.append(nextWord) # Add the nth line of the txt file to guessList[]

# ------------------------------------

# Variables and Functions

def resetAll():

    createList() # Call the function to create the list of words

    global possibleWords
    possibleWords = wordList # Makes another list of words for words that are yet to be eliminated

    global selectedWord
    selectedWord = rnd.choice(wordList) # Set the word to guess as a random word from the list

    if (config_keyboard == True): # Check if the keyboard is turned on

        global letterState
        letterState = [] # Reset the letter state list

        global qwerty
        qwerty = 'qwertyuiopasdfghjklzxcvbnm'

        for let in range(len(qwerty)): # For all 26 letters...

            letterState.append('d' + str(qwerty[let])) # Append the nth letter in the default state to letterState

# ------------------------------------
# Text stylizing
# ------------------------------------

global style

class style:

    end = '\033[0m'
    gray = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'

# ------------------------------------
# Visuals for word guesses
# ------------------------------------

def returnGuess(guess):

    for letter in range(5):
        
        # Letter is in the correct spot

        if (guess[letter]) == selectedWord[letter]:
            print(style.green + guess[letter] + style.end, end = '')
        
        # Letter is in the word but in the wrong spot

        elif (guess[letter]) in selectedWord:
            print(style.yellow + guess[letter] + style.end, end = '')
        
        # Letter is not in the word

        else:
            print(style.gray + guess[letter] + style.end, end = '')
    
    print('')

# ------------------------------------
# Solving
# ------------------------------------

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
# Keyboard display
# ------------------------------------

def colorSet(guess):

    for letter in range(5):

        if guess[letter] not in selectedWord: # Check if the nth letter is not in the correct word

            colorIndex = qwerty.index(guess[letter]) # Set the color index to the position of the nth letter
            letterState[colorIndex] = 'r' + qwerty[colorIndex] # Gray out the nth letter
        
        elif guess[letter] in selectedWord and selectedWord[letter] != guess[letter]: # Check if the nth letter is in the correct word BUT in the wrong spot

            colorIndex = qwerty.index(guess[letter]) # Set the color index to the position of the nth letter
            letterState[colorIndex] = 'y' + qwerty[colorIndex] # Yellow out the nth letter
        
        else: # Check if the nth letter is in the right spot

            colorIndex = qwerty.index(guess[letter]) # Set the color index to the position of the nth letter
            letterState[colorIndex] = 'g' + qwerty[colorIndex] # Green out the nth letter

def keyboard(guess):

    colorSet(guess)

    for let in range(len(letterState)): # For length of letterState (26)

        if (letterState[let][0] == 'r'): # Check if the letter is in the grayed out state

            color = skin.gray[config_skin]
        
        elif (letterState[let][0] == 'g'): # Check if the letter is in the correct state

            color = skin.green[config_skin]
        
        elif (letterState[let][0] == 'y'): # Check if the letter is in the yellow state

            color = skin.yellow[config_skin]
        
        else:
            
            color = skin.neutral[config_skin]
        
        print(color + str(letterState[let][1]) + ' ' + style.end, end = '') # Print the letter with it's correct color assigned

        if (let == 9 or let == 18): # Check if the program should go to the next line

            print('')
    
    print('')

# ------------------------------------

# Logic

for rep in range(config_repeat):

    resetAll() # Resets all variables
    guesses = 0
    currentGuess = ''

    while guesses != config_maxGuesses and currentGuess != selectedWord: # Repeat guesses until # of guesses has run out or the program guesses correctly

        if (config_manual == False): # Check for if the bot is running (manual == False) means the bot is running

            time.sleep(config_speed)

            if (config_optimal == True and guesses == 0): # Checks on the first guess if the bot is set to guess with the most optimal word
                currentGuess = config_optimalWord # Sets the guess to the most optimal word the bot has
            else:
                currentGuess = rnd.choice(possibleWords) # Select a random word from all possible words
            
            removeWords(currentGuess) # Remove incorrect words from the list

        else: # Code for the manual version of the program
            currentGuess = ''

            while (currentGuess not in guessList): # Check if the word guessed is a real word
                currentGuess = str(input('Make a guess | ')) # Ask the user to guess a word

                if (currentGuess not in guessList): # Check if the word guessed is a real word
                    print(style.red + 'Invalid word!' + style.end)
            
            if (config_possible == True):
                removeWords(currentGuess) # Remove incorrect words from the list
        
        returnGuess(currentGuess)

        if (config_possible == True):
            print(possibleWords)
        
        if (config_keyboard == True):
            keyboard(currentGuess)

        guesses += 1

    # ------------------------------------

    # Return if the guess was successful

    if (currentGuess == selectedWord): # Check if the user/bot got the word correct
        print(style.green + 'Wordle complete in ' + str(guesses) + ' guesses!' + style.end)
    else:
        print(style.red + 'Wordle failed! ' + style.end + 'Answer was "' + selectedWord + '"')

# ------------------------------------

print('Closing program in 5 minutes!')
time.sleep(300) # Set 5 minute timer to close the program