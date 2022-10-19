import dragon
import random
class Flying_dragon(dragon.Dragon):
  def __init__(self, name, max_hp, swoops):
    super().__init__(name, max_hp)
    self.swoops = swoops

  def special_attack(self, hero):
    if self.swoops > 0:
      damage = random.randint(5,8)
      self.swoops -= 1
      hero.take_damage(damage)
      return str(self.name) + " swoops at you for " + str(damage) + " damage!"
    else:
      return str(self.name) + " is out of swoop attacks" 