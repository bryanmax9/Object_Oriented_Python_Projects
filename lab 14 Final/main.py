import puppy
import check_input
def main():
    """ creating the puppy first """
    player = puppy.Puppy()
    """ creating the loop control """
    control = True
    print("Congratulations on your new puppy! 🐕‍🦺")
    while(control):
        print("What would you like to do? 🐾")
        print("1. Feed the puppy 🦴")
        print("2. Play with the puppy ⚽")
        print("3. Quit 🏃💨")
        choice = check_input.get_int_range("Enter choice: ", 1, 3)
        if (choice == 1):
            player.give_food()
        elif (choice == 2):
            player.throw_ball()
        elif (choice == 3):
            control = False
            break
main()
