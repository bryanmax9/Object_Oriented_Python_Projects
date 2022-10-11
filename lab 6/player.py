
import die
class Player:
  def __init__(self):
    self.dice = [die.Die(), die.Die(),die.Die()]
    self.dice.sort()
    self.points = 0

  def get_points(self):
    return self.points

  def roll_dice(self):
    """ sorts each  """
    for d in self.dice:
      d.roll()

  def has_pair(self):
    """ returing true if two dice are same value """
    if  self.dice[0].__eq__(self.dice[1]):
      """ if the first in the list and the sencond are the same value, add 1 to points """
      self.points += 1 
      return True
    elif self.dice[1].__eq__(self.dice[2]):
      """ if the second in the list and the third are the same value, add 1 to points """
      self.points += 1
      return True
    elif self.dice[0].__eq__(self.dice[-1]):
      """ if the first in the list and the last are thesame value, add 1 to points """
      self.points += 1
      return True
    
    False
  
  def has_three_of_a_kind(self):
    """ if the three die are the same value, add 3 to points """
    if self.dice[0] == self.dice[1] == self.dice[-1]:
      self.points += 3
      return True
    False
  
  def has_series(self):
    """ if the values of the die are in a sequence like 123 or 234 or 345 or 456 then add 2 points """

    s = ''.join(str(i) for i in self.dice)
    if '123' in s or '234' in s or '345' in s or '456' in s:
      self.points += 2
      return True
    
    return False
  
  def __str__(self):
    return "D1=" + str(self.dice[0]) + "," + "D2=" + str(self.dice[1]) + "," + "D3=" + str(self.dice[-1]) 
