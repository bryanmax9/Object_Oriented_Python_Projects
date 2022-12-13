import decorator
class Fire(decorator.Decorator):
  def __init__(self,monst):
    monst.name = "Firey " + monst.name
    monst.hp += 10
    super().__init__(monst)
    
  
  def attack(self):
    return self._monster.attack() + 5