import string

number_of_guesses = 8

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in available_letters:
            available_letters.remove(letter)
    return ''.join(available_letters)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    
    i = 0
    numletters = len(secretWord)
    shadowword = list(numletters * '_')

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    guessed = 0
    
    for letter in lettersGuessed:
        if letter in secretWord:
            guessed += 1

    if guessed == len(secretWord):
        return True
    else:
        return False

def hangman(secretWord):
'''
secretWord: string, the secret word to guess.

Starts up an interactive game of Hangman.

* At the start of the game, let the user know how many
letters the secretWord contains.

* Ask the user to supply one guess (i.e. letter) per round.

* The user should receive feedback immediately after each guess
about whether their guess appears in the computers word.

* After each round, you should also display to the user the
partially guessed word so far, as well as letters that the
user has not yet guessed.

Follows the other limitations detailed in the problem write-up.

'''
tries = 8
lettersGuessed = ''
def checkGame():
if tries > 0:
return True
else:
return False

print 'Loading word list from file...'
print '55900 words loaded.'
print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'


while tries > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
print 'You have ' + str(tries) + ' guesses left'
print 'Available letters ' + getAvailableLetters(lettersGuessed)
lettersGuessed = raw_input('Please guess a letter: ')
y = isWordGuessed(secretWord, getAvailableLetters(lettersGuessed))
if y == True:
print 'Good guess' + getGuessedWord(secretWord, lettersGuessed)
if checkGame() == True:
print "Congratulations you won!"
break
else:
print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
tries -= 1





    
   
         
            
        

        







