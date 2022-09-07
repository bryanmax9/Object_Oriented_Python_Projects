import random
import check_input

def weapon_menu():
  #The computer choice will be set before the weapon menu
  pc_input = comp_weapon()

  print(""" 
  -------- Choose your weapon ---------
  R. Rock 🪨
  P. Paper 📃
  S. Scissors ✂️
  B. Back 
   """)

  validiy =  True
  while validiy: 
    user_input = input("Choose R (Rock), P (Paper), S (Scissor), or B (Back to the menu):  ")
    if user_input == "R":
      winner = find_winner(user_input, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      if winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      if winner == 0:
        print("It was a tie!! 😥")
        return 0

    elif user_input == "P":
      winner = find_winner(user_input, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      if winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      if winner == 0:
        print("It was a tie!! 😥")
        return 0

    elif user_input == "S":
      winner = find_winner(user_input, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      if winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      if winner == 0:
        print("It was a tie!! 😥")
        return 0
    
    elif user_input == "B":
      return 0

    else:
      print("Invalid character, try again! ☠️") 
    

def displayScore(playerScore, computerScore):
  print(f'Scores:  💻Computer: {computerScore} 🧑Player: {playerScore}')

def comp_weapon():
  randomNum = random.randint(1,3)
  if randomNum == 1:
    return "R"
  if randomNum == 2:
    return "P"
  if randomNum == 3:
    return "S"

def find_winner(weaponPlayer, weaponComputer):
  #Computer choices
  if weaponComputer == "R":
    pc = "Rock"

  if weaponComputer == "P":
    pc = "Paper"
  
  if weaponComputer == "S":
    pc = "Scissor"
  
  #User choices
  if weaponPlayer == "R":
    user = "Rock"

  if weaponPlayer == "P":
    user = "Paper"
  
  if weaponPlayer == "S":
    user = "Scissor"

  print(f'You chose {user} 🧑\nComputer chose {pc} 💻🤖')

  #If pc wins
  if weaponPlayer == "R" and weaponComputer == "P":
    
    return 2
  
  elif weaponPlayer == "P" and weaponComputer == "S":
    
    return 2
  
  elif weaponPlayer == "S" and weaponComputer == "R":

    return 2

  
  #If Player wins
  
  elif weaponComputer == "R" and weaponPlayer == "P":
    
    return 1
  
  elif weaponComputer == "P" and weaponPlayer == "S":
    
    return 1
  
  elif weaponComputer == "S" and weaponPlayer == "R":

    return 1
  
  #If tie

  if weaponPlayer == "R" and weaponComputer == "R":
    
    return 0
  
  elif weaponPlayer == "P" and weaponComputer == "P":
    
    return 0
  
  elif weaponPlayer == "S" and weaponComputer == "S":

    return 0


def main():
  Score = None
  PlayerScore = 0
  PcScore = 0
  quit = True

  while quit:
    print(""" 
    ----------Rock 🪨, Paper 📃, Scissor ✂️ GAME ------------
    1. Play game 🎮
    2. Show Score 💯
    3. Quit 
     """)
    
    menuChoice = check_input.get_positive_int("Option: ")

    if menuChoice == 3:
      print("Thanks for Playing! 🕹️")
      break

    elif menuChoice == 1:
      Score = weapon_menu()
    
    elif menuChoice == 2:
      displayScore(PlayerScore, PcScore)

    
    #After the winner has been decided the weapon_meni will return 1(if player won), 2(if pc won), and 0(if it was a tie)
    if Score == 1:
      PlayerScore +=1
    elif Score == 2:
      PcScore += 1
    elif Score == 0:
      quit = True


    

main()



  



