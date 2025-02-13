import random
from typing import Optional
from accessify import private, protected

class Matrix:
  _defaultValue = 1 # default value that is used when filling matrix with values

  def __init__(self, rows: int, columns: int):
    '''
      class constructor based on matrix shape

      args:
        rows - number of rows in creating matrix
        columns - number of columns in creating matrix
    '''

    if rows < 1 or columns < 1:
      raise ValueError("rows and columns must be positive numbers")

    self.__rows = rows
    self.__cols = columns
    self.__matrix = [[Matrix._defaultValue for _ in range(columns)] for _ in range(rows)]

  @classmethod
  def create(cls, matrix: list[list[float]]):
    '''
      alternative way to initialize matrix object

      based on already existing 2d array

      returns created instance of matrix class

      args:
        matrix - existing 2d array 
    '''

    instance = cls(1, 1) # create class instance
    instance.set_matrix(matrix) # update matrix variable

    return instance

  def fill_with_random(self, 
                       min_value: Optional[float] = 0, 
                       max_value: Optional[float] = 1000,
                       fill_with_float: Optional[bool] = True) -> list[list[float]]:
    '''
      fills matrix with random float values

      returns filled matrix data

      args:
        min value - min bound of randomizer range
        max value - max bound of randomizer range
        fill_with_float: bool - if True - will fill with float values
          otherwise will fill with in values 
    '''

    if max_value < min_value:
      raise ValueError("max value is less than min value")

    rnd_range = max_value - min_value # get range to randomize numbers in

    def new_value():
      '''
        define what type new elements will be initialized with
      '''
      return round(min_value + random.random() * rnd_range, 3) \
        if fill_with_float \
        else random.randint(int(min_value), int(max_value))


    # fill all matrix with new values
    self.__matrix = [[new_value()
                    for _ in range(self.__cols)] 
                    for _ in range(self.__rows)]
    
    return self.__matrix


  def resize(self, rows: int, columns: int, 
                       min_value: Optional[float] = 0, 
                       max_value: Optional[float] = 1000,
                       randomize_new_elements: Optional[bool] = False) -> list[list[float]]:
    '''
      resize matrix and init added elements

      returns resized matrix data
      
      args:
        rows - number of rows of resized matrix
        columns - number of columns of resized matrix

        min value - min bound of randomizer range
        max value - max bound of randomizer range

        randomize_new_elements: bool - if True - will fill added elements with float values
          otherwise will fill with defaultValue (by default = 1)
    '''

    if rows < 1 or columns < 1:
      raise ValueError("rows and columns must be positive numbers")
    if max_value < min_value:
      raise ValueError("max value is less than min value")

    # no need to change anything
    if rows == self.__rows and self.__cols == columns:
      return

    cols_diff = columns - self.__cols # difference - negative means that it needs to be removed
    rows_diff = rows - self.__rows # positive means that it needs to be added
    rnd_range = max_value - min_value

    def new_element():
      '''
        define if matrix will be extend with random numbers or with default value
      '''
      return round(min_value + random.random() * rnd_range, 3) \
              if randomize_new_elements else Matrix._defaultValue

    # change rows
    if rows < self.__rows:
      # just trim the data
      self.__matrix = self.__matrix[:rows]
    elif rows > self.__rows:
      # add new rows until correct amount with correcr amount of columns
      self.__matrix.extend([[new_element() 
                          for _ in range(self.__cols + cols_diff)] 
                          for _ in range(rows_diff)])

    # change columns
    for i in range(min(self.__rows, rows)):
      if columns < self.__cols:
        # trim the row
        self.__matrix[i] = self.__matrix[i][:columns]
      elif columns > self.__cols:
        # extend unupdated rows with elements
        self.__matrix[i].extend([new_element() for _ in range(cols_diff)])

    # update shape vars
    self.__rows = rows
    self.__cols = columns

    return self.__matrix

  @property
  def transpose(self) -> list[list[float]]:
    '''
      transpose matrix (change rows to columns and columns to rows)

      returns transposet matrix data
    '''
    self.__matrix = [[self.__matrix[j][i] for j in range(self.__rows)] for i in range(self.__cols)]
    self.__rows, self.__cols = self.__cols, self.__rows

    return self.__matrix

  def set_seed(seed: int) -> None:
    '''
      set seed in randomizer
    '''
    random.seed(seed)

  @classmethod
  def set_defaul_value(cls, value: int) -> None:
    '''
      set new default value that uses to initialize new elements
    '''
    cls._defaultValue = value

  @classmethod
  def reset_default_value(cls) -> None:
    cls._defaultValue = 1

  @protected
  def set_matrix(self, new_matrix: list[list[float]]):
    '''
      set new matrix as matrix data instance
      updates rows and columns counters in class
    '''
    rows = len(new_matrix)
    if rows > 0:
      columns = len(new_matrix[0])
    else: 
      raise ValueError("matrix is empty")
    
    for row in new_matrix:
      if len(row) != columns:
        raise ValueError("all rows in matrix must contain the same element number")
      
    self.resize(rows, columns)
    for i in range(rows):
      self.__matrix[i] = new_matrix[i].copy()
    self.__rows = rows
    self.__cols = columns

  @property
  def get_matrix(self) -> list[list[float]]:
    return self.__matrix

  @property
  def is_square(self) -> bool:
    return self.__rows == self.__cols
  
  @property
  def rows(self) -> int:
    return self.__rows
  
  @property
  def cols(self) -> int:
    return self.__cols

  def __str__(self):
    return '\n'.join([' '.join(map(str, row)) for row in self.__matrix])

  def __repr__(self):
    return str(self.__matrix)
  
  @private
  def private_test_method(self) -> bool:
      return True
