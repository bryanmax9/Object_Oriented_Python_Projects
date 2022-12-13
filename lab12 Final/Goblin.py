import entity
import random
class Goblin(entity.Entity):
    '''This is the goblin class'''
    def __init__(self):
        super().__init__("Goblin",random.randint(6,10))
    def attack(self,entity):
        '''This is how the hero will take damage from the enemy'''
        damage = random.randint(4,8)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
