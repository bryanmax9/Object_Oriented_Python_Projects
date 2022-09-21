from operator import index
from turtle import heading
import check_input
import rectangle

def display_grid(grid):
  
  """ printing grid """
  for row in grid:
    for item in row:
      print(item, end=' ') 
    print()
  
  
  

def reset_grid(grid):

  reset = []
  
  """ creating again a grid with dots """
  for i in range(20):
    list = []
    for j in range(20):
      list.append('.')
    reset.append(list)
  
  return reset
   
      

def place_rect(grid,rect):

  x_location = rect.x 
  y_location = rect.y 

  rect_width= rect.width
  rect_height = rect.height
  
  for i in range(rect_height):
    for j in range(rect_width):
      grid[x_location + i][y_location + j] = "*"


  
  
  
          
          

  
  return grid

      
    
        







          
       

def main():
  """ if salir is false then it means the user quit the game  """
  salir = True 

  """ Display and Check user inputs """

  rectangle_height = check_input.get_positive_int("Enter rectangle height (1-5): ")


  while rectangle_height > 5 :
    print("Invalid input – should be within range 1-5")


    
    rectangle_height = check_input.get_positive_int("Enter rectangle height (1-5): ")
  

  rectangle_width = check_input.get_positive_int("Enter rectangle width (1-5): ")

  while rectangle_width > 5:
    print("Invalid input – should be within range 1-5")
    rectangle_width = check_input.get_positive_int("Enter rectangle width (1-5): ")
  

  """ Create the Rectangle Objet """
  rectangulo = rectangle.Rectangle(rectangle_width,rectangle_height)

  """ Creating the grid with dots """
  list2d = []

  for i in range(20):
    list = []
    for j in range(20):
      list.append('.')
    list2d.append(list)
  
  """ storing the 2d list in the grid variable """
  grid = list2d


  while salir:
    new_grid = reset_grid(grid)
    rect_with_grid = place_rect(new_grid, rectangulo)
    
    display_grid(rect_with_grid)

    print(rectangulo.get_coords())

    """ user's directions """
    print(""" 
    Enter Direction:
    1. Up
    2. Down
    3. Left
    4. Right
    5. Quit
     """)

    direction = int(input())

    if direction == 1:
      rectangulo.move_up()
    
    elif direction == 2:
      """ If statements to prevent out of range error """
      if rectangulo.x != 19 and rectangle_height == 1:
        rectangulo.move_down()
      elif rectangulo.x != 18 and rectangle_height == 2:
        rectangulo.move_down()
      elif rectangulo.x != 17 and rectangle_height == 3:
        rectangulo.move_down()
      elif rectangulo.x != 16 and rectangle_height == 4:
        rectangulo.move_down()
      elif rectangulo.x != 15 and rectangle_height == 5:
        rectangulo.move_down()

    
    elif direction == 3:
      rectangulo.move_left()
    
    elif direction == 4:
      """ to prevent out of range error, we will restrict the rectangle to move beyond by hardcoding """
      """ I know that hard coding is not a good practice by the way! 😥 """
      if rectangulo.y != 15 and rectangle_width == 5:
        rectangulo.move_right()
      elif rectangulo.y != 16 and rectangle_width == 4:
        rectangulo.move_right()
      elif rectangulo.y != 17 and rectangle_width == 3:
        rectangulo.move_right()
      elif rectangulo.y != 18 and rectangle_width == 2:
        rectangulo.move_right()
      elif rectangulo.y != 19 and rectangle_width == 1:
        rectangulo.move_right()


    
    elif direction == 5:
      salir = False
      break

  



    
    


main()
