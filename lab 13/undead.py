import monster
class Undead(monster.Monster):
  def __init__(self):
    super().__init__("Undead", 10)
  
  def attack(self):
    return 10
