import cat
class Ocelot(cat.Cat):
  def feed(self, player):
    if self.hunger <= 2:
      """ this is when hunger is all thw way les then 2. 2 to -infinity in math term """
      self.update_hunger(5) 
      player.take_damage(5)
      return str(self._name) + " is so hungry that when you set\ndown the steak, "+str(self.name)+ " mistakes you\nfor food and bites you for 5\ndamage."
    
    elif self.hunger <= 5:
      self.update_hunger(5)
      player.take_damage(2)
      return  str(self._name) + " is pretty hungry and\naccidentally bites you when it\ntakes the steak from your hand."
    
    elif self.hunger <= 8:
      self.update_hunger(5)
      player.take_damage(2)
      return  str(self._name) + " is pretty hungry and\naccidentally bites you when it\ntakes the steak from your hand."
    
    else:
      """ this woud be when hunger is greater then 8. From 8 to +infinity in mathematical terms"""
      self.update_hunger(5)
      player.take_damage(2)
      return str(self.name)+" will not eat becuase it's not hungry"


  def play(self, player):
    if self.hunger <= 2:
      """ this is when hunger is all thw way les then 2. 2 to -infinity in math term """
      self.update_hunger(-1)  
      player.take_damage(8)
      return str(self._name) + " is starving, they don't want\nto play right now. "+ str(self._name) + " stalks\nyou, chases you down, tackles you,\nand takes a large chunk out of your\narm for 8 damage."
    
    elif self.hunger <= 5:
      self.update_hunger(-2)
      player.take_damage(3)
      return  str(self._name) + " sniffs the basketball you have\nand then decides that you might be\ndelicious. "+str(self._name)+" bites you for 3\ndamage."
    
    elif self.hunger <= 8:
      self.update_hunger(-4)
      player.take_damage(2)
      return  str(self._name) + " jumps and plays with the\nsoccer ball you threw, then\naccidentally tackles you when it\ncomes running back."
    
    else:
      """ this woud be when hunger is greater then 8. From 8 to +infinity in mathematical terms"""
      self.update_hunger(-1)
      player.take_damage(0)
      return str(self.name)+" is so full, when your throw\nthe ball, it lays there sleepily in\nthe sun."
  
  def pet(self, player):
    if self.hunger <= 2:
      """ this is when hunger is all thw way les then 2. 2 to -infinity in math term """
      self.update_hunger(-1) 
      player.take_damage(8)
      return str(self._name) + " is starving, they don't want\nyou to pet him now. "+ str(self._name) + " stalks\nyou, chases you down, tackles you,\nand takes a large chunk out of your\narm for 8 damage."
    
    elif self.hunger <= 5:
      self.update_hunger(-1)
      player.take_damage(0)
      return  str(self._name) + " happily allows you to pet\nthem."
    
    elif self.hunger <= 8:
      self.update_hunger(-1)
      player.take_damage(0)
      return  str(self._name) + " happily allows you to pet\nthem."
    
    else:
      """ this woud be when hunger is greater then 8. From 8 to +infinity in mathematical terms"""
      self.update_hunger(-1)
      player.take_damage(0)
      return str(self.name)+" is incredibly full and purrs\nhappily as they drift off to sleep."
