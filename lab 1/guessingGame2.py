import random
randomNum = random.randint(1,100)
print("- Guessing Game -")
print (randomNum)
print("you have 5 tries!")

numGuess = 0

import check_input


guess = check_input.get_positive_int("I'm thinking of a number. Make a Guess(1-100): ")

while numGuess < 100:
  numGuess += 1

  if (not guess):
    guess = check_input.get_positive_int('Invalid. Guess again (1-100): ')

  elif guess < randomNum:
    guess = check_input.get_positive_int('Too low! Guess again (1-100): ')
  elif guess > randomNum:
    guess = check_input.get_positive_int('Too high! Guess again (1-100): ')
  elif numGuess == 5:
    print('You did not guess the number, The number was ' + str(randomNum))
    break
  elif guess == randomNum:
    print('Correct! you got it in ' + str(numGuess) + ' tries.')
    break      
    



