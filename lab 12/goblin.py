import random
import entity
class Goblin(entity.Entity):
  def __init__(self):
    super().__init__("Goblino rey", random.randint(6,10))
  def attack(self, entity):
    dmg = random.randint(4,8)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."