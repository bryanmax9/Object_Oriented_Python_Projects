import random
import entity
class EasyGoblin(entity.Entity):
  def __init__(self):
    super().__init__("Goblino", random.randint(3,4))
  def attack(self, entity):
    dmg = random.randint(1,3)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."