from matrix import Matrix
from matrixoperators import MatrixOperators

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = Matrix(3, 3)
print(matrix)
matrix.fill_with_random()
print(matrix)
matrix.transpose
print(matrix)
matrix.set_matrix(my_matrix)
print(matrix)

matrix = MatrixOperators.power_elements(matrix, 2)
print(matrix)

diag = MatrixOperators.diag(matrix)
print(diag)

det = MatrixOperators.determinant(matrix)
print(det)
