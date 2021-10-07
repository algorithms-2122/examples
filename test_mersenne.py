from mersenne import isPrime, generatePotentialMP

def test_isPrime():
    assert(isPrime(7))
    assert(isPrime(2))
    assert(isPrime(4) == False)
    assert(isPrime(1) == False)
    assert(isPrime(11))
    assert(isPrime(0) == False)

def test_generatePotentialMP():
    assert(generatePotentialMP(2) == 3)
    assert(generatePotentialMP(1) == 1)
    assert(generatePotentialMP(0) == 0)