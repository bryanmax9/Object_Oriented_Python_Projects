import decorator
class Poison(decorator.Decorator):
  def __init__(self,monst):
    monst.name = "Poison " + monst.name
    monst.hp += 8
    super().__init__(monst)
    
  
  def attack(self):
    return self._monster.attack() + 13