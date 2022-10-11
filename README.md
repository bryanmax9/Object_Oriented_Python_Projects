# Object_Oriented_Python_Projects
Here I'm uploading my python projects done on my Object Oriented Class

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Lab 1 – Python Basics

Guessing Game 
 
Have the computer generate a random number between 1 and 100, then prompt the user to guess 
a number between 1 and 100.  Test that the user’s input is an integer within the range, if it isn’t, 
tell them that it is invalid and allow them to continue guessing.  Compare the user’s number to 
the computer’s number, if the user’s number is lower than the computer’s, tell them that it is too 
low, if it is higher, tell them that it is too high.  Repeat until the user guesses the correct value.  
Keep count of the number of guesses and display it when the user wins (exclude invalid entries). 
 
Example Output (user input is in italics): 
 
- Guessing Game – 

I’m thinking of a number.  Make a guess (1-100): 50 

Too low!  Guess again (1-100): 75 

Too low!  Guess again (1-100): -1 

Invalid.  Guess again (1-100): a 

Invalid.  Guess again (1-100): 95 

Too high! Guess again (1-100): 90 

Too high! Guess again (1-100): 80 

Too low!  Guess again (1-100): 85 

Correct!  You got it in 6 tries.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Lab 2 – Functions  
Rock-Paper-Scissors 
 
Write a program that allows a user to play Rock-Paper-Scissors against the computer.  Have the 
program keep score of how many times each has won a round.  Your program should have a 
main method that has a loop that repeats the game until the user chooses to quit.  Display the 
final score before exiting. 
 
Write the following functions: 
 
1. weapon_menu() - Asks the user to input their choice: (R)ock, (P)aper, (S)cissors, 
or (B)ack.  Checks user input for validity and then returns the inputted value. 
2. comp_weapon() - Randomly chooses the computer’s throw and returns an “R”, 
“P”, or “S”. 
3. find_winner(player, comp) – Passes in the two weapons (R, P, or S), 
displays the throws, compares the two weapons and displays the result and returns 
who is the winner of that round (0=Tie, 1=Player, 2=Computer). 
a. Rock crushes Scissors 
b. Scissors cuts Paper 
c. Paper covers Rock 
4. display_scores(player, comp) - Displays the scores. 
 
Example Output (user input is in italics):

RPS Menu: 

1. Play game 
2. Show Score 
3. Quit 

1 

Choose your weapon: 

R. Rock 

P. Paper 

S. Scissors 

B. Back 

P 

You chose Paper 

Computer chose Paper 

Tie 

Choose your weapon: 

R. Rock 

P. Paper 

S. Scissors 

B. Back 

S 

You chose Scissors 

Computer chose Rock 

Computer wins 

Choose your weapon: 

R. Rock 

P. Paper 

S. Scissors 

B. Back 

B 

RPS Menu: 

1. Play game 

2. Show Score 

3. Quit 

2 

Player = 0 

Computer = 1 

RPS Menu: 

1. Play game 

2. Show Score 

3. Quit 

3 

Final Score: 

Player = 0 

Computer = 1 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Lab 3 – 2D Lists
Minesweeper Board Creator
Create a program that generates a RxC solution board for the game Minesweeper. Prompt the
user to enter the size of the grid (rows and columns between 5-10), and the number of mines
(also between 5-10). Randomly place the mines on the grid, then fill the remaining spaces by
counting the number of mines in any adjacent squares (diagonals included). Display the filled
grid. Error check all user input and document each of your functions.
Create the following functions for your program:
1. place_mines(board, mines) – for each mine, generate a random row and
column within the bounds of the grid and check that location. If it is a 0, then place an
‘X’ there, otherwise repeat the loop to generate a new location (this ensures that it cannot
overwrite a previously written ‘X’ and generate the incorrect number of mines).
2. count_mines(board) – for each spot in the grid (except places with a mine ‘X’),
count any ‘X’s in the surrounding eight spaces, then place the value of the counter in that
spot. Use a nested set of loops to iterate through the surrounding eight spaces. Be
careful not to overwrite any mines.
3. display_board(board) – display the contents of the grid using a set of nested
loops.
The main method should prompt the user for the three inputs, then call each of the three methods
in the above order.
Example Outputs (user input is in italics):


Minesweeper Maker

Enter number of rows (5-10):

5

Enter number of columns (5-10):

5

Enter number of mines (5-10):

5


X 2 2 1 1

2 X 2 X 1

2 2 2 1 1

X 2 1 1 0

1 2 X 1 0


Minesweeper Maker

Enter number of rows (5-10):

6

Enter number of columns (5-10):

8

Enter number of mines (5-10):

10


0 0 1 1 1 0 0 0

1 1 1 X 3 2 2 1

X 3 3 4 X X 3 X

X 3 X X 3 3 4 X

1 2 2 2 1 1 X 2

0 0 0 0 0 1 1 1

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Lab 4 – File IO  
State Capitals Quiz 
 
Create a program that quizzes the user on the state capitals.  Use the file (StateCapitals.txt) 
provided on Canvas to create the quiz questions. 
 
Create the following functions: 
1. read_file_to_dict(file_name) – each line in the file is in the format: 
state,capital.  Read in each line, break up the state from the capital, and store them 
as a key:value pair in a dictionary.  Return the filled dictionary. 
2. get_random_state(states) – pass in the states dictionary.  Convert the 
dictionary to a list of key:value pairs, then choose a random key:value pair from the list 
and return it.  This returned value will be used as the correct state:capital pair for each 
question. 
3. get_random_choices(states, correct_capital) – pass in the states 
dictionary, and the capital of the correct answer.  Convert the dictionary to a list of values 
and choose 3 incorrect choices from this list.  These incorrect choices should be different 
from the correct capital and also different from each other.  Place the three incorrect 
capitals and the correct capital in a list.  Shuffle and then return the list. 
4. ask_question(correct_state, possible_answers) – pass in the name of 
the correct state and the list of 4 possible answers.  Display the question to the user and 
the four possible answers.  Take in the user’s selection and check that it is an A, B, C, or 
D.  If it isn’t, then display an ‘Invalid’ message and repeat until the user enters a valid 
choice.  If it is, then convert the input to 0-3 (A=0, B=1, C=2, D=3) and return the value. 
 
