import random
import check_input

def userChose(letterChoice):
  #User choices
  
  if letterChoice == "R" or letterChoice == "r":
    
    return "Rock"
  if letterChoice == "P" or letterChoice == "p":
    
    return "Paper"
  
  if letterChoice == "S" or letterChoice == "s":
    
    return "Scissor"


def weapon_menu():
  #The computer choice will be set before the weapon menu
  pc_input = comp_weapon()
  #Computer choices
  if pc_input == "R":
    pc_input = "Rock"

  elif pc_input == "P":
    pc_input = "Paper"
  
  elif pc_input == "S":
    pc_input = "Scissor"

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

    if user_input == "R" or "r":
      nameChoice = userChose(user_input)
      winner = find_winner(nameChoice, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      elif winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      elif winner == 0:
        print("It was a tie!! 😥")
        return 0

    elif user_input == "P" or "p":
      nameChoice = userChose(user_input)
      winner = find_winner(nameChoice, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      elif winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      elif winner == 0:
        print("It was a tie!! 😥")
        return 0

    elif user_input == "S" or "s":
      nameChoice = userChose(user_input)
      winner = find_winner(nameChoice, pc_input)
      if winner == 1:
        print("User Won!! 👻🍾🥂")
        return 1
      elif winner == 2:
        print("Computer Won!! 💻🤖")
        return 2
      elif winner == 0:
        print("It was a tie!! 😥")
        return 0
    
    elif user_input == "B" or "b":
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
  
  print(f'You chose {weaponPlayer} 🧑\nComputer chose {weaponComputer} 💻🤖')

  #If pc wins
  if weaponPlayer == "Rock" and weaponComputer == "Paper":
    
    return 2
  
  elif weaponPlayer == "Paper" and weaponComputer == "Scissor":
    
    return 2
  
  elif weaponPlayer == "Scissor" and weaponComputer == "Rock":

    return 2

  
  #If Player wins
  
  elif weaponComputer == "Rock" and weaponPlayer == "Paper":
    
    return 1
  
  elif weaponComputer == "Paper" and weaponPlayer == "Scissor":
    
    return 1
  
  elif weaponComputer == "Scissor" and weaponPlayer == "Rock":

    return 1
  
  #If tie

  elif weaponPlayer == "Rock" and weaponComputer == "Rock":
    
    return 0
  
  elif weaponPlayer == "Paper" and weaponComputer == "Paper":
    
    return 0
  
  elif weaponPlayer == "Scissor" and weaponComputer == "Scissor":

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



  



