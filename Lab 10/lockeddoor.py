import door
import random

class LockedDoor(door.Door):
    """This is one of three types of doors based off the door interface"""
    def __init__ (self):
        self._key_location = random.randint(1,3)
        self._input = 3
    
    def examine_door (self):
        """This is how we give the user a description of the door"""
        return """\nA locked door. Look around for the key """
    
    def menu_options (self):
        """This is the menu of the class"""
        return """1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock. """
    
    def get_menu_max (self):
        """This method will return a value that will be the max value of choice
        that the user can only have in the menu options"""
        return 3
    
    def attempt (self, option):
        """This will display a message about the user's choice"""
        self._input = option
        if option == 1:
          return """You looked under the mat """
        elif option == 2:
          return """You looked under the flower pot """
        else:
          return """You looked under the fake rock """
        
    def is_unlocked (self):
        """This is the method that will check user's choice"""
        if self._input == self._key_location:
          return True
        else:
          return False
    
    def clue (self):
        """This method will display a message of a clue"""
        return """\nLook somewhere else """
    
    def success (self):
        """This is the message that will be displayed if the user was successful"""
        return """\nCongratulations, you got the key and opened the door. """