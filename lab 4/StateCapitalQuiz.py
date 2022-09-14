# STATE CAPITAL QUIZ LAB
from ctypes.wintypes import PINT
import random
from os import stat


def read_file_to_dict(file_name):
  dictionary = {}
  file = open(file_name)
  state_capital = file.readlines()
  
  #Putting all the states and the capital in dictionary
  for state in state_capital:
    lista = state.split(",")
    dictionary[lista[0]] = lista[1].strip()

  file.close()

  return dictionary


def get_random_state(states):
  n_states = len(states)
  #Converting the dictionary to a list of key: value pairs
  lista = []
  for item in states:
    #item is the current state
    lista.append((item,states[item]))

    #above we are saving each state with its respective capital in a tuple inside a list
  
  #after getting the amount of states and capitals, we are selecting one of them randomly using randint
  random_index = random.randint(0, n_states - 1)
  correct_statecapital = lista[random_index]
  
  return correct_statecapital

def get_random_choices(states, correct_capital):
  #storing the correct capital
  correct = correct_capital[1]

  #First we are storing the dictionary's capitals as a list of values
  capitals = list(states.values())

  #now we are getting the number of capitals that there are in the list
  n_capitals = len(capitals)

  #We are picking three incorrect choices, so we will generate three random indexes
  random_index1 = random.randint(0, n_capitals - 1)
  random_index2 = random.randint(0, n_capitals - 1)
  random_index3 = random.randint(0, n_capitals - 1)

  off_on_whileloop = True

  while off_on_whileloop:
    #Getting three incorrect choices
    incorrect_choice1 = capitals[random_index1]
    incorrect_choice2 = capitals[random_index2]
    incorrect_choice3 = capitals[random_index3]

    if incorrect_choice1 != correct and incorrect_choice2 != correct and incorrect_choice3 != correct:
      off_on_whileloop = False
      break
  
  #we are creating a list were we store the 3 incorrect capitals and the correct capital
  lista_correct_incorrect = []

  #INCORRECT CAPITALS appended to list
  lista_correct_incorrect.append(incorrect_choice1)
  lista_correct_incorrect.append(incorrect_choice2)
  lista_correct_incorrect.append(incorrect_choice3)

  #CORRECT CAPITAL appended to list
  lista_correct_incorrect.append(correct)

  
  #shuffling list of correct and incorrect answers
  random.shuffle(lista_correct_incorrect)

  #We will return the shuffled list
  return lista_correct_incorrect


def ask_question(correct_state, possible_answers, question_number):
  name_state = correct_state[0]

  print("🎮 - State Capital Quiz - 🎮")
  print(f""" 
  {question_number}. The capital of {name_state} is:
        A.{possible_answers[0]}   B.{possible_answers[1]}   C.{possible_answers[2]}   D.{possible_answers[3]}
   """)
   
 

  user_choice =  input("Enter selection: ")

  #the choice will always pass these while loop!, if its the correct choice it will exit the loop
  while user_choice != "A" and user_choice != "B" and user_choice != "C" and user_choice != "D":
    print("Invalid input. Input choice A-D")
    user_choice =  input("Enter selection: ")
  
  if user_choice == "A":
    return 0
  
  elif user_choice == "B":
    return 1
  
  elif user_choice == "C":
    return 2
  
  elif user_choice == "D":
    return 3
  





  

def main():
  user_points = 0
  n_questions = 1
  #rweads file
  reading = read_file_to_dict("StateCapitals.txt")

  while n_questions != 11: 
    correct_capital = get_random_state(reading)
    #print(correct_capital[1], "is the correct capital")
    choices = get_random_choices(reading, correct_capital)

    #since we are getting returned a number from 1 to 3 from ask question
    #then, we are using that to check the index of the user's choice
    user_choice = choices[ask_question(correct_capital,choices, n_questions)]

    if user_choice == correct_capital[1]:
      user_points += 1
      print("Correct!")
    
    else:
      print(f"Incorrect! The correct answer is: {correct_capital[1]}")


    n_questions += 1

  
  if user_points >= 5:
    print(f"End of test. You got {user_points} correct! 👻👻")
  
  elif user_points == 3:
    print(f"End of test. You got {user_points} correct 😶‍🌫️😅")
  
  else:
    print(f"End of test. You got {user_points} correct 😥")





main()
  



  
  


