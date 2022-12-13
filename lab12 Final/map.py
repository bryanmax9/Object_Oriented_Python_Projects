class Map:
  _instance = None 
  _initialized = False
  def __new__(cls, *args):
      '''Since we only want to initialize the map once this method is resposible for
      a one time creation of the map
      cls._instance: This ensures that only one creation of this class is made as required'''
      if cls._instance is None:
         cls._instance = super().__new__(cls)
      return cls._instance
  def __init__(self):
      if not Map._initialized:
          self.load_map(1)
          Map._initialized = True
  def __getitem__ (self,row):
      '''This is a getter method that will return the location that was requested'''
      return self._map[row]
  def __len__(self):
        '''This is the method that will give us the length of our map when we request for it'''
        n_rows = 0
        for i in self._map:
            n_rows += 1
        return n_rows
  def show_map (self,loc):
    """This is how the map will show at the end of all the calculations"""
    string_showmap = ""
    for row_indx in range(len(self._revealed)):
        for column_indx in range(len(self._revealed)):
            if self._revealed[row_indx][column_indx] == False:
                if row_indx == loc[0] and column_indx == loc[1]:
                    string_showmap += "*"
                else:
                    string_showmap += "x"
            else:
                if row_indx == loc[0] and column_indx == loc[1]:
                    string_showmap += "*"
                else:
                    string_showmap += ""+str(self._map[row_indx][column_indx])+ ""
        string_showmap += "\n"
    return string_showmap
  def reveal (self,loc):
      '''This is the method resposible for revealing the map at the location of where the'''
      self._revealed[loc[0]][loc[1]] = True
  def remove_at_loc(self,loc):
      '''This is the method resposible for removing any monsters on the map once the hero
        defeats it'''
      self._map[loc[0]][loc[1]] = "n"
  def load_map (self, map_num):
    '''This is the number for the map we are to load for the game. Maps are listed
    from one to three'''
    file = open ("map"+str(map_num)+".txt")
    row_map = file.readlines()
    self._map = []
    for row in row_map:
        list = []
        for column in row:
            if column != "\n":
                list.append(column)
        self._map.append(list)
        self._revealed = []
    for row in row_map:
        list = []
        for column in row:
            if column != "\n":
                list.append(False)
        self._revealed.append(list)
