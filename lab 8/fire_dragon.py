import dragon
import random
class Fire_dragon(dragon.Dragon):
  def __init__(self, name, max_hp, f_shots):
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, hero):
    if self.f_shots > 0:
      damage = random.randint(5,9)
      self.f_shots -= 1
      hero.take_damage(damage)
      return str(self.name) + " engulfs you in flames for " + str(damage) + " damage!"
    else:
      return str(self.name) + " is out of fire shots" 