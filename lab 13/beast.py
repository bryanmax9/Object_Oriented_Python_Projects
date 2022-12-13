import monster
class Beast(monster.Monster):
  def __init__(self):
    super().__init__("Beast", 20)
  
  def attack(self):
    return 5
