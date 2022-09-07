from multiprocessing.sharedctypes import Value
import random


print("- Guessing Game -")

randomNum = random.randint(1, 100)
print(randomNum)
UserGuess = input("I'm thinking of a number. Make a guess (1-100): ")

try:
  int(UserGuess)
  is_Int = True
except ValueError:
  is_Int = False
print(is_Int)


while (randomNum !=  UserGuess ):
  if ( not is_Int):
    UserGuess = input("INVALID. Guess again (1-100): ")

  if(int(UserGuess) < 1):
    UserGuess = input("INVALID. Guess again (1-100): ")
  
  
  
  

  if (randomNum >= int(UserGuess) ):
    UserGuess = input("Too low! Guess again (1-100): ")

  if (randomNum <= int(UserGuess) ):
    UserGuess = input("Too high! Guess again (1-100): ")
    



