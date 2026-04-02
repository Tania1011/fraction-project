# Fraction Class – Learning OOP in Python

This project is a simple Fraction class to practice Object-Oriented Programming (OOP) concepts in Python. Supports basic arithmetic operations using operator overloading.

---

## Features

- Creating classes and objects
- Constructor `(__init__)` and attributes
- Methods for arithmetic operations: `+`, `-`, `*`, `/`
- Operator overloading
- Comparison operators: `==`, `!=`, `<`, `>`
- Unary operators: `-`, `abs()`
- Simplifying fractions using `GCD`

---

## Notes

- Denominator cannot be zero
- Fractions are always simplified
- Designed to practice OOP concepts

## Example

```
f = Fraction(2, 3) # 1/2

print(f + 1)     # 3/2
print(f * 2)     # 1/1
print(f - 1)     # -1/2
print(f / 2)     # 1/4

print(f < 1)     # True
print(f == Fraction(2, 4))  # True
print(f > 1)     # False
```
