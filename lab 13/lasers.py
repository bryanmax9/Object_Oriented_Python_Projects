import decorator
class Laser(decorator.Decorator):
  def __init__(self,monst):
    monst.name = monst.name + " with Lasers"
    monst.hp += 15
    super().__init__(monst)
    
  
  def attack(self):
    return self._monster.attack() + 10