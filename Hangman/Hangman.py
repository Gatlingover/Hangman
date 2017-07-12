import random
HANGMANPICS = ['''

+---+
  | |
    |
    |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion
lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon
python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake
spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat
zebra'.split()

def getRandomword(wordList):
     # this function returns a random string from the passed list of strings.
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #returns the letter the player entered. this function makes sure the player entered a single letter, and not something else.

    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print ('H A N G M A N')
missedLetters = ' '
correctLetters = ' '
secretWord = getRandomword(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)  

    # let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #