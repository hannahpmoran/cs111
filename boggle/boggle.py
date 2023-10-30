#Boggle game
# A legitimate word:
# contains at least 3 letters
# is made by connecting adjacent tiles
# does not have any repeated tile

from os import RTLD_NOW
import random
import time
from graphics import *
from buttons import Button
import math

#Load dictionary
def loadDictionary():
    words = []
    try: 
        dictfile = open("twl98.txt")
    except IOError:
        print("ERROR! where's 'twl98.txt'?")
        exit(1)
    for line in dictfile:
        word = line.strip()
        words.append(word)
    dictfile.close()
    return words

#Generate letters, make a grid
class Cubes:
    def __init__(self, cubes):
        self.cubes = cubes

    def randomCube(self, cubes):
        letters = []
        for cube in cubes:
            i = random.randint(0,5)
            letters.append(cube[i])
        return letters

    def shuffleBoard(self):
        board = self.randomCube(self.cubes)
        random.shuffle(board)
        return board
    
    def boardLayout(self, board):
        #find how to print in 4X4
        rowZero, rowOne, rowTwo, rowThree, grid = [], [], [], [], []
        rowZero = board[0:4]
        rowOne = board[4:8]
        rowTwo = board[8:12]
        rowThree = board[12:16]
        for row in [rowZero, rowOne, rowTwo, rowThree]:
            grid.append(row)
        return grid

