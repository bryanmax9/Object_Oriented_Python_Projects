class Rectangle:
        """Represents a rectangle on the coordinate plane.
        Attributes:
            x (int): location x of the rectangle.
            y (int): location y of the rectangle.
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """

        def __init__(self, w=1, h=1 , x=0, y=0):
            """Sets the rectangle’s x, y, width, height."""
            self.x = x
            self.y = y
            self.width = w
            self.height = h
        
        def get_coords(self):
          return self.x , self.y
        
        def get_width(self):
          return self.width
        
        def get_height(self):
          return self.height

        def move_up(self):
          self.x -= 1
        
        def move_down(self):
          self.x += 1

        def move_left(self):
          self.y -= 1
        
        def move_right(self):
          self.y += 1

        def translate(self, dx, dy):
            """Shifts the rectangle’s location by dx, dy."""
            self.x += dx
            self.y += dy

        def __str__(self):
            """ “““Returns the rectangle as a string.””” """
            return "Loc=(" + str(self.x) + ", " + str(self.y) + "): W=" + str(self.width) + " H=" + str(self.height)