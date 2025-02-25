# Table of Contents

* [mat.matrix](#mat.matrix)
  * [Matrix](#mat.matrix.Matrix)
    * [\_\_init\_\_](#mat.matrix.Matrix.__init__)
    * [create](#mat.matrix.Matrix.create)
    * [fill\_with\_random](#mat.matrix.Matrix.fill_with_random)
    * [resize](#mat.matrix.Matrix.resize)
    * [transpose](#mat.matrix.Matrix.transpose)
    * [set\_seed](#mat.matrix.Matrix.set_seed)
    * [set\_defaul\_value](#mat.matrix.Matrix.set_defaul_value)
    * [set\_matrix](#mat.matrix.Matrix.set_matrix)
    * [get\_matrix](#mat.matrix.Matrix.get_matrix)
    * [is\_square](#mat.matrix.Matrix.is_square)
    * [rows](#mat.matrix.Matrix.rows)
    * [cols](#mat.matrix.Matrix.cols)
    * [private\_test\_method](#mat.matrix.Matrix.private_test_method)
* [mat.matrixoperators](#mat.matrixoperators)
  * [MatrixOperators](#mat.matrixoperators.MatrixOperators)
    * [diag](#mat.matrixoperators.MatrixOperators.diag)
    * [determinant](#mat.matrixoperators.MatrixOperators.determinant)
    * [power\_elements](#mat.matrixoperators.MatrixOperators.power_elements)
    * [add\_matrices](#mat.matrixoperators.MatrixOperators.add_matrices)

<a id="mat.matrix"></a>

# mat.matrix

<a id="mat.matrix.Matrix"></a>

## Matrix Objects

```python
class Matrix()
```

class of matrix representation and matrix base operations

<a id="mat.matrix.Matrix.__init__"></a>

#### \_\_init\_\_

```python
def __init__(rows: int, columns: int)
```

class constructor based on matrix shape

**Arguments**:

- `rows` _int_ - number of rows in creating matrix
- `columns` _int_ - number of columns in creating matrix
  

**Returns**:

  None
  

**Raises**:

- `ValueError` - if rows or columns are less than 1

<a id="mat.matrix.Matrix.create"></a>

#### create

```python
@classmethod
def create(cls, matrix: list[list[float]]) -> "Matrix"
```

alternative way to initialize matrix object

based on already existing 2d array


args:
matrix (list[list[float]]): existing 2d array

**Returns**:

- `Matrix` - created instance of matrix class

<a id="mat.matrix.Matrix.fill_with_random"></a>

#### fill\_with\_random

```python
def fill_with_random(
        min_value: Optional[float] = 0,
        max_value: Optional[float] = 1000,
        fill_with_float: Optional[bool] = True) -> list[list[float]]
```

fills matrix with random float values

returns filled matrix data



**Arguments**:

  min value (float, optional): min bound of randomizer range
  max value (float, optional): max bound of randomizer range
- `fill_with_float` _bool_ - if True - will fill with float values
  otherwise will fill with in values
  

**Returns**:

- `list[list[float]]` - matrix data with filled values
  

**Raises**:

- `ValueError` - if min value is less than max

<a id="mat.matrix.Matrix.resize"></a>

#### resize

```python
def resize(
        rows: int,
        columns: int,
        min_value: Optional[float] = 0,
        max_value: Optional[float] = 1000,
        randomize_new_elements: Optional[bool] = False) -> list[list[float]]
```

resize matrix and init added elements

**Arguments**:

- `rows` _int_ - number of rows of resized matrix
- `columns` _int_ - number of columns of resized matrix
  
  min value (float, optional): min bound of randomizer range
  max value (float, optional): max bound of randomizer range
  
- `randomize_new_elements` _bool_ - if True - will fill added elements with float values
  otherwise will fill with defaultValue (by default = 1)
  

**Returns**:

- `list[list[float]]` - resized matrix data
  

**Raises**:

- `ValueError` - if rows or columns less than 1
- `ValueError` - if min value < max value in range

<a id="mat.matrix.Matrix.transpose"></a>

#### transpose

```python
@property
def transpose() -> list[list[float]]
```

transpose matrix (change rows to columns and columns to rows)

**Returns**:

- `list[list[float]]` - transposet matrix data

<a id="mat.matrix.Matrix.set_seed"></a>

#### set\_seed

```python
@staticmethod
def set_seed(seed: int) -> None
```

set seed in randomizer

**Arguments**:

- `seed` _int_ - new seed to set in generator ("random" lib)
  

**Returns**:

  None

<a id="mat.matrix.Matrix.set_defaul_value"></a>

#### set\_defaul\_value

```python
@classmethod
def set_defaul_value(cls, value: int) -> None
```

set new default value that uses to initialize new elements

**Arguments**:

- `value` _int_ - new value to change defaultValue on
  

**Returns**:

  None

<a id="mat.matrix.Matrix.set_matrix"></a>

#### set\_matrix

```python
@protected
def set_matrix(new_matrix: list[list[float]]) -> None
```

set new matrix as matrix data instance
updates rows and columns counters in class
copying all rows from new_matrix!!

**Arguments**:

- `new_matrix` _list[list[float]]_ - matrix that supposed to replace current matrix
  

**Returns**:

  None
  

**Raises**:

- `ValueError` - if rows < 1
- `ValueError` - if any of rows element number is different from others

<a id="mat.matrix.Matrix.get_matrix"></a>

#### get\_matrix

```python
@property
def get_matrix() -> list[list[float]]
```

**Returns**:

- `list[list[float]]` - actual matrix data

<a id="mat.matrix.Matrix.is_square"></a>

#### is\_square

```python
@property
def is_square() -> bool
```

checks if matrix is square shape


**Returns**:

- `bool` - True - if rows == columns, false otherwise

<a id="mat.matrix.Matrix.rows"></a>

#### rows

```python
@property
def rows() -> int
```

getter for __rows var

**Returns**:

- `int` - number of rows in matrix

<a id="mat.matrix.Matrix.cols"></a>

#### cols

```python
@property
def cols() -> int
```

getter for __cols var

**Returns**:

- `int` - number of columns in matrix

<a id="mat.matrix.Matrix.private_test_method"></a>

#### private\_test\_method

```python
@private
def private_test_method() -> bool
```

just method to test encapsulation in tests

**Returns**:

- `bool` - constantly returns True

<a id="mat.matrixoperators"></a>

# mat.matrixoperators

<a id="mat.matrixoperators.MatrixOperators"></a>

## MatrixOperators Objects

```python
class MatrixOperators()
```

<a id="mat.matrixoperators.MatrixOperators.diag"></a>

#### diag

```python
@staticmethod
def diag(matrix: Matrix) -> float
```

calculate sum of diagonal elements in matrix

if matrix shape is not squared - then
goes by min diagonal of rows and columns

**Arguments**:

- `matrix` _Matrix_ - matrix object to calculate on
  

**Returns**:

- `float` - sum of diagonal matrix elements

<a id="mat.matrixoperators.MatrixOperators.determinant"></a>

#### determinant

```python
@staticmethod
def determinant(matrix: Matrix) -> float
```

calculate the determinant for square matrices which size is not greater than 3x3

**Arguments**:

- `matrix` _Matrix_ - matrix object to calculate on
  

**Returns**:

- `float` - calculated determinant of matrix
  

**Raises**:

- `ValueError` - if matrix is not square
- `NotImplementedError` - if matrix size is greater than 3x3

<a id="mat.matrixoperators.MatrixOperators.power_elements"></a>

#### power\_elements

```python
@staticmethod
def power_elements(matrix: Matrix, power: float) -> Matrix
```

power all elements in matrix

**Arguments**:

- `matrix` _Matrix_ - matrix object to calculate on
- `power` _float_ - power to which matrix should be raised
  

**Returns**:

- `Matrix` - powered matrix instance

<a id="mat.matrixoperators.MatrixOperators.add_matrices"></a>

#### add\_matrices

```python
@staticmethod
def add_matrices(matrix1: Matrix, matrix2: Matrix) -> Matrix
```

adds matrix 1 to matrix 2

**Arguments**:

- `matrix1` _Matrix_ - first matrix that will be added to second
- `matrix2` _Matrix_ - second matrix that will be added to first
  

**Returns**:

- `Matrix` - new instance with sum of matrix
  

**Raises**:

- `ValueError` - if matrices are not the same shape

