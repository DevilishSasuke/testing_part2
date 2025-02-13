from matrix import Matrix
from matrixoperators import MatrixOperators

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = Matrix.create(my_matrix)
print(matrix)

matrix = MatrixOperators.power_elements(matrix, 2)
print(matrix)

diag = MatrixOperators.diag(matrix)
print(diag)

det = MatrixOperators.determinant(matrix)
print(det)
