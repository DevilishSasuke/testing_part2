import unittest
from mat.matrix import Matrix
from mat.matrixoperators import MatrixOperators

class TestMatrixIntegration(unittest.TestCase):
  def test_many_functions_in_row(self):
    mat1 = Matrix.create([[1, 2], [3, 4]])
    mat2 = Matrix.create([[5, 6], [7, 8]])

    Matrix.set_defaul_value(9)
    mat1.resize(3, 3)
    mat2.resize(3, 3)

    new_matrix = MatrixOperators.add_matrices(mat1, mat2)
    determ = MatrixOperators.determinant(new_matrix)
    expected = [[6, 8, 18], [10, 12, 18], [18, 18, 18]]

    self.assertEqual(expected, new_matrix.get_matrix)
    self.assertEqual(determ, -144)

    new_matrix = MatrixOperators.power_elements(
      Matrix.create(new_matrix.transpose), 3)
    determ = MatrixOperators.determinant(new_matrix)
    expected = [[216, 1000, 5832], [512, 1728, 5832], [5832, 5832, 5832]]

    self.assertEqual(expected, new_matrix.get_matrix)
    self.assertEqual(determ, -15502482432)

    Matrix.set_seed(1001)

    new_matrix = Matrix.create(
      Matrix.create(new_matrix.transpose).\
        resize(new_matrix.rows + 1, new_matrix.cols + 1, 
               min_value=new_matrix.rows * 5, max_value=new_matrix.rows * 8, 
               randomize_new_elements=True))
    
    expected = [[216, 512, 5832, 15.821], 
                [1000, 1728, 5832, 23.122], 
                [5832, 5832, 5832, 22.073], 
                [22.17, 15.528, 21.842, 22.764]]
    
    self.assertEqual(expected, new_matrix.get_matrix)

    twiced_matrix = MatrixOperators.add_matrices(new_matrix, new_matrix).get_matrix
    new_matrix = new_matrix.get_matrix
    for i in range(len(new_matrix)):
      for j in range(len(new_matrix[i])):
        self.assertAlmostEqual(twiced_matrix[i][j], new_matrix[i][j] * 2)

    Matrix.reset_default_value()
