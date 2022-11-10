import entity
import random
import map
class Hero(entity.Entity):
  def __init__(self, name):
    super().__init__(name, 25)
    self._loc = [0,0]
    self._m1 = map.Map()

  
  @property
  def loc(self):
    return self._loc
  
  def attack(self, entity):
    damage_random = random.randint(2,5)
    entity.take_damage(damage_random)
    return f"{self.name} attacks a {entity.name} for {damage_random} damage."
  
  def go_north (self):
    if (self._loc[0]-1 < 0):
      return "x"
    else:
      self._loc[0] -= 1
      return self._m1[self._loc[0]][self._loc[1]]
      
  def go_south (self):
    if (self._loc[0]+1 > 4):
      return "x"
    else:
      self._loc[0] += 1
      return self._m1[self._loc[0]][self._loc[1]]

  def go_east (self):
    if (self._loc[1]+1 > 4):
      return "x"
    else:
      self._loc[1] += 1
      return self._m1[self._loc[0]][self._loc[1]]

  def go_west (self):
    
    if (self._loc[1]-1 < 0):
      return "x"
    else:
      self._loc[1] -= 1
      return self._m1[self._loc[0]][self._loc[1]]