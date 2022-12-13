import abc
class Monster(abc.ABC):
  def __init__(self,name,hp):
    self._name = name
    self._hp = hp
  
  @property
  def name(self):
    return self._name
  
  @property
  def hp(self):
    return self._hp
  
  @name.setter
  def name(self, name):
    self._name = name
  
  @hp.setter
  def hp(self, hp):
    self._hp = hp
  
  def __str__(self):
    return f"Name: {self.name}\nHp: {self._hp}\nAttack: {self.attack()}"
  
  @abc.abstractclassmethod
  def attack(self):
    pass

  
  
