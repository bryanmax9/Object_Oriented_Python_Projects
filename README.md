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
 
- State Capitals Quiz – 
1. The capital of New Mexico is: 
 A. Phoenix   B. Lansing   C. Santa Fe   D. Cheyenne 
Enter selection: G 
Invalid input. Input choice A-D. 
Enter selection: B 
Incorrect!  The correct answer is: Santa Fe. 
2. The capital of Florida is: 
 A. Tallahassee   B. Dover   C. Honolulu   D. Sacramento 
Enter selection: A 
©2022 Cleary 
Correct! 
... 
10. The capital of California is: 
 A. Hartford   B. Sacramento   C. Montgomery   D. Juneau 
Enter selection: B 
Correct! 
End of test.  You got 8 correct.
