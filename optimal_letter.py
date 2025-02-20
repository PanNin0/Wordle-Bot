# ------------------------------------

# Optimal Letter

# ------------------------------------

# Modules

import string
import time

# ------------------------------------

# Variables and Functions

global alphabet
alphabet = string.ascii_lowercase

occurance = []

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

# Logic

createList()

for let in range(len(alphabet)):

    currentLetter = alphabet[let] # Sets the current letter to the nth letter of the alphabet
    currentTotal = 0 # Resets the total occurances of the current letter

    for word in range(len(wordList)):

        if (currentLetter in wordList[word]):

            currentTotal += 1
    
    occurance.append(currentTotal)

    print('Letter "' + str(currentLetter) + '" occured ' + str(currentTotal) + ' times!')

# ------------------------------------

print('Closing program in 5 minutes!')
time.sleep(300)

# ------------------------------------