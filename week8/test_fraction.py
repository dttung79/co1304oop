from fraction import Fraction

def test_init_01():
    f = Fraction(2, 2)
    assert f.numerator == 2
    assert f.denominator == 2

def test_init_02():
    f = Fraction(2, 5)
    assert f.numerator == 2
    assert f.denominator == 5

def test_init_03():
    f = Fraction(-2, -3)
    assert f.numerator == -2
    assert f.denominator == -3

def test_str_01():
    f = Fraction(2, 2)
    assert str(f) == "2/2"

def test_str_02():
    f = Fraction(2, 5)
    assert str(f) == "2/5"

def test_str_03():
    f = Fraction(-2, -3)
    assert str(f) == "-2/-3"

def test_to_float_01():
    f = Fraction(1, 2)
    assert f.to_float() == 0.5

def test_to_float_02():
    f = Fraction(1, 3)
    assert f.to_float() == 0.33

def test_to_float_03():
    f = Fraction(4, 2)
    assert f.to_float() == 2.0