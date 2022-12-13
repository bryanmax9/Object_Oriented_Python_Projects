import entity
import random
import map
class Hero(entity.Entity):
    '''This is the class that will build the hero needed for the game'''
    def __init__(self,name):
        super().__init__(name,25)
        self._loc = [0,0]
    @property
    def loc(self):
        '''This is a getter method that will be used to get the location of the hero'''
        return self._loc
    def attack(self,entity):
        '''This a modified version of the attack that was taken from the entity abstract class
        and is now being redefined for this class purpose'''
        damage = random.randint(2,5)
        entity.take_damage(damage)
        return self.name + "attacks a " + entity.name + "for " + str(damage) + "damage."
    def go_north (self):
        '''This is the method that will allow the player to move north and not go out
        of bounds on the map'''
        mapita = map.Map()
        if (self._loc[0]-1 < 0):
            return "x"
        else:
            self._loc[0] -= 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_south (self):
        '''This is the method that will allow the player to move south and not go out
        of bounds on the map'''
        mapita = map.Map()
        if (self._loc[0]+1 > 4):
            return "x"
        else:
            self._loc[0] += 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_east (self):
        '''This is the method that will allow the player to move east and not go out
        of bounds on the map'''
        mapita = map.Map()
        if (self._loc[1]+1 > 4):
            return "x"
        else:
            self._loc[1] += 1
            return mapita[self.loc[0]][self.loc[1]]
    def go_west (self):
        '''This is the method that will allow the player to move west and not go out
        of bounds on the map'''
        mapita = map.Map()
        if (self._loc[1]-1 < 0):
            return "x"
        else:
            self._loc[1] -= 1
            return mapita[self.loc[0]][self.loc[1]]
