import pytest
from app.matrix import Matrix

def test_private_variable():
  matrix = Matrix(10)
  with pytest.raises(AttributeError):
    print(matrix.__matrix)