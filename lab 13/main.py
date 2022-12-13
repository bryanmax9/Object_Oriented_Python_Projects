import alien
import beast
import undead
import check_input
import lasers
import fire
import flying
import poison
def main():
  print("Monster Maker! 👻")
  print(""" 
  Choose a base monster:
  1. Alien 👽
  2. Beast 👹
  3. Undead 🧟
   """)
  usr_choice = check_input.get_int_range("Enter choice: ",1,3)

  

  if usr_choice == 1:
    monstruo = alien.Alien()
  elif usr_choice == 2:
    monstruo = beast.Beast()
  else:
    monstruo = undead.Undead()
  
  frootloops = True
  while frootloops:
    print(monstruo)
    print(""" 
    Add an ability:
    1. Fire
    2. Flying
    3. Lasers
    4. Poison
    5. Quit
     """)
    usr_ability = check_input.get_int_range("Enter ability: ",1,5)
    if usr_ability == 1:
      monstruo = fire.Fire(monstruo)
    elif usr_ability == 2:
      monstruo = flying.Flying(monstruo)
    elif usr_ability == 3:
      monstruo = lasers.Laser(monstruo)
    elif usr_ability == 4:
      monstruo = poison.Poison(monstruo)
    else:
      print("Your final monster 👻 is:")
      print(f"Name: {monstruo.name}📛")
      print(f"Hp: {monstruo.hp}💓")
      print(f"Attack: {monstruo.attack()}⚔️")
      frootloops = False
      break

      

main()