"""Lesson 3: inheritance and polymorphism.

Covers: abstract base classes, subclasses, ``super().__init__``, overriding
methods, and calling the same method on different types.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """A Shape can't be created directly; subclasses must implement ``area``."""

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self) -> str:
        # Shared behaviour that relies on methods the subclasses provide.
        return f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")  # run the parent's __init__ first
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Square(Rectangle):
    """A Square is a Rectangle with equal sides: it reuses all the maths."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.name = "Square"


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


def total_area(shapes: list[Shape]) -> float:
    """Polymorphism: works for any Shape without knowing its exact type."""
    return sum(shape.area() for shape in shapes)
