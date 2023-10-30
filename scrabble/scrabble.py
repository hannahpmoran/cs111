# scrabble.pcleay
# Portions written by David Liben-Nowell for CS 111, Carleton College.
import random

def scoreTile(letter):
    '''Given a letter (one of ABCDEFGHIJKLMNOPQRSTUVWXYZ), returns the
       number of points that letter is worth.  Causes an error if it
       is passed a parameter that is not a upper-case letter.'''

    # Check to make sure that letter is really a letter.
    if letter not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        raise ValueError("I can't compute the score of letter " + letter + "!")

    # Each letter is worth some designated number of points.  The list
    # scores records the value of each letter -- the letters in the
    # string scores[i] are each worth exactly i points.
    scores = ['',           # 0 points
              'EAIONRTLSU', # 1 point
              'DG',         # 2 points
              'BCMP',       # 3 points
              'FHVWY',      # 4 points
              'K',          # 5 points 
              '',           # 6 points
              '',           # 7 points
              'JX',         # 8 points
              '',           # 9 points
              'QZ']         # 10 points

    # Look through every string in the scores list until we find letter.
    # If we found letter in scores[i], then the point count for letter is i.
    for i in range(len(scores)):
        if letter in scores[i]:
            value = i
    return value


def scoreWord(word): # Question 2
    '''Given a word, returns the number of points that word is worth, which
       is the sum of the point counts for each word, plus a bonus of 50 for 
       7-letter words.  For example:
         scoreWord("TSKTSK")     --> 14
         scoreWord("DJINN")      --> 13
         scoreWord("HEGEMON")    --> 63'''

    scoreLetters = 0
    scoreLettersCombined = 0
    for ch in word:
        scoreLetters = scoreTile(ch)
        scoreLettersCombined = scoreLettersCombined + scoreLetters
    
    if len(word) == 7:
            scoreLettersCombined = scoreLettersCombined + 50
    
    return scoreLettersCombined


def randomHand(pool):
    '''Computes a random hand of seven tiles from a given pool.'''
    return random.sample(pool,7)



def playable(word, hand): # Question 3
    '''Given a word and a hand, where a word is a string of letters
       and a hand is a list of tiles (which are themselves letters),
       returns True if that word can be played using only the tiles in
       hand and False if not.  For example:
          playable("ADZE", ['Z', 'C', 'E', 'E', 'D', 'T', 'A'])     --> True
          playable("ARIOSE", ['R', 'I', 'S', 'A', 'O', 'I', 'E'])   --> True
          playable("UCALEGON", ['R', 'I', 'S', 'A', 'O', 'I', 'E']) --> False
          playable("AREA", ['A', 'E', 'I', 'O', 'U', 'Y', 'R'])     --> False
       Notice this last example returns False because, although there is an 'A'
       in the hand, the word "AREA" requires *two* 'A's.'''

    playableHand = hand.copy()

    for ch in word:
        if ch in playableHand:
            playableHand.remove(ch)
        else:
            return False
    
    return True


def loadDictionary():
    ''' Create a list of all words that are legal to play in Scrabble.
        The dictionary file that we've been using all term is the
        official Scrabble dictionary from a few years ago, so we can
        accomplish this simply by loading each line and adding it to
        the end of the words list.  (Feel free to look up L.append for
        a list L if you're interested in the details.)'''

    # This block of code allows you to work either on some CS lab machines
    # (without downloading the data file) OR on your own computer 
    # (downloading it).
    words = []
    try:
        dictfile = open("/Accounts/courses/cs111/dln/data/twl98.txt")
    except IOError:
        try: 
            dictfile = open("twl98.txt")
        except IOError:
            print("ERROR!  twl98.txt doesn't appear in either the current")
            print("    directory or in /Accounts/courses/cs111/dln/data")
            print("Please see the problem set instructions.")
            exit(1)
    for line in dictfile:
        word = line.strip()
        words.append(word)
    dictfile.close()
    return words


def allPlayable(hand, words): # Question 4

    playablewords = []
    playableWordsInHand = []
    dictfile = open("twl98.txt")

    for line in dictfile:
        words = line.strip()
        playablewords.append(words)
    
    for i in playablewords:
        if playable(i, hand) == True:
            playableWordsInHand.append(i)

    return playableWordsInHand

def bestPlayable(hand, words):

    currentScoreWord = 0
    highestScoreWord = 0

    for i in allPlayable(hand, words):
        currentScoreWord = scoreWord(i)
        if currentScoreWord > highestScoreWord:
            highestScoreWord = currentScoreWord

    return highestScoreWord


def main():
    # The full set of 100 tiles in Scrabble.  (Actually, I'm only giving
    # you 98 of them; two of the real tiles are blanks, which can be used
    # in place of any letter as a wildcard.)
    tiles = 12*['E'] + 9*['A'] + 9*['I'] + 8*['O'] + 6*['N'] + 6*['R'] \
        + 6*['T'] + 4*['L'] + 4*['S'] + 4*['U'] + 4*['D'] + 3*['G'] + 2*['B'] \
        + 2*['C'] + 2*['M'] + 2*['P'] + 2*['F'] + 2*['H'] + 2*['V'] + 2*['W'] \
        + 2*['Y'] + 1*['K'] + 1*['J'] + 1*['X'] + 1*['Q'] + 1*['Z']

    words = loadDictionary()

    hand = randomHand(tiles)
    plays  = allPlayable(hand, words)
    best = bestPlayable(hand, words)

    print(hand)
    print(plays)
    print(best) #needs to print the word too


    # We have now computed two useful pieces of data and two useful
    # functions for the remainder of this program:
    #   -- tiles                  the list of 98 tiles in the game
    #   -- words                  the list of all legal words
    #   -- scoreTile(letter)      returns the number of points for letter
    #   -- randomHand(tiles)      selects a random subset of 7 tiles


if __name__ == "__main__":
    main()
