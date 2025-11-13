class Fraction:
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be 0")
        self.__numerator = n
        self.__denominator = d

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def to_float(self, n_digits=2):
        return round(self.__numerator / self.__denominator, n_digits)

        