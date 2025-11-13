from demo_functions import add, divide, sum

def test_add_01():
    a = 5
    b = 3
    expected = 8
    actual = add(a, b)
    assert actual == expected

def test_add_02():
    a = 5
    b = 0
    expected = 5
    actual = add(a, b)
    assert actual == expected

def test_divide_01():
    a = 5
    b = 1
    expected = 5
    actual = divide(a, b)
    assert actual == expected

def test_divide_02():
    a = 10
    b = 2
    expected = 5
    actual = divide(a, b)
    assert actual == expected

def test_divide_03():
    a = 0
    b = 10
    expected = 0
    actual = divide(a, b)
    assert actual == expected

def test_divide_04():
    try:
        a = 10
        b = 0
        c = divide(a, b)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == "Không chia được cho 0"

def test_sum_01():
    n = 5
    expected = 15
    actual = sum(n)
    assert actual == expected

def test_sum_02():
    n = 10
    expected = 55
    actual = sum(n)
    assert actual == expected

def test_sum_03():
    n = 0
    expected = 0
    actual = sum(n)
    assert actual == expected

def test_sum_04():
    n = 1
    expected = 1
    actual = sum(n)
    assert actual == expected

def test_sum_05():
    try:
        n = -5
        actual = sum(n)
        assert False
    except ValueError as e:
        assert str(e) == "n must >= 0"