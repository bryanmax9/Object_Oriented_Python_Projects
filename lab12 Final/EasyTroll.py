import entity
import random
class EasyTroll(entity.Entity):
    '''this is the easy troll class'''
    def __init__(self):
        super().__init__("Troll",random.randint(4,5))
    def attack(self,entity):
        '''This is how the hero will take damage from the enemy'''
        damage = random.randint(1,5)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
