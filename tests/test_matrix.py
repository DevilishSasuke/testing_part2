import unittest
from mat.matrix import Matrix
from accessify.access import InaccessibleDueToItsProtectionLevelException


class TestMatrixPositive(unittest.TestCase):
  def test_matrix_init(self):
    Matrix.reset_default_value()
    result = [[1, 1], [1, 1]]
    matrix = Matrix(2, 2).get_matrix
    self.assertEqual(result, matrix)

    default_value = -100
    Matrix.set_defaul_value(default_value)
    result = [[default_value], [default_value]]
    matrix = Matrix(2, 1).get_matrix
    self.assertEqual(result, matrix)
    Matrix.reset_default_value()

  def test_matrix_create(self):
    result = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix.create(result).get_matrix
    
    self.assertEqual(result, matrix)

  def test_create_square_matrix(self):
    values = [1, 2, 3]
    for value in values:
      matrix = Matrix(value, value)
      self.assertTrue(matrix.is_square)
      self.assertEqual(matrix.rows, value)
      self.assertEqual(matrix.cols, value)

  def test_fill_with_random(self):
    rows = 6
    cols = 17
    min_val = 10
    max_val = 14

    matrix = Matrix(rows, cols)

    def test_fill_with_type(self: TestMatrixPositive, val_type):
      matrix.fill_with_random(min_val, max_val, val_type == float)

      self.assertEqual(matrix.rows, rows)
      self.assertEqual(matrix.cols, cols)

      min_val_ = int(min_val) if val_type == int else min_val 
      max_val_ = int(max_val) if val_type == int else max_val 

      for row in matrix.get_matrix:
        for el in row:
          self.assertGreaterEqual(el, min_val_)
          self.assertLessEqual(el, max_val_)
          self.assertEqual(type(el), val_type)

    test_fill_with_type(self, float)
    min_val = 120.13
    max_val = 122.98
    test_fill_with_type(self, int)

  def test_resize(self):
    rows = 3
    cols = 5
    matrix = Matrix(rows, cols)
    
    def test_resize_matrix(self: TestMatrixPositive, new_rows, new_cols, randomize = False):
      matrix.resize(new_rows, new_cols, randomize_new_elements=randomize)
      self.assertEqual(new_rows, matrix.rows)
      self.assertEqual(new_cols, matrix.cols)

    test_resize_matrix(self, rows + 1, cols + 1, False)
    test_resize_matrix(self, rows - 1, cols - 1, True)
    test_resize_matrix(self, 1, 1, False)
    test_resize_matrix(self, 2, 2, True)
    self.assertEqual(type(matrix.get_matrix[matrix.rows-1][matrix.cols-1]), float)

  def test_resize_extend_matrix(self):
    rows = 3
    cols = 5
    matrix = Matrix(rows, cols)
    old_default_value = Matrix._default_value
    new_default_value = 2

    def test_resize_matrix(self: TestMatrixPositive, new_rows, new_cols, randomize = False):
      matrix.resize(new_rows, new_cols, randomize_new_elements=randomize)
      self.assertEqual(new_rows, matrix.rows)
      self.assertEqual(new_cols, matrix.cols)

    test_resize_matrix(self, rows + 1, cols + 1, False)
    self.assertEqual(matrix.get_matrix[rows][cols], old_default_value)

    Matrix.set_defaul_value(new_default_value)
    test_resize_matrix(self, rows + 2, cols + 2, False)
    self.assertEqual(matrix.get_matrix[matrix.rows - 2][matrix.cols - 2], old_default_value)
    self.assertEqual(matrix.get_matrix[matrix.rows - 1][matrix.cols - 1], new_default_value)

    Matrix.reset_default_value()

  def test_resize_dont_replace_content(self):
    start_matrix = [[1, 2, 3, 4, 5],  [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]] 
    cutted_matrix = [row[:3] for row in start_matrix[:-1]]
    rows = 3
    cols = 5
    matrix = Matrix.create(start_matrix)

    def test_resize_matrix(self: TestMatrixPositive, new_rows, new_cols, randomize = False):
      matrix.resize(new_rows, new_cols, randomize_new_elements=randomize)
      self.assertEqual(new_rows, matrix.rows)
      self.assertEqual(new_cols, matrix.cols)

    test_resize_matrix(self, rows + 5, cols + 4, False)
    test_resize_matrix(self, rows + 3, cols + 2, False)

    test_resize_matrix(self, rows, cols, False)
    self.assertEqual(matrix.get_matrix, start_matrix)

    test_resize_matrix(self, rows - 1, cols - 2, False)
    self.assertEqual(matrix.get_matrix, cutted_matrix)
    Matrix.reset_default_value()

  def test_transpose(self):
    values = [[1, 2, 3], [4, 5, 6]]
    result = [[1, 4], [2, 5], [3, 6]]

    matrix = Matrix.create(values)
    transposed = matrix.transpose

    self.assertEqual(transposed, result)

    values = [[1]]
    matrix = Matrix.create(values)
    transposed = matrix.transpose
    self.assertEqual(transposed, values)

class TestMatrixExceptions(unittest.TestCase):
  def test_wrong_matrix_shapes(self):

    Matrix(1, 1)
    with self.assertRaises(ValueError):
      Matrix(0, 0)
    with self.assertRaises(ValueError):
      Matrix(-100, -1)
    with self.assertRaises(ValueError):
      Matrix(0, 100)
    with self.assertRaises(ValueError):
      Matrix(100, -21312)

  def test_wrong_range_on_fill(self):
    with self.assertRaises(ValueError):
      Matrix(1, 1).fill_with_random(10, 9)

  def test_resize_validation(self):
    matrix = Matrix(10, 10)
    with self.assertRaises(ValueError):
      matrix.resize(0, 10)
    with self.assertRaises(ValueError):
      matrix.resize(1, 1, min_value=10, max_value=9)

  def test_empty_matrix_create(self):
    with self.assertRaises(ValueError):
      Matrix.create([])
    with self.assertRaises(ValueError):
      Matrix.create([[]])
    with self.assertRaises(ValueError):
      Matrix.create([[], [], []])

  def test_dif_row_lens(self):
    values = [[1, 2, 3], [4, 5], [6, 7, 8]]
    with self.assertRaises(ValueError):
      Matrix.create(values)

class TesTMatrixEncaps(unittest.TestCase):
  def test_private_variable(self):
    matrix = Matrix(1, 1)
    with self.assertRaises(AttributeError):
      print(matrix.__matrix)

    new_value = 120
    matrix.__rows = new_value
    self.assertNotEqual(matrix.rows, new_value)

  def test_protected_and_private_methods(self):
    matrix = Matrix(1, 1)
    with self.assertRaises(InaccessibleDueToItsProtectionLevelException):
      matrix.set_matrix([[1]])

    with self.assertRaises(InaccessibleDueToItsProtectionLevelException):
      matrix.private_test_method()