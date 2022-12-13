import abc
import monster

class Decorator(monster.Monster, abc.ABC):
  def __init__(self,monst):
    super().__init__(monst.name, monst.hp)
    self._monster = monst
  
  def attack(self):
    return self._monster.attack()