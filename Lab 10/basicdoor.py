import door
import random

class BasicDoor(door.Door):
    """This is one of three types of doors based off the door interface"""
    def __init__ (self):
        self._state = random.randint(1,2)
    
    def examine_door (self):
        """This is how we give the user a description of the door"""
        return "\nA door that is either pushed or pulled."
    
    def menu_options (self):
        """This is the menu of the class"""
        menu = "1.Push\n2.Pull"
        return menu
    
    def get_menu_max (self):
        """This method will return a value that will be the max value of choice
        that the user can only have in the menu options"""
        return int(2)
    
    def attempt (self, option):
        """This will display a message about the user's choice"""
        self._input = option
        if option == 1:
            return "You pushed the door"
        else:
            return "You pulled the door"
        
    def is_unlocked (self):
        """This is the method that will check user's choice"""
        if self._input == self._state:
            return True
        else:
            return False
    
    def clue (self):
        """This method will display a message of a clue"""
        return "\nTry the other way."
    
    def success (self):
        """This is the message that will be displayed if the user was successful"""
        return "\nCongratulations, you opened the door."
    
