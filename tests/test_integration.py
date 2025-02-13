import unittest
from mat.matrix import Matrix
from mat.matrixoperators import MatrixOperators

class TestMatrixIntegration(unittest.TestCase):
  def test_create_after_add_power_and_resize(self):
    matrix = Matrix.create([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    Matrix.set_defaul_value(12)

    new_matrix = MatrixOperators.add_matrices(
      MatrixOperators.power_elements(matrix, 3),
      matrix).resize(5, 5)

    expected = [[2, 10, 30, 12, 12], 
                [68, 130, 222, 12, 12], 
                [350, 520, 738, 12, 12], 
                [12, 12, 12, 12, 12], 
                [12, 12, 12, 12, 12]]

    self.assertEqual(new_matrix, expected)

    Matrix.reset_default_value()

  def test_wave_numbers_in_matrix(self):
    matrix = Matrix.create(MatrixOperators.power_elements((Matrix(3, 3)), 10).resize(2, 2))

    Matrix.set_defaul_value(2)
    matrix = Matrix.create(matrix.resize(matrix.rows + 2, matrix.cols + 2))

    Matrix.set_defaul_value(3)
    matrix = Matrix.create(matrix.resize(matrix.rows + 2, matrix.cols + 2))

    diag = MatrixOperators.diag(matrix)
    self.assertEqual(diag, 1 * 2 + 2 * 2 + 3 * 2)

    expected = [
      [1, 1, 2, 2, 3, 3],
      [1, 1, 2, 2, 3, 3],
      [2, 2, 2, 2, 3, 3],
      [2, 2, 2, 2, 3, 3],
      [3, 3, 3, 3, 3, 3],
      [3, 3, 3, 3, 3, 3]
    ]

    self.assertEqual(matrix.get_matrix, expected)

    Matrix.reset_default_value()


