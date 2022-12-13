import entity
import random
class Ogre(entity.Entity):
    """This is the ogre class, one of the harder enemies"""
    def __init__(self):
        super().__init__("Goblin",random.randint(8,12))
    def attack(self,entity):
        damage = random.randint(6,10)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
