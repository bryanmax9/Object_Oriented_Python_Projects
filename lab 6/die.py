import random
class Die:
  def __init__(self, sides=6):
    self.sides = sides
    self.value = self.roll()

  def roll(self):
    self.value = random.randint(1, self.sides)
    return self.value

  def __str__(self):
    return str(self.value)


  def __lt__(self, other):
    return self.value < other.value

  def __eq__(self, other):
    return self.value == other.value

  def __sub__(self, other):
    return self.value - other.value