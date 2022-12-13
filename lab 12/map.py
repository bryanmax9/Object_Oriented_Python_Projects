class Map:
  _instance = None
  _initialized = False

  def __new__(cls, *args):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self):
    if not Map._initialized:
      self.load_map(1)
      Map._initialized = True
    
    
    

  def __getitem__(self, row):
    return self._map[row]

  def __len__(self):
    """ counting number of rows and returning it """
    n_rows = 0
    for i in self._map:
      n_rows += 1
    
    return n_rows
  

  def load_map(self,map_num):
    self._map = []
    self._revealed = []
    """ Chosing the map depending if 1,2 or 3 """
    file = open("map"+str(map_num)+".txt")

    """ row map stores each line as an item of the list. Example: [smnmn,nnmni,mnmnn,minmm,nmnmf] """
    row_map = file.readlines()
    """ we create empty list to prepare creating the 2d list, here will be stored the 2d list """
    self._map = []
    """ creating the 2d list using nested loops(not froot loops, so dont confuse ) """
    for row in row_map:
      list =[]
      for column in row:
        if column != "\n":
          list.append(column)
      self._map.append(list)
    
    """ Now initializing _revealed """
    """ we use the row_map to guide us the dimensions of the map """
    for row in row_map:
      alist =[]
      for column in row:
        if column != "\n":
          alist.append(False)
      self._revealed.append(alist)
      

  def show_map(self, loc):
    string_showmap=""
    
    self.reveal(loc)
    
    for row_indx in range(len(self._revealed)):
      for column_indx in range(len(self._revealed[row_indx])):

        if self._revealed[row_indx][column_indx] == False:
          """ Check if that postion is the player if not then display 'x' """
          if row_indx == loc[0] and column_indx == loc[1]:
            string_showmap += " * "
          else:
            string_showmap += " x "
        

        
        else:
          """ Check if that postion is the player if not display the map letter"""
          if row_indx == loc[0] and column_indx == loc[1]:
            string_showmap += " * "
          else:
            string_showmap += " "+ str(self._map[row_indx][column_indx]) + " "
      
      string_showmap += "\n"

    return string_showmap

  def reveal(self,loc):
    """ We modify the reveal list by replacing with True in the location given """  
    self._revealed[loc[0]][loc[1]]= True 

  def remove_at_loc(self, loc):
    """ replace location with n """
    self._map[loc[0]][loc[1]] = "n"

  


    