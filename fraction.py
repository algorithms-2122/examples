from gcd import gcd

class Fraction:
    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator

    def __eq__(self, o):
        if not isinstance(o, Fraction):
            return False
        reduced = self.__reduce()
        otherReduced = o.__reduce()
        return (reduced.__nominator == otherReduced.__nominator and reduced.__denominator == otherReduced.__denominator)
        

    def multiply(self, other):
        return Fraction(self.__nominator * other.__nominator, self.__denominator * other.__denominator)

    def __repr__(self):
        return str(self.__nominator) + "/" + str(self.__denominator)

    def __reduce(self):
        divider = gcd(self.__nominator, self.__denominator)
        return Fraction(self.__nominator / divider, self.__denominator /divider)

    def add(self, other):
        return Fraction(self.__nominator * other.__denominator + other.__nominator * self.__denominator, self.__denominator * other.__denominator).__reduce()

    def divide(self, other):
        return self.multiply(Fraction(other.__denominator, other.__nominator))