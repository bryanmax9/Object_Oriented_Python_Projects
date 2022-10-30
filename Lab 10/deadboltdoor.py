import door
import random

class DeadBoltDoor(door.Door):
    def __init__ (self):
        """1 = unlocked, 0 = unlock. Initializing one bolt unlocked an one locked randomly"""
        self._bolt1 = random.randint(0,1) 
        self._bolt2 = random.randint(0,1) 

    def examine_door (self):
        """This is how we give the user a description of the door"""
        return """\nA door with two deadbolts. Both need to be unlocked\nto open the door, but you can't tell if\neach one is locked or unlocked. """
    
    def menu_options (self):
        """This is the menu of the class"""
        return """1. Toggle bolt 1\n2. Toggle bolt 2 """
    
    def get_menu_max (self):
        """This method will return a value that will be the max value of choice
        that the user can only have in the menu options"""
        return 2
    
    def attempt (self, option):
        """This will display a message about the user's choice"""
        if option == 1:
            if self._bolt1 == 0:
                """ if bolt 1 is locked then we will randomize its state """
                self._bolt1 = random.randint(0,1) 

            return """You toggle the first bolt. """

        elif option == 2:
            if self._bolt2 == 0:
                """ if bolt 2 is locked then we will randomize its state """
                self._bolt2 = random.randint(0,1) 

            return """You toggle the second bolt. """
    
    def is_unlocked (self):
        """This is the method that will check if we unlocked the door"""
        if self._bolt1 == 1 and self._bolt2 == 1:
          return True
        else:
          return False
    
    def clue (self):
        """See if at least one of the bolts is unlocked"""
        if self._bolt1 == 1 or self._bolt2 == 1:
            """if one of the bolts is unlocked then let the player know that """
            return """\nYou jiggle the door…it seems\nlike one of the bolts is unlocked. """
        else:
            """if none of the bolts is open then let the user know """
            
            return """\n… it seems like it's\ncompletely locked. """
    
    def success (self):
        """This is the message that will be displayed if the user was successful"""
        return """\nYou unlocked both deadbolts\nand opened the door. """