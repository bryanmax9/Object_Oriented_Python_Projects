import random
import entity
class EasyOgre(entity.Entity):
  def __init__(self):
    super().__init__("Ogro", random.randint(3,5))
  def attack(self, entity):
    dmg = random.randint(1,4)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."