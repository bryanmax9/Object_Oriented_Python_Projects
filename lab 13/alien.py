import monster
class Alien(monster.Monster):
  def __init__(self):
    super().__init__("Alien",30)
  
  def attack(self):
    return 2