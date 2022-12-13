import random
import entity
class Ogre(entity.Entity):
  def __init__(self):
    super().__init__("Ogro rey", random.randint(8,12))
  def attack(self, entity):
    dmg = random.randint(6,10)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."