import random
from typing import Optional

class Matrix:
  _defaultValue = 1

  def __init__(self, rows: int, columns: int):
    self.rows = rows
    self.cols = columns
    self.__matrix = [[Matrix._defaultValue for _ in range(columns)] for _ in range(rows)]

  @classmethod
  def create(cls, matrix: list[list[float]]):
    instance = cls(1, 1)
    instance.set_matrix(matrix)

    return instance

  def fill_with_random(self, 
                       min_value: Optional[float] = 0, 
                       max_value: Optional[float] = 1000) -> list[list[float]]:
    rnd_range = max_value - min_value
    self.__matrix = [[round(min_value + random.random() * rnd_range, 3)
                    for _ in range(self.cols)] 
                    for _ in range(self.rows)]
    
    return self.__matrix

  def resize(self, rows: int, columns: int, 
                       min_value: Optional[float] = 0, 
                       max_value: Optional[float] = 1000,
                       randomize_new_elements: Optional[bool] = False) -> list[list[float]]:
    if rows == self.rows and self.cols == columns:
      return

    cols_diff = columns - self.cols
    rows_diff = rows - self.rows
    rnd_range = max_value - min_value

    def new_element():
      return round(min_value + random.random() * rnd_range, 3) if randomize_new_elements else Matrix._defaultValue

    if rows < self.rows:
      self.__matrix = self.__matrix[:rows]
    elif rows > self.rows:
      self.__matrix.extend([[new_element() 
                          for _ in range(self.cols + cols_diff)] 
                          for _ in range(rows_diff)])

    for i in range(min(self.rows, rows)):
      if columns < self.cols:
        self.__matrix[i] = self.__matrix[i][:columns]
      elif columns > self.cols:
        self.__matrix[i].extend([new_element() for _ in range(cols_diff)])

    self.rows = rows
    self.cols = columns

    return self.__matrix

  @property
  def transpose(self) -> list[list[float]]:
    self.__matrix = [[self.__matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
    self.rows, self.cols = self.cols, self.rows

    return self.__matrix

  def set_seed(seed: int) -> None:
    random.seed(seed)

  @classmethod
  def set_defaul_value(cls, value: int) -> None:
    cls._defaultValue = value

  def set_matrix(self, new_matrix: list[list[float]]):

    rows = len(new_matrix)
    if rows > 0:
      columns = len(new_matrix[0])
    else: 
      raise ValueError("matrix is empty")
    
    for row in new_matrix:
      if len(row) != columns:
        raise ValueError("all rows in matrix must contain the same element number")
      
    self.__matrix = new_matrix
    self.rows = rows
    self.cols = columns

  @property
  def get_matrix(self) -> list[list[float]]:
    return self.__matrix

  @property
  def is_square(self) -> bool:
    return self.rows == self.cols

  def __str__(self):
    return '\n'.join([' '.join(map(str, row)) for row in self.__matrix])

  def __repr__(self):
    return self.__matrix

