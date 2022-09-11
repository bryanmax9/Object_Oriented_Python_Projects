#Group 12
#Ramon Alaysa, Bryan Tineo
#This program allows the user to enter a number of rows, columns, and mines in order to generate a 2d board of a minesweeper game
#This program only allows valid inputs and generates the right amount of mines and numbers surrounding each mine

import random
import check_input

def place_mines(board, mines):
  """ Find number of rows and columns """
  n_columns = 0
  for row in board:
    for item in row:
      n_columns += 1
  
  n_rows = len(board)
  """ We will divide the the number of items in all lists and divide it by the rows to get total columns """
  n_columns = int(n_columns / n_rows)

  """ Now that we have the number of rows and columns we create a random value of row and column for each bomb  """
  """ will save the number of bombs in a variable """
  n_mines = mines
  while int(n_mines) != 0:
    random_row = random.randint(1, n_rows - 1)
    random_column = random.randint(1, n_columns - 1)
    
    """ Check if there is already a bomb in that place """
    while board[random_row][random_column] == 'X':
      random_row = random.randint(1, n_rows - 1)
      random_column = random.randint(1, n_columns - 1)

    board[random_row][random_column] = 'X'

    n_mines -= 1

def count_mines(board):
  """ lista = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]] """
  lista_row = len(board) - 1
  last_row_num = len(board) - 1
  last_column_num = len(board[0]) - 1
  
  while lista_row >= 0:
    lista_columnas = len(board[0]) - 1

    """ print(lista_row, board[lista_row]) """

    while lista_columnas >= 0:
      """ print( f'current item: {board[lista_row][lista_columnas]} left: {board[lista_row][lista_columnas - 1]}') """

      """ if the item is a bomb sum sorrounding it, but X is not in the left or right corner either bottom or top. also, avoid if X is in top or bottom"""
      if board[lista_row][lista_columnas] == "X" and lista_row != 0 and lista_row != last_row_num and lista_columnas != 0 and lista_columnas != last_column_num :
        """ the current item is a bomb so we add 1 to each side """

        """ add 1 to the left """
        if board[lista_row][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1
        
        """ add 1 to right """
        if board[lista_row][lista_columnas + 1] != "X":
          board[lista_row][lista_columnas + 1] += 1
        
        """ add 1 to the top """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add 1 to the top left """
        if board[lista_row - 1][lista_columnas - 1] != "X":
          board[lista_row - 1][lista_columnas -1] += 1
        
        """ add 1 to the top right """
        if board[lista_row - 1][lista_columnas + 1] != "X":
          board[lista_row - 1][lista_columnas + 1] += 1

        """ add 1 to the bottom  """
        if board[lista_row + 1][lista_columnas] != "X":
          board[lista_row + 1][lista_columnas] += 1
        
        """ add 1 to the bottom left """
        if board[lista_row + 1][lista_columnas - 1] != "X":
          board[lista_row + 1][lista_columnas -1] += 1
        
        """ add 1 to the bottom right """
        if board[lista_row + 1][lista_columnas + 1] != "X":
          board[lista_row + 1][lista_columnas + 1] += 1
      

      """ If the X is in the bottom right corner  """
      if board[lista_row][lista_columnas] == "X" and lista_row == last_row_num and lista_columnas == last_column_num:
        """ add to the top """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add to the top left """
        if board[lista_row - 1][lista_columnas - 1] != "X":
          board[lista_row - 1][lista_columnas - 1] += 1
        
        """ add to the left """
        if board[lista_row][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1
      
      """ If the X is in the bottom left corner  """
      if board[lista_row][lista_columnas] == "X" and lista_row == last_row_num and lista_columnas == 0:
        """ add to the right """
        if board[lista_row][lista_columnas + 1] != "X":
          board[lista_row][lista_columnas + 1] += 1
        
        """ add to the top  """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add to the top right """
        if board[lista_row - 1][lista_columnas + 1] != "X":
          board[lista_row - 1][lista_columnas + 1] += 1
      
      """ If the X is in the top left corner  """
      if board[lista_row][lista_columnas] == "X" and lista_row == 0 and lista_columnas == 0:
        """ add to the right """
        if board[lista_row][lista_columnas + 1] != "X":
           board[lista_row][lista_columnas + 1] += 1
        
        """ add to the bottom """
        if board[lista_row + 1][lista_columnas] != "X":
           board[lista_row + 1][lista_columnas] += 1

        """ add to the bottom right """
        if board[lista_row + 1][lista_columnas + 1] != "X":
           board[lista_row + 1][lista_columnas + 1] += 1
      
      """ If the X is in the top right corner  """
      if board[lista_row][lista_columnas] == "X" and lista_row == 0 and lista_columnas == last_column_num:
        """ add to the left """
        if board[lista_row][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1
        
        """ add to the bottom """
        if board[lista_row + 1][lista_columnas] != "X":
          board[lista_row + 1][lista_columnas] += 1
        
        """ add to the bottom left """
        if board[lista_row + 1][lista_columnas - 1] != "X":
          board[lista_row + 1][lista_columnas - 1] += 1
      
      
      



      """ If the X is all the way to the right but neither first row and last row """
      if board[lista_row][lista_columnas] == "X" and lista_columnas == last_column_num and lista_row != 0 and lista_row != last_row_num:
        """ add top """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add top left """
        if board[lista_row - 1][lista_columnas - 1] != "X":
          board[lista_row - 1][lista_columnas - 1] += 1

        """ add left """
        if board[lista_row][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1

        """ add bottom """
        if board[lista_row + 1][lista_columnas] != "X":
          board[lista_row + 1][lista_columnas] += 1
        
        """ add bottom left """
        if board[lista_row + 1][lista_columnas - 1] != "X":
          board[lista_row + 1][lista_columnas - 1] += 1
      
      """ If the X is all the way to the left but neither first row and last row """
      if board[lista_row][lista_columnas] == "X" and lista_columnas == 0 and lista_row != 0 and lista_row != last_row_num:
        """ add top """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add top right """
        if board[lista_row - 1][lista_columnas + 1] != "X":
          board[lista_row - 1][lista_columnas + 1] += 1
        
        """ add right """
        if board[lista_row][lista_columnas + 1] != "X":
          board[lista_row][lista_columnas + 1] += 1
        
        """ add to the bottom """
        if board[lista_row + 1][lista_columnas ] != "X":
          board[lista_row + 1][lista_columnas ] += 1
        
        """ add to the bottom right """
        if board[lista_row + 1][lista_columnas + 1] != "X":
          board[lista_row + 1][lista_columnas + 1] += 1
      
      """ If the X is in the bottom but is not the first and the last column """
      if board[lista_row][lista_columnas] == "X" and lista_row == last_row_num and lista_columnas != 0 and lista_columnas != last_column_num:
        """ add top """
        if board[lista_row - 1][lista_columnas] != "X":
          board[lista_row - 1][lista_columnas] += 1
        
        """ add top right """
        if board[lista_row - 1][lista_columnas + 1] != "X":
          board[lista_row - 1][lista_columnas + 1] += 1
        
        """ add top left """
        if board[lista_row - 1][lista_columnas - 1] != "X":
          board[lista_row - 1][lista_columnas - 1] += 1
        
        """ add left """
        if board[lista_row ][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1
        
        """ add right """
        if board[lista_row ][lista_columnas + 1] != "X":
          board[lista_row][lista_columnas + 1] += 1
      
      """ If the X is in the top but is not the first and the last column """
      if board[lista_row][lista_columnas] == "X" and lista_row == 0 and lista_columnas != 0 and lista_columnas != last_column_num:
        """ add left """
        if board[lista_row][lista_columnas - 1] != "X":
          board[lista_row][lista_columnas - 1] += 1
        
        """ add right """
        if board[lista_row][lista_columnas + 1] != "X":
          board[lista_row][lista_columnas + 1] += 1

        """ add bottom """
        if board[lista_row + 1][lista_columnas] != "X":
          board[lista_row + 1][lista_columnas] += 1
        
        """ add bottom left """
        if board[lista_row + 1][lista_columnas - 1] != "X":
          board[lista_row + 1][lista_columnas - 1] += 1
        
        """ add bottom right """
        if board[lista_row + 1][lista_columnas + 1] != "X":
          board[lista_row + 1][lista_columnas + 1] += 1

      lista_columnas -= 1
    
    lista_row -= 1
  

def display_board(board):
  print()
  """ displaying the grid with the bombs and numbers inside """
  for row in board:
    for item in row:
      print(item, end=' ')
    print()

def main():
  print("Minesweeper Maker 💣💥")
  
  #checks to see if the user inputs are valid and within range
  rows = check_input.get_positive_int("Enter number of rows (5-10): ")
  while type(rows) != type(1) or int(rows) > 10 or int(rows) < 5 :
    rows = check_input.get_positive_int("Please enter a valid number of rows (5-10): ")
  
  columns = check_input.get_positive_int("Enter number of columns (5-10): ")
  while type(columns) != type(1) or int(columns) > 10 or int(columns) < 5:
    columns = check_input.get_positive_int("Please enter a valid number of columns (5-10): ")
  
  n_mines = check_input.get_positive_int("Enter number of mines (5-10): ")
  while type(n_mines) != type(1) or int(n_mines) > 10 or int(n_mines) < 5:
    n_mines = check_input.get_positive_int("Please enter a valid number of mines (5-10): ")

  Board = []
  for i in range(rows):
    list = []
    for j in range(columns):
      list.append(int(0))
    Board.append(list)
  
  
  place_mines(Board, n_mines)
  count_mines(Board)
  display_board(Board)



main()