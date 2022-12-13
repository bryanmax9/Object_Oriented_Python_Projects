# Group 6
# Alarik Damrow , Anthony Hernandez-Torres
# November 16 2022
import random
import hero
import map
import exp_factory
import beg_factory
import check_input

def main():
    '''This is how the game will run and it is resposible for the creation of classes
    and handling user input for decisions being made and also what are the outcomes
    of such decisions'''
    i = 2
    playername = input ("What is your name, traveler? ")
    Player = hero.Hero(playername)
    print ("Difficulty")
    print ("1. Beginner")
    print ("2. Expert")
    print("",end="")
    Dif = check_input.get_int_range(1,2)
    if (Dif == 1):
        Fact = beg_factory.BeginnerFactory()
    elif (Dif == 2):
        Fact = exp_factory.ExpertFactory()
    m1 = map.Map()
    Trigger = False
    while not Trigger:
        print(Player)
        print (m1.show_map(Player.loc))
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        print("Enter choice:", end="")
        ch1 = check_input.get_int_range(1,5)
        if (ch1 == 1):
            r1 = Player.go_north()
            m1.reveal(Player.loc)
            if r1 == "x":
                print ("You cannot go that way...")
            print (m1.show_map(Player.loc))
        elif (ch1 == 2):
            r1 = Player.go_south()
            m1.reveal(Player.loc)
            if r1 == "x":
                print ("You cannot go that way...")
            print (m1.show_map(Player.loc))
        elif (ch1 == 3):
            r1 = Player.go_east()
            m1.reveal(Player.loc)
            if r1 == "x":
                print ("You cannot go that way...")
            print (m1.show_map(Player.loc))
        elif (ch1 == 4):
            r1 = Player.go_west()
            m1.reveal(Player.loc)
            if r1 == "x":
                print ("You cannot go that way...")
            print (m1.show_map(Player.loc))
        elif (ch1 == 5):
            Trigger = True
        loc = Player.loc
        letter = m1[loc[0]][loc[1]]
        if letter == "m":
            Enemy = Fact.create_random_enemy()
            Fight = False
            print("You encounter a "+str(Enemy))
            while not Fight:
                print("1. Attack "+str(Enemy.name))
                print("2. Run Away")
                print("Enter choice", end= "")
                ch2 = check_input.get_int_range(1,2)
                if ch2 == 1:
                    Player.attack(Enemy)
                    if (Enemy.hp == 0):
                        print(str(Enemy.name)+ "'s Hp is "+str(Enemy.hp))
                        print(str(Enemy.name)+" was defeated")
                        m1.remove_at_loc(Player.loc)
                        Fight = True
                    elif (Player.hp == 0):
                        print("You have been deafeated")
                        print("Game over!")
                        Fight = True
                        Trigger = True
                    else:
                        print(str(Enemy.name)+ "'s Hp is "+str(Enemy.hp))
                        Enemy.attack(Player)
                        print("Your hp is "+str(Player.hp))
                if ch2 == 2:
                    ch3 = random.randint(1,4)
                    if (ch3 == 1):
                        r1 = Player.go_north()
                        m1.reveal(Player.loc)
                        if r1 == "x":
                            print ("You cannot go that way...")
                        print (m1.show_map(Player.loc))
                    elif (ch3 == 2):
                        r1 = Player.go_south()
                        m1.reveal(Player.loc)
                        if r1 == "x":
                            print ("You cannot go that way...")
                        print (m1.show_map(Player.loc))
                    elif (ch3 == 3):
                        r1 = Player.go_east()
                        m1.reveal(Player.loc)
                        if r1 == "x":
                            print ("You cannot go that way...")
                        print (m1.show_map(Player.loc))
                    elif (ch3 == 4):
                        r1 = Player.go_west()
                        m1.reveal(Player.loc)
                        if r1 == "x":
                            print ("You cannot go that way...")
                        print (m1.show_map(Player.loc))
                    Fight = True
        elif letter == "n":
            print("There is nothing here...")
        elif letter == "s":
            print("You are back where you started...")
        elif letter == "i":
            print("You found a Health Potion! You drink it to restore your health.")
            Player.heal()
            m1.remove_at_loc(Player.loc)
            print(Player)
        elif letter == "f":
            print("Congratulations! You found the stairs to the next floor of the dungeon.")
            print (m1.show_map(Player.loc))
            if i == 4:
                i = 1
            m1.load_map(i)
            i += 1
            
                    
                    

main()
