import entity
import random
class EasyOgre(entity.Entity):
    '''this is the easy ogre classne of easy enemies'''
    def __init__(self):
        super().__init__("Ogre",random.randint(3,5))
    def attack(self,entity):
        '''This is how the hero will take damage from the enemy'''
        damage = random.randint(1,4)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
