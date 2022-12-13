import decorator
class Flying(decorator.Decorator):
  def __init__(self,monst):
    monst.name = "Flying " + monst.name
    monst.hp += 7
    super().__init__(monst)
    
  
  def attack(self):
    return self._monster.attack() + 2