Your main should read in the file then have a loop that repeats 10 times, one for each of the quiz 
questions.  For each quiz question, choose a random state (repeats are allowed) as the correct 
answer, generate the possible answers, get the correct choice by searching the possible answer 
list for the correct capital, and then ask the quiz question.  Compare the user’s selection (0-3) 
against the location of the correct capital (0-3).  If the user was correct, display a congratulatory 
message and give them a point, otherwise, tell them that they were incorrect and display the 
correct answer.  After all 10 questions are finished, display the total points they received.   
 
Partial Example Output (user input is in italics): 
 
-  State Capitals Quiz  – 

1. The capital of New Mexico is: 

 A. Phoenix   B. Lansing   C. Santa Fe   D. Cheyenne 


Enter selection: G 

Invalid input. Input choice A-D. 

Enter selection: B 

Incorrect!  The correct answer is: Santa Fe. 

2. The capital of Florida is: 

 A. Tallahassee   B. Dover   C. Honolulu   D. Sacramento 

Enter selection: A 
 
Correct! 

... 

10. The capital of California is: 

A. Hartford   B. Sacramento   C. Montgomery   D. Juneau 

Enter selection: B 

Correct! 

End of test.  You got 8 correct.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Lab 5 – Classes & Objects

Drawing Rectangles

Create a program that allows the user to move a rectangle around a grid. The user should input
the dimensions of the rectangle (width and height 1-5), and then be able to choose which
direction to move the rectangle in.

Create a Rectangle class (in a separate file named ‘rectangle.py’) with the following:
1. Attributes – x, y, width, height
2. Methods
1. __init__(self, w, h) – pass in w and h, set them to width and height, set x
and y to 0.
2. get_coords(self) – returns the x and y values as a pair.
3. get_width(self) – returns the rectangle’s width.
4. get_height(self) – returns the rectangle’s height.
5. move_up(self) – moves the rectangle up one row.
6. move_down(self) – moves the rectangle down one row.
7. move_left(self) – moves the rectangle left one column.
8. move_right(self) – moves the rectangle right one column.

In a separate file (‘main.py’), in the main function, prompt the user to enter a width and height of
a rectangle (1-5). Use these inputs to create an instance of the rectangle. Create a 20x20 2D list
(the grid) that is initially all ‘.’s.

Also create the following functions in your main.py:

1. display_grid(grid) – pass in the grid and display the contents of the grid.
2. reset_grid(grid) – pass in the grid and overwrite the contents with all ‘.’s.
3. place_rect(grid, rect) – pass in the grid and the rectangle. At the location of
the rectangle (x, y) on the grid, overwrite the ‘.’ characters with ‘*’s using the width and
height of the rectangle.

After the rectangle is created, place it on the grid, display the grid, and then display a menu that
allows the user to choose which direction to move the rectangle in, up, down, left, right, or to
quit. Once the user has chosen a direction, check that the rectangle can move in that direction, it
should not be able to move past the boundaries of the grid in any direction. If the rectangle has
room to move, then you should call the move method for that direction to update the rectangle.
Then call the reset_grid, place_rect, and display_grid functions to update and display the grid.
Repeat until the user chooses to quit the program. Use the check_input module to validate all
user inputs. Use docstrings to document the class, its methods, and the main functions.

Example Output (user input is in italics):

Enter rectangle height (1-5): 3

Enter rectangle width (1-5): g

Invalid input – should be an integer.

Enter rectangle width (1-5): 7

Invalid input – should be within range 1-5.

Enter rectangle width (1-5): 4

* * * * . . . . . . . . . . . . . . . .
* * * * . . . . . . . . . . . . . . . .
* * * * . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .

Enter Direction:
1. Up
2. Down
3. Left
4. Right
5. Quit
2

. . . . . . . . . . . . . . . . . . . .
* * * * . . . . . . . . . . . . . . . .
* * * * . . . . . . . . . . . . . . . .
* * * * . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . .

Enter Direction:
1. Up
2. Down
3. Left
4. Right
5. Quit
5

Notes:
1. You should have 3 different files in your project: rectangle.py, check_input.py, and
main.py.
2. Check all user input using the get_int_range function in the check_input module.
3. Do not create any extra functions or add any extra parameters.
4. Please do not create any global variables or use the attributes globally. Only access the
attributes using the class’s methods.
5. Use docstrings to document the class, each of its methods, and the main functions. See
the lecture notes and the Coding Standards reference document for examples.
6. Place your names, date, and a brief description of the program in a comment block at the
top of your main. Place brief comments throughout your code.
7. Thoroughly test your program before submitting:
a. Make sure that all user inputs are validated.
b. Make sure that the rectangle is drawn with the correct dimensions (ie. make sure
that you didn’t get the height and width backwards), and in the correct location.
c. Make sure that the rectangle moves in the direction that the user selects.
d. Make sure that the rectangle cannot move past the border of the grid. Up and left
should check the top and left edges of the rectangle, and down and right should
check the bottom and right edges of the rectangle (which means you’ll have to
account for the width and height of the rectangle).

....... <h1>The continuing Labs, they contain a pdf with the detailed information</h1>

