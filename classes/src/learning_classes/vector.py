"""Lesson 4: dataclasses and dunder (magic) methods.

Covers: ``@dataclass`` (auto ``__init__``, ``__repr__``, ``__eq__``),
``frozen=True`` for immutability, and operator overloading with
``__add__``, ``__mul__``, ``__abs__``.
"""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    # Makes ``3 * v`` work as well as ``v * 3``.
    __rmul__ = __mul__

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)
