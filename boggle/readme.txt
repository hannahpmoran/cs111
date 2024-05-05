# boggle.py
Written by Nhi Luong and Hannah Moran

Boggle is a game in which a board of sixteen cubes is randomly placed and landed on a letter for 
each cube. Six letters are on each cube, designed to produce maximum words when a board is ready. 

When the game is started, a player reads the instructions and has one minute to complete before receiving their score and the maximum score possible from that round. 

Our program requires boggle.py, buttons.py, graphics.py, and twl98.txt to run. 

We have two classes: Cubes and Boggles. "Cubes" includes the functions necessary for 
randomly "rolling" each cube and randomly distributing cubes on the board. "Boggles" contains 
all of the required functions for running each game. Each function is described accordingly using 
comments. 

More complex functions, such as pathways, may be unclear. The pathways function generates the numerical path that users can legally play within the board and converts the numbers into 
directions (ex: (+1, +0)). The path begins at an origin cord (ex: (1, 2)), and the directions are subsequently applied to start from the origin coordinate to the final position. Immediately 
following, the function convertCoords will change each path into a corresponding letter. Then, 
isWord will match up each set of letters to determine if they are words in our dictionary. 

Assess is the function that checks if the user input is in our word list and returns the appropriate point amount.
As it stands, the game operates how we want. The game runs considerably efficiently after 
implementing some additional checks to reduce the amount of information processing while the game loads. One of our obstacles was decreasing the amount of processing time before the game began since some functions (like pathways) were running several duplicate pathways and tripling 
the information processed. 

We set a goal early on (very optimistically) to provide a "leaderboard" that included a name and 
a score. The leaderboard would display the high scores in descending order at the end of each 
game. It might have been possible with an external file formatted to input the data from each 
game. There is some incomplete code in the function "scoreBoard" that Nhi worked on 
separately to start the project, but complications with windows and time prevented its completion. 

Instructions: 

1. With all files required in the same directory, the player can run boggle.py. 
2. A window should appear and contain the instructions for the game. It also should include how points are determined. 
3. Once the game has loaded, the board of sixteen cubes is displayed on the screen. Submit and clear button is visible in the bottom right. A timer is visible in the bottom left. 
4. In the player's minute, you click (in order) the cubes to form words, only connected 
through adjacent cubes (prohibited input). 
5. The current input is logged in the terminal. You can see the coordinates visited and their 
corresponding letters. 
6. You can click clear to reset the current inputs. 

7. You can click submit to submit a word (if not a word, then no points added, and "nay" is printed). "yay" is printed as a result of valid word input, and points are added to the total. 
8. At the end of the minute, the following data is returned:
1. the grid 
2. user-inputted legitimate words 
3. user total score 
4. total score in board possible 
9. Repeat to play again! 

