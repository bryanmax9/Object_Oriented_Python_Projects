import random
import entity
class Troll(entity.Entity):
  def __init__(self):
    super().__init__("Trol rey", random.randint(10,14))
  def attack(self, entity):
    dmg = random.randint(8,12)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."