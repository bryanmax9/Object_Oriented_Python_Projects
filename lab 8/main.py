from optparse import Option
import random
from unicodedata import name
import entity
import dragon
import fire_dragon
import flying_dragon
import hero
def main():
  control = True
  f_shots = 3
  swoops = 5

  """ starting game getting username """
  print("What is your name, challenger? 🎮")
  name_usr = input("")

  """ setting Hero and dragons 🐉🐉🐉 """
  h = hero.Hero(name_usr,50)
  Nadder = dragon.Dragon("Deadly Nadder", 10)
  Gronckle = fire_dragon.Fire_dragon("Gronckle",15,f_shots)
  Timberjack = flying_dragon.Flying_dragon("Timberjack", 20,swoops)
  dragons = [ Nadder, Gronckle , Timberjack ]

  print("Welcome to dragon training 🐉⚔️, ", name_usr)
  print("You must defeat 3 dragons.")

  """ Entering the Game loops of attacks!⚔️🔥🔥🔥 """
  while control:
    
    print()
    print(h)
    if Nadder in dragons:
      print("1. Attack ", Nadder, "🐉☠️")
    if Gronckle in dragons:
      print("2. Attack ", Gronckle, "🐉🔥")
      print("Fire Shots remaining: ", f_shots, "🔥")
    if Timberjack in dragons:
      print("3. Attack ", Timberjack, "🐉💨")
      print("Swoop attacks remaining: ", swoops,"💨")
    usr_choice = int(input("Choose a dragon to attack: "))

    
    choosed_dragon = None

    """ Check if dragon still in list """
    while choosed_dragon == None:
      
      if usr_choice == 1 or usr_choice == 2 or usr_choice == 3:
        if usr_choice == 1 and Nadder in dragons:
          
          choosed_dragon = Nadder
        elif usr_choice == 2 and Gronckle in dragons:
          
          choosed_dragon = Gronckle
        elif usr_choice == 3 and Timberjack in dragons:
          
          choosed_dragon = Timberjack
        else:
          """ if dragon is no longer in list """
          usr_choice = int(input("Choose a dragon to attack: "))
      else:
        """ if user didnt input correctly """
        usr_choice = int(input("Choose a dragon to attack: "))

    print(""" 
    Attack with⚔️:
    1. Arrow (1 D12) 🏹
    2. Sword (2 D6)  🤺
     """)
    
    weapon = int(input("Enter weapon: "))

    """ check if weapon input is in range """
    while weapon > 2 or weapon < 1:
      print("Enter 1 or 2")
      weapon = int(input("Enter weapon: "))
    
    if weapon == 1:
      """ attack with arrow if it is option 1 🏹"""
      
      attack = h.arrow_attack(choosed_dragon)
      print(attack)

      """ Choosing a random dragon attack """
      """ if 1 = basic attack, if 2 = especial attack """
      random_dragonattack = random.randint(1,2)
      if random_dragonattack == 1:
        drag_attack = choosed_dragon.basic_attack(h)
        print(drag_attack)
      elif random_dragonattack == 2:
        drag_attack = choosed_dragon.special_attack(h)
        print(drag_attack)
    
    elif weapon == 2:
      """ attack with sword if it is option 2 🤺"""
      
      attack = h.sword_attack(choosed_dragon)
      print(attack)

      """ Choosing a random dragon attack """
      """ if 1 = basic attack, if 2 = especial attack """
      random_dragonattack = random.randint(1,2)
      if random_dragonattack == 1:
        drag_attack = choosed_dragon.basic_attack(h)
        print(drag_attack)
      elif random_dragonattack == 2:
        drag_attack = choosed_dragon.special_attack(h)
        print(drag_attack)
    
    
    """ Checking if any dragon is dead """
    
    if Nadder.hp == 0:
      if Nadder in dragons:
        dragons.remove(Nadder)
    if Gronckle.hp == 0:
      if Gronckle in dragons:
        dragons.remove(Gronckle)
    if Timberjack.hp == 0:
      if Timberjack in dragons:
        dragons.remove(Timberjack)

    """ After attacking checking for an end """

    """ Case were Hero dies ☠️💀 """
    if h.hp < 1:
      print("""
      Sorry but You have been defeated... ☠️⚰️
      Thanks for playing. 🎮
       """)
      control = False
      break
    elif not dragons:
      """ When list is empty (No dragons left) """
      print(""" 
      ⚔️Congratulations! You have defeated
      all 3 dragons, you have passed the
      trials.⚔️
       """)
      break



    



    
    






main()