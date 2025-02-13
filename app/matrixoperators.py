from matrix import Matrix

class MatrixOperators:

  def diag(matrix: Matrix) -> float:
    '''
      returns sum of diagonal matrix elements
    '''
    mat = matrix.get_matrix
    
    return sum([mat[i][i] for i in range(min(matrix.rows, matrix.cols))])

  def determinant(matrix: Matrix) -> float:
    '''
      returns determinant ONLY for 2x2 or 3x3 matrices
    '''
    if not matrix.is_square:
      raise(ValueError, "matrix must be square.")
    
    mat = matrix.get_matrix
    if matrix.rows == 1:
      return matrix.get_matrix[0][0]
    elif matrix.rows == 2:
      return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    elif matrix.rows == 3:
      return (mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) - 
              mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) + 
              mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))

    raise(NotImplementedError, "supports only 2x2 or 3x3 matrices")
  
  def power_elements(matrix: Matrix, power: float) -> Matrix:
    '''
      power all elements in matrix

      return powered matrix instance
    '''
    mat = matrix.get_matrix
    powered_matrix = Matrix.create([[el ** power for el in row] for row in mat])
    return powered_matrix

  def add_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    '''
      adds matrix 1 to matrix 2

      returns new instance with sum of matrix
    '''
    if matrix1.rows != matrix2.rows or matrix1.cols != matrix2.cols:
      raise ValueError("matrixes shapes must be the same")
    
    mat1 = matrix1.get_matrix
    mat2 = matrix2.get_matrix
    
    result_matrix = Matrix.create([
      # add every element
      [mat1[i][j] + mat2[i][j] for j in range(matrix1.cols)]
      for i in range(matrix1.rows)
    ])

    return result_matrix