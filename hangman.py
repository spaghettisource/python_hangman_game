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

    
    
    
    for letter in secretWord:
        
        if letter in lettersGuessed:            
            shadowword[i] = secretWord[i]
        i += 1
            
                    
    return ''.join(shadowword)
        
