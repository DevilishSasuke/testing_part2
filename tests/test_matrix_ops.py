import unittest
from mat.matrix import Matrix
from mat.matrixoperators import MatrixOperators


class TestMatrixPositive(unittest.TestCase):
  def test_power_elements(self):
    values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    def get_powered(power):
      powered_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      for i in range(len(powered_values)):
        for j in range(len(powered_values[i])):
          powered_values[i][j] **= power

      return powered_values
    
    def check_for_powered_instances(power):
      powered_matrix = MatrixOperators.power_elements(matrix, power)
      powered_values = get_powered(power)
      self.assertEqual(powered_matrix.get_matrix, powered_values)

    matrix = Matrix.create(values)
    check_for_powered_instances(3)
    check_for_powered_instances(0)
    check_for_powered_instances(-1)

  def test_diag(self):
    values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    my_diag = values[0][0] + values[1][1] + values[2][2]

    matrix = Matrix.create(values)
    self.assertEqual(MatrixOperators.diag(matrix), my_diag)

    powered_matrix = MatrixOperators.power_elements(matrix, 2)
    my_diag = values[0][0] * values[0][0] + \
      values[1][1] * values[1][1] + \
      values[2][2] * values[2][2]

    self.assertEqual(MatrixOperators.diag(powered_matrix), my_diag)

  def test_determinant(self):
    values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_determ_result(matrix, value):
      det = MatrixOperators.determinant(matrix)
      self.assertEqual(det, value)

    matrix = Matrix.create(values)
    test_determ_result(matrix, 0)

    powered_matrix = MatrixOperators.power_elements(matrix, 2)
    test_determ_result(powered_matrix, -216)

    matrix = Matrix.create([row[:-1] for row in values[:-1]])
    test_determ_result(matrix, -3)

    matrix = Matrix.create([[values[0][0]]])
    test_determ_result(matrix, values[0][0])

  def test_add_matrices(self):
    val1 = [[1, 2], [3, 4]]
    val2 = [[5, 6], [7, 8]]
    new_val = [[6, 8], [10, 12]]

    matrix1 = Matrix.create(val1)
    matrix2 = Matrix.create(val2)

    new_matrix = MatrixOperators.add_matrices(matrix1, matrix2)
    self.assertEqual(new_matrix.rows, matrix1.rows)
    self.assertEqual(new_matrix.cols, matrix1.cols)
    self.assertEqual(new_matrix.get_matrix, new_val)

    new_matrix = Matrix.create(new_val)
    new_val = [[el * 2 for el in row] for row in new_val]
    new_matrix = MatrixOperators.add_matrices(new_matrix, new_matrix)
    self.assertEqual(new_matrix.get_matrix, new_val)


class TestMatrixExceptions(unittest.TestCase):
  def test_not_square_determ(self):
    with self.assertRaises(ValueError):
      MatrixOperators.determinant(Matrix(2, 3))
    with self.assertRaises(ValueError):
      MatrixOperators.determinant(Matrix(1, 2))
  
  def test_wrong_shape_determ(self):
    with self.assertRaises(NotImplementedError):
      MatrixOperators.determinant(Matrix(4, 4))

  def test_dif_shapes_on_add(self):
    with self.assertRaises(ValueError):
      MatrixOperators.add_matrices(Matrix(1, 2), Matrix(2, 1))

    with self.assertRaises(ValueError):
      MatrixOperators.add_matrices(Matrix(1, 2), Matrix(1, 1))
