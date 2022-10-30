#Group 12
#Ramon Alaysa, Bryan Tineo
# October 25 2022
import random
import check_input
import deadboltdoor
import lockeddoor
import basicdoor

def open_door(door):
    """This is a method that will work with one of the door types being passed in and will
    request various methods that should be in these door types due to a common interface"""
    print(door.examine_door())
    print(door.menu_options())
    choice = int(check_input.get_int_range(1, door.get_menu_max()))
    print(door.attempt(choice))
    loop = True
    while loop:
        if bool(door.is_unlocked()) == False:
            print(door.clue())
            print(door.menu_options())
            choice = int(check_input.get_int_range(1, door.get_menu_max()))
            print(door.attempt(choice))
        else:
            loop = False
            print(door.success())

def main ():
    """This is how the game will work. The main will create three doors that are random
    and set them into a list that will be called on later. The main will display the
    entrance statement and pass one of the doors in the list into the open_door method
    and that is when the game will start. This will happen until the doors list has been
    completely passed through"""
    door = []
    for i in range(0,3):
        key = random.randint(1,3)
        if key == 1:
            door.append(basicdoor.BasicDoor())
        elif key == 2:
            door.append(lockeddoor.LockedDoor())
        elif key == 3:
            door.append(deadboltdoor.DeadBoltDoor())
    print("Welcome to the Escape Room🎮.\nYou must unlock 3 doors 🚪🚪🚪 to\nescape...🏃‍♂️💨\t")
    for i in door:
        open_door(i)
    print("\nCongratulations! You escaped...this time. 🏃‍♂️💨 🚪")
        

main()
    
