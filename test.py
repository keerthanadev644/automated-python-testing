from app import add, subtract, multiply, divide, is_even


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False
    except ValueError:
        assert True


def test_even_number():
    assert is_even(10) is True


def test_odd_number():
    assert is_even(7) is False