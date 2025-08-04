import pytest
import source.my_functions as mf

def test_add():
    result = mf.add(1,4)
    assert result == 5

def test_divide():
    result = mf.divide(10,5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        mf.divide(10,0)

def test_add_strings():
    result = mf.add("i like ","burgers")
    assert result == "i like burgers"