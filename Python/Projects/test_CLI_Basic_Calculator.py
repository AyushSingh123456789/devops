from CLI_Basic_Calculator import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)