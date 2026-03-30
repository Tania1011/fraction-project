# Fraction Class – Learning OOP in Python

### This project is a simple Fraction class to practice Object-Oriented Programming (OOP) concepts in Python. Supports basic arithmetic and comparisons.


## Features
- Creating classes and objects
- Constructor (__init__) and attributes
- Methods for arithmetic operations: +, -, *, /
- Operator overloading
- Comparison operators: ==, !=, <, >
- Unary operators: -, abs()
- Simplifying fractions using gcd

## Notes
- Denominator cannot be zero
- Fractions are always simplified
- Designed to practice OOP concepts

## Example

```
f = Fraction(1, 2)
g = Fraction(3, 4)

print(f + g)       # 5/4
print(f * 2)       # 1/1
print(-f)          # -1/2
print(abs(Fraction(-3, 4)))  # 3/4

print(f < g)       # True
print(f == Fraction(2, 4))  # True
```
