# # overload all operators 
# # Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# # Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)    
 
from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")

        self.numerator = numerator
        self.denominator = denominator
        self._normalize()
        self._simplify()

    def _normalize(self):
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def _simplify(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    def _to_fraction(self, value):
        if isinstance(value, int):
            return Fraction(value, 1)
        return value

    # ----------------------------
    # Representation
    # ----------------------------
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    # ----------------------------
    # Arithmetic
    # ----------------------------
    def __add__(self, other):
        other = self._to_fraction(other)
        return Fraction(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __sub__(self, other):
        other = self._to_fraction(other)
        return Fraction(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator
        )

    def __mul__(self, other):
        other = self._to_fraction(other)
        return Fraction(
            self.numerator * other.numerator,
            self.denominator * other.denominator
        )

    def __truediv__(self, other):
        other = self._to_fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    # ----------------------------
    # # Extra operators
    # # ----------------------------
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))

    # ----------------------------
    # Comparison (ALL)
    # ----------------------------
    def __eq__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        other = self._to_fraction(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __ne__(self, other):
        return not (self == other)
    


f = Fraction(1, 2)

print(f + 1)      # 3/2
print(f * 3)      # 3/2
print(-f)         # -1/2
print(Fraction(-3, 4))  # -3/4
print(abs(Fraction(-3, 4)))  # 3/4

print(f < 1)      # True
print(f >= 1)     # False
print(f > 1)      # False
print(f != 1)     # True

f = Fraction(2, 3)

print(f + 1)     # 3/2
print(f * 2)     # 1/1
print(f - 1)     # -1/2
print(f / 2)     # 1/4

print(f < 1)     # True
print(f == Fraction(2, 4))  # True
print(f > 1)     # False