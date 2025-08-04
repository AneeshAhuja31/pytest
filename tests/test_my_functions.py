import pytest
import source.my_functions as mf
import time

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

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = mf.divide(10,5)
    assert result == 2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert mf.add(1,2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero_broken():
    mf.divide(4,0)