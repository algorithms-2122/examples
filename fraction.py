class Fraction:
    def __init__(self, nominator, denominator):
        self.__nominator = nominator
        self.__denominator = denominator

    def __eq__(self, o):
        return (isinstance(o, Fraction) and self.__nominator == o.__nominator and self.__denominator == o.__denominator)

    def multiply(self, other):
        return Fraction(self.__nominator * other.__nominator, self.__denominator * other.__denominator)
