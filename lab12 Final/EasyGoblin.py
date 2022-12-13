import entity
import random
class EasyGoblin(entity.Entity):
    '''One of easy enemies as goblin'''
    def __init__(self):
        super().__init__("Goblin",random.randint(3,4))
    def attack(self,entity):
        '''This is how the hero will take damage from the enemy'''
        damage = random.randint(1,3)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
