import cat
import ocelot
import player
import tabby
import tiger
import check_input
def interact_cat(cat, player):
  print(player)
  print(cat)
  print(""" 
  Cat Menu:
  1. Feed your cat 🍗
  2. Play with your cat ⚽🐈
  3. Pet your cat ❣️😺
   """)
  print("Enter choice: ", end = '')
  usr_choice = int(check_input.get_int_range(1,3))
  
  if usr_choice == 1:
    print(cat.feed(player))
  elif usr_choice == 2:
    print(cat.play(player))
  elif usr_choice == 3:
    print(cat.pet(player))

def main():
  print(""" 
  🐾Cat Selection🐾:
  1. Tabby Cat 🐈‍⬛
  2. Ocelot 🐈
  3. Tiger 🐅
   """)

  print("Enter choice: ", end = '')
  usr_choice = int(check_input.get_int_range(1,3))
  pet_name = input("Name your kitty😺: ")

  if usr_choice == 1:
    pet_cat = tabby.Tabby(pet_name)
  elif usr_choice == 2:
    pet_cat = ocelot.Ocelot(pet_name)
  elif usr_choice == 3:
    pet_cat = tiger.Tiger(pet_name)

  usr = player.Player()
  while usr.hp > 0:
    print()
    interact_cat(pet_cat, usr)
  
  print("Your cat killed you... 🩸💀🐾")
  






main()