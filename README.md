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

