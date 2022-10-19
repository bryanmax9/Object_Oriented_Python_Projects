import entity
import random
class Dragon(entity.Entity):
  def basic_attack(self, hero):
    damage = random.randint(4,8)
    hero.take_damage(damage)
    return str(self.name) + " smashes you with its tail for " + str(damage) + " damage!"
  def special_attack(self,hero):
    damage = random.randint(4,8)
    hero.take_damage(damage)
    return str(self.name) + " slashes you with its claws for " + str(damage) + " damage!"
  