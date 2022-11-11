import check_input 
import enemy
import hero
import map
import random


def movimiento(choice,player,direction):
    """ choice is the letter that is in the position we are going """
    """ First we will check that itt a letter and if is x then just dont check the letter in thatt position """
    if choice != "x":
        
        if choice == "m":
            enemigo = enemy.Enemy()
            print(f"You encounter a {enemigo.name}")
            print(enemigo)
            while enemigo.hp != 0:
                print(f""" 
1. Attack {enemigo.name}
2. Run Away
             """)
                print("Enter Choice: ", end="")
                opcion = check_input.get_int_range(1,2)
                if opcion == 1:
                    print(player.attack(enemigo), "⚔️")
                    if enemigo.hp == 0:
                        """ if player kills the monster before then you slain it and stay in the new position """
                        print(f"You have slain a {enemigo.name} 💀⚔️🩸")
                        """ Since player didnt die, then return false """
                        return False

                    print(enemigo.attack(player), "⚔️")

                    if player.hp == 0:
                        """ if the player dies while fighting then return True to main """
                        return True
                if opcion == 2:
                    direction = random.randint(1,4)
                    """ If you run away, then you step back and prints that you ran """
                    if direction == 1:
                        """ if you went north """
                        player.go_south()
                    elif direction == 2:
                        """ if you went south """
                        player.go_north()
                    elif direction == 3:
                        """ if you went east(right) """
                        player.go_west()
                    elif direction == 4:
                        """ if you went west(left) """
                        player.go_east()

                    print("You ran away! ")
                    """ since player didnt die return false """
                    return False
        
        elif choice == "i":
            print("You found a health potion! You drink it to restore your HP.")
            player.heal()
            return False
        
        elif choice == "s":
            print("You are back where you started...")
            return False
        elif choice == "f":
            print(player._m1.show_map(player.loc))
            print("Congratulations! You found the exit.")
            return "E"
        elif choice == "n":
            print("There is nothing here...")


        
    

def main():

    playerName = input("What is your name, traveler? ")
    Player = hero.Hero(playerName)
    m1 = map.Map()
    loop = False
    print(Player)
    print(Player._m1.show_map(Player.loc))
    while not loop:
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        print("Enter Choice: ", end="")
        usr_option = check_input.get_int_range(1,5)
        if usr_option == 1:
            choice1 = Player.go_north()
            """ we first reveal the location we are going """
            m1.reveal(Player.loc)

            if choice1 == "x":
                print("You cannot go that way")
            else:
                player_die_or_won = movimiento(choice1,Player,usr_option)
                if player_die_or_won == True:
                    """ if player dies in battle finish the game """
                    print("you have been slain! 💀⚔️🩸")
                    print("You Lost")
                    loop = True
                    break
                elif player_die_or_won == "E":
                    print("Game Over 🎮")
                    break
                
            
            
            print(Player)
            print(Player._m1.show_map(Player.loc))
        elif usr_option == 2:
            choice2 = Player.go_south()
            """ we first reveal the location we are going """
            m1.reveal(Player.loc)

            if choice2 == "x":
                print("You cannot go that way")
            
            else:
                player_die_or_won = movimiento(choice2,Player,usr_option)
                if player_die_or_won == True:
                    """ if player dies in battle finish the game """
                    print("you have been slain! 💀⚔️🩸")
                    print("You Lost")
                    loop = True
                    break
                elif player_die_or_won == "E":
                    print("Game Over 🎮")
                    loop = True
                    break
            print(Player)
            print(Player._m1.show_map(Player.loc))
        elif usr_option == 3:
            choice3 = Player.go_east()
            """ we first reveal the location we are going """
            m1.reveal(Player.loc)

            if choice3 == "x":
                print("You cannot go that way")
            else:
                player_die_or_won = movimiento(choice3,Player,usr_option)
                if player_die_or_won == True:
                    """ if player dies in battle finish the game """
                    print("you have been slain! 💀⚔️🩸")
                    print("You Lost")
                    loop = True
                    break
                elif player_die_or_won == "E":
                    print("Game Over 🎮")
                    loop = True
                    break

            print(Player)
            print(Player._m1.show_map(Player.loc))
        elif usr_option == 4:
            choice4 = Player.go_west()
            """ we first reveal the location we are going """
            m1.reveal(Player.loc)

            if choice4 == "x":
                print("You cannot go that way")
            
            else:
                if player_die_or_won == True:
                    """ if player dies in battle finish the game """
                    print("you have been slain! 💀⚔️🩸")
                    print("You Lost")
                    loop = True
                    break
                elif player_die_or_won == "E":
                    print("Game Over 🎮")
                    loop = True
                    break
            print(Player)
            print(m1.show_map(Player.loc))
        elif usr_option == 5:
            loop = True
            print("Thanks for Playing! 🎮")
            break





       



main()