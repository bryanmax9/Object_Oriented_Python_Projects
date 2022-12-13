import entity
import random
class Troll(entity.Entity):
    """"This is the troll class that is an enemy"""
    def __init__(self):
        super().__init__("BigTroll",random.randint(10,14))
    def attack(self,entity):
        damage = random.randint(8,12)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