class Boggles:
    def __init__(self, title, width, height, words, board, grid):
        #Graphics
        self.window = GraphWin(title, width, height)
        self.instruction()
        self.status = Text(Point(200, 450),"Game Loading")        
        self.status.draw(self.window)
        self.window.setMouseHandler(self.handleClick) 
        self.grid = grid
        self.board = board
        self.lastupdate = time.time()
        self.squares = []
        self.words = words
        for col in range(4):
            for row in range(4):
                letter = self.grid[row][col]
                self.squares.append(Button(col* 100, row * 100, 100, 100, letter, self.window, row, col))
        self.maxScore = 0
        
        self.playerCurrentInput = ""
        self.currentCol = None 
        self.currentRow = None
        self.lastCol = None
        self.lastRow = None
        self.visited = []
        self.userWords = []
        self.userScore = 0

        #Generatate playable words
        self.playableWords = self.isWord()

        #Draw letter tiles
        for square in self.squares:
            square.draw(self.window)
        
        #Draw submit button
        submitButton = Rectangle(Point(300,420), Point(350, 440))
        self.submitButton = submitButton
        submitText = Text(Point(325, 430),"Submit")  
        submitButton.draw(self.window)
        submitText.draw(self.window)

        #Draw clear button
        clearButton = Rectangle(Point(300,460), Point(350, 480))
        self.clearButton = clearButton
        clearText = Text(Point(325, 470),"Clear")  
        clearButton.draw(self.window)
        clearText.draw(self.window)

        #Update game status once the game is loaded
        self.status.setText("Game Started")
        self.timerText = Text(Point(50, 445),"Timer")
        self.timerText.draw(self.window) 
        self.timer = Text(Point(50, 455),"Timer")
        self.timer.draw(self.window) 
        
    def update(self):
        self.window.update()
    
    #Instruction while the game loads
    def instruction(self):
        self.how = Text(Point(200, 200),"How to play this Boggle")
        self.ins = Text(Point(200, 210),"Click on adjacent cells to make a word")
        self.ins1 = Text(Point(200, 220),"Click submit when happy with your word")
        self.score3 = Text(Point(200, 230),"3 letters = 1 point")
        self.score4 = Text(Point(200, 240),"4 letters = 2 points")
        self.score5 = Text(Point(200, 250),"5 letters = 3 points")
        self.minute = Text(Point(200, 260),"You have 1 minute")
        self.fun = Text(Point(200, 270),"Have fun!")
        self.how.draw(self.window)
        self.ins.draw(self.window)
        self.ins1.draw(self.window)
        self.score3.draw(self.window)
        self.score4.draw(self.window)
        self.score5.draw(self.window)
        self.minute.draw(self.window)
        self.fun.draw(self.window)

    def handleClick(self, point):
        #If click submit/clear button
        if 300 <= point.getX() <= 350 and (420 <= point.getY() <= 440 or 460 <= point.getY() <= 480):
            if 420 <= point.getY() <= 440:
                self.submitButton.setFill("orange")
                self.assess()
            else:
                self.clearButton.setFill("pink")
            self.lastCol = None
            self.lastRow = None
            self.visited = []
            self.playerCurrentInput = ""
            for square in self.squares:
                square.reset()
            if 420 <= point.getY() <= 440:
                self.submitButton.setFill("white")
            else:
                self.clearButton.setFill("white")

        #If click one of the letters
        elif 0 <= point.getX() <= 400 and 0 <= point.getY() <= 400:
            for square in self.squares:
                if square.pointInside(point):
                    self.currentCol = square.col
                    self.currentRow = square.row
                    # Make sure the clicked tile is either the first tile of a new combination 
                    # or is a new tile and adjacent to the latest tile in the current combination
                    if self.isFirst() or (self.isAdjacent() and not self.isVisited()):
                        self.addToCurrentInput(square)
                        square.onClick(self.window)
                        self.lastCol = square.col
                        self.lastRow = square.row
                        self.visited.append((self.lastRow, self.lastCol))

            print("current input: ", self.playerCurrentInput)
            print("has visited: ", self.visited)
            print("-------")

    #Store player's current letter combinations
    def addToCurrentInput(self, square):
        self.playerCurrentInput += square.letter

    def isAdjacent(self):
        #print("checking if current coordinate ", self.currentRow, self.currentCol, "is adjacent to last coordinate", self.lastRow, self.lastCol)
        return max(abs(self.currentCol - self.lastCol),abs(self.currentRow - self.lastRow)) <= 1
   
    def isFirst(self):
        return self.lastCol == None

    def isVisited(self):
        #print("checking if current coordinate", self.currentRow, self.currentCol, "has already been visited in the list", self.visited )
        for coordinates in self.visited:
            if (self.currentRow, self.currentCol) == coordinates:
                return True
        return False

    def pathways(self):
        directions = [  0, 
                        (+1, +0),
                        (+1, +1),
                        (+0, +1),
                        (-1, +1),
                        (-1, +0),
                        (-1, -1),
                        (+0, -1),
                        (+1, -1)]

        startCoords = [(0, 0), (0, 1), (0, 2), (0, 3),
                    (1, 0), (1, 1), (1, 2), (1, 3),
                    (2, 0), (2, 1), (2, 2), (2, 3),
                    (3, 0), (3, 1), (3, 2), (3, 3)]

        coordPaths = []

        #Starting with (0,0)
        for originalCoord in startCoords:
            for numberPath in range(10,100000):
                currentCoordPath = []
                currentCoordPath.append(originalCoord)
                if "0" not in str(numberPath) and "9" not in str(numberPath):
                    currentCoord = originalCoord
                    for number in str(numberPath):
                        currentDirection = directions[int(number)]
                        row = currentCoord[0] + currentDirection[0]
                        col = currentCoord[1] + currentDirection[1]
                        if row <0 or row >3 or col <0 or col >3:
                            break
                        else:
                            currentCoord = (row, col)
                            #Make sure not to revisit a coordinate
                            if currentCoord not in currentCoordPath:
                                currentCoordPath.append(currentCoord)
                    if len(currentCoordPath) == math.ceil(math.log(numberPath, 10)) + 1: 
                        #print(a, coordinates, math.ceil(math.log(a, 10)), len(coordinates))
                        coordPaths.append(currentCoordPath)
        return coordPaths

    def convertCoords(self):
        coordPaths = self.pathways()
        wordList = []
        for i in range(len(coordPaths)):
            word = ''
            for coord in coordPaths[i]:
                letter = self.grid[coord[0]][coord[1]]
                word += letter    
            if word not in wordList:
                wordList.append(word)
        return wordList

    def isWord(self):
        print("starting")
        playableWords = []
        words = self.words
        wordList = self.convertCoords()
        for i in range(len(wordList)):
            word = wordList[i]
            if word in words:
                print("found a word!", word)
                playableWords.append(word)
                self.maxScore += len(word) - 2
        print(playableWords)
        print("no more words!")
        return playableWords

    def assess(self):
        userInput =  self.playerCurrentInput
        wordScore = len(userInput) - 2
        if userInput in self.playableWords and userInput not in self.userWords:
            print("yay")
            self.userWords.append(userInput)
            self.userScore += wordScore
        else:
            print("nay")
    
    def showTime(self, timeLeft):
        self.timer.setText(str(timeLeft))

    #This is currently useless. I'm trying to show a scoreboard on the same window and let the player restart game if they want
    def scoreBoard(self):
        self.window.setBackground("white")
        #self.window.setMouseHandler(self.restartGame)
        gameOver = Text(Point(200, 200),"Game Over")
        gameOver.draw(self.window)

def main(): 
    #Load 16 cubes
    cubes = [("A","A","E","E","G","N"), ("A","B","B","J","O","O"), ("A","C","H","O","P","S"), ("A","F","F","K","P","S"),
            ("A","O","O","T","T","W"), ("C","I","M","O","T","U"), ("D","E","I","L","R","X"), ("D","E","L","R","V","Y"),
            ("D","I","S","T","T","Y"), ("E","E","G","H","N","W"), ("E","E","I","N","S","U"), ("E","H","R","T","V","W"),
            ("E","I","O","S","S","T"), ("E","L","R","T","T","Y"), ("H","I","M","N","Q","U"), ("H","L","N","N","R","Z")]
                                

    cubes = Cubes(cubes)
    board = cubes.shuffleBoard()
    grid = cubes.boardLayout(board)
    words = loadDictionary()
    window = Boggles("Boggle", 400, 500, words, board, grid) 
    #print("Here are all the playable words in this boggle: ", window.isWord())
    #print(window.allPlayable())
    start = time.time()
    while time.time() - start <= 60:   
        window.showTime(int(60 - (time.time() - start)))
        window.update()

    print("your grid: ", window.grid)
    print("your legitimate words: ", window.userWords)
    print("your total score: ", window.userScore)
    print("total score possible: ", window.maxScore)

if __name__ == "__main__":
    main()

