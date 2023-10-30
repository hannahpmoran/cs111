# David Liben-Nowell
# CS 111, Carleton College
# buttons.py
#
# A sample chunk of code to support some interactive buttons for projects.

from graphics import *

class Button:
    def __init__(self, x, y, width, height, letter, window, row, col):
        self.xRange = [x, x + width]
        self.yRange = [y, y + height]
        self.rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        self.clicks = 0
        self.rectangle.setFill("white")
        self.letter = letter
        self.text = Text(Point(x+width/2, y+height/2), self.letter)
        self.window = window
        self.row = row
        self.col = col

    def reset(self):
        self.rectangle.setFill("white")
        
    def draw(self, window):
        self.rectangle.draw(window)
        self.text.draw(window)

    def pointInside(self, point):
        return self.xRange[0] <= point.getX() <= self.xRange[1] \
            and self.yRange[0] <= point.getY() <= self.yRange[1] \

    def onClick(self, window):
        #self.clicks += 1
        #input = Text(Point(10, 450), self.letter)

        #if self.clicks % 2 == 1:
            self.rectangle.setFill("blue")
        #input.draw(window)
        #else:
            #self.rectangle.setFill("white")

    #def onRightClick(self):
        #self.rectangle.setFill("red")

class ButtonWindow:
    def __init__(self, title, width, height, squares):
        self.window = GraphWin(title, width, height)
        self.window.setMouseHandler(self.handleClick)
        self.window.setMouseRightHandler(self.handleRightClick)
        self.lastupdate = time.time()
        self.squares = squares

    def update(self):
        self.window.update()

    def closed(self):
        return not self.window.winfo_exists()        

    def handleClick(self, point):
        for square in self.squares:
            if square.pointInside(point):
                square.onClick()

    def handleRightClick(self, point):
        for square in self.squares:
            if square.pointInside(point):
                square.onRightClick()

def main():
    squares = []
    for row in range(8):
        for col in range(8):
            squares.append(Button(row * 50, col * 50, 50, 50))
    window = ButtonWindow("Game board", 400, 400, squares)
    for square in squares:
        square.draw(window)
    while not window.closed():
        window.update() 

if __name__ == "__main__":
    main()
