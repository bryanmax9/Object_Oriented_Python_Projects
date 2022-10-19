class Player:
  def __init__(self):
    self._hp = 25
  
  @property
  def hp(self):
    return self._hp
  
  def take_damage(self, dmg):
    self._hp -= dmg
  
  def __str__(self):
    return "You have " + str(self._hp) +" hp."