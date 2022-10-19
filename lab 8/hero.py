import random
import entity
class Hero(entity.Entity):
  def sword_attack(self, dragon):
    damage = random.randint(1,6) + random.randint(1,6)
    dragon.take_damage(damage)
    return "You slash the " + str(dragon._name) + "with your sword for " + str(damage) + " damage."

  
  def arrow_attack(self, dragon):
    damage = random.randint(1,12)
    dragon.take_damage(damage)
    return "You hit the" + str(dragon._name) + "with an arrow for " + str(damage) + " damage."