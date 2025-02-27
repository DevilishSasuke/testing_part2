from mat.matrix import Matrix

class MatrixOperators:
  @staticmethod
  def diag(matrix: Matrix) -> float:
    '''
      calculate sum of diagonal elements in matrix

      if matrix shape is not squared - then 
        goes by min diagonal of rows and columns

      Args:
        matrix (Matrix): matrix object to calculate on

      Returns:
        float: sum of diagonal matrix elements
    '''
    mat = matrix.get_matrix
    
    return sum([mat[i][i] for i in range(min(matrix.rows, matrix.cols))])

  @staticmethod
  def determinant(matrix: Matrix) -> float:
    '''
      calculate the determinant for square matrices which size is not greater than 3x3

      Args:
        matrix (Matrix): matrix object to calculate on

      Returns:
        float: calculated determinant of matrix

      Raises:
        ValueError: if matrix is not square
        NotImplementedError: if matrix size is greater than 3x3
    '''
    if not matrix.is_square:
      raise ValueError("matrix must be square")
    
    mat = matrix.get_matrix
    if matrix.rows == 1:
      return matrix.get_matrix[0][0]
    elif matrix.rows == 2:
      return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    elif matrix.rows == 3:
      return (mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]) - 
              mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0]) + 
              mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]))

    raise NotImplementedError("supports only 2x2 or 3x3 matrices")
  
  @staticmethod
  def power_elements(matrix: Matrix, power: float) -> Matrix:
    '''
      power all elements in matrix

      Args:
        matrix (Matrix): matrix object to calculate on
        power (float): power to which matrix should be raised

      Returns:
        Matrix: powered matrix instance
    '''
    mat = matrix.get_matrix
    powered_matrix = Matrix.create([[el ** power for el in row] for row in mat])
    return powered_matrix

  @staticmethod
  def add_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    '''
      adds matrix 1 to matrix 2

      Args:
        matrix1 (Matrix): first matrix that will be added to second
        matrix2 (Matrix): second matrix that will be added to first

      Returns:
        Matrix: new instance with sum of matrix
        
      Raises:
        ValueError: if matrices are not the same shape
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