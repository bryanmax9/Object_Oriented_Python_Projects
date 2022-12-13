import random
import entity
class EasyTroll(entity.Entity):
  def __init__(self):
    super().__init__("Trol", random.randint(4,5))
  def attack(self, entity):
    dmg = random.randint(1,5)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."