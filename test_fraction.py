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

def test_fractionAsAString():
    half = Fraction(1,2)
    assert(str(half) == "1/2")

def test_reduction():
    half = Fraction(1,2)
    otherHalf = Fraction(2,4)
    assert(half == otherHalf)

def test_addFractions():
    half = Fraction(1,2)
    aThird = Fraction(1,3)
    result = half.add(aThird)
    assert(result == Fraction(5,6))

def test_divideFractions():
    half = Fraction(1,2)
    result = half.divide(half)
    assert(result == Fraction(1,1))
    assert(Fraction(3,2) == Fraction(1,2).divide(Fraction(1,3)))    