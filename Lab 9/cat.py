import abc
from lib2to3.pytree import HUGE
class Cat(abc.ABC):
  def __init__(self, name):
    self._name = name
    self._hunger = 5 

  @property
  def name(self):
    return self._name
  
  @property
  def hunger(self):
    return self._hunger

  def update_hunger(self, val):
    self._hunger += val
    if self._hunger < 1:
      self._hunger = 1
    elif self._hunger > 10:
      self._hunger = 10 

  def __str__(self):
    if self._hunger == 1:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ - - - - - - - - - |"
    
    elif self._hunger == 2:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + - - - - - - - - |"
    
    elif self._hunger == 3:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + + - - - - - - - |"
    
    elif self._hunger == 4:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + + + - - - - - - |"
    
    elif self._hunger == 5:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + + + + - - - - - |"
    
    elif self._hunger == 6:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + + + + + - - - - |"
    
    elif self._hunger == 7:
      
      return str(self.name) + ":\n" + "Starving       Full\n" + "|+ + + + + + + - - - |"
    
    elif self._hunger == 8:
      
      return str(self.name) + ":\n" + "Starving           Full\n" + "|+ + + + + + + + - - |"
    
    elif self._hunger == 9:
      
      return str(self.name) + ":\n" + "Starving           Full\n" + "|+ + + + + + + + + - |"
    
    elif self._hunger == 10:
      
      return str(self.name) + ":\n" + "Starving           Full\n" + "|+ + + + + + + + + + |"
    else:
      """ In case it is out of bound """
      return str(self.name) + ":\n" + "Starving           Full\n" + "|- - - - - - - - - - |" 

  @abc.abstractmethod
  def feed(self,player):
    pass

  @abc.abstractmethod
  def play(self, player):
    pass


  @abc.abstractmethod
  def pet(self,player):
    pass