import abc
class Door (abc.ABC):
    """This is the interface for future door classes to be based on"""
    @abc.abstractmethod
    def examine_door (self):
        """This is how we access the menu options class itself"""
        pass
    
    @abc.abstractmethod
    def menu_options (self):
        """This is how we access the menu class itself"""
        pass
    
    @abc.abstractmethod
    def get_menu_max (self):
        """This is how we access the get menu max class itself"""
        pass
    
    @abc.abstractmethod
    def attempt (self, option):
        """This will display a message about the user's choice"""
        pass
    
    @abc.abstractmethod
    def is_unlocked (self):
        """This is the method that will check user's choice"""
        pass
    
    @abc.abstractmethod
    def clue (self):
        """This method will display a message of a clue"""
        pass
    
    @abc.abstractmethod
    def success (self):
        """This is the message that will be displayed if the user was successful"""
        pass
