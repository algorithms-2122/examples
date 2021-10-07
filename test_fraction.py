from fraction import Fraction

def test_equality():
    half = Fraction(1,2)
    otherHalf = Fraction(1,2)
    assert(half == otherHalf)

def test_notEqual():
    half = Fraction(1,2)
    oneThird = Fraction(1,3)
    assert(half != oneThird)

def test_multiply():
    half = Fraction(1,2)
    otherHalf = Fraction(1,2)
    result = half.multiply(otherHalf)
    assert(result == Fraction(1,4))

def test_differentObjectsAreNotEqual():
    half = Fraction(1,2)
    assert(half != 1)