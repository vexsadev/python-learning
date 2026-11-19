"""Lesson 1: the basics of a class.

Covers: defining a class, ``__init__``, instance attributes, class attributes,
methods, and ``__repr__`` / ``__str__``.
"""


class Dog:
    # A class attribute is shared by every Dog.
    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        # Instance attributes belong to one particular dog.
        self.name = name
        self.age = age
        self.tricks: list[str] = []

    def bark(self) -> str:
        """A method is a function that receives the instance as ``self``."""
        return f"{self.name} says woof!"

    def learn(self, trick: str) -> None:
        """Methods can change the instance's state."""
        self.tricks.append(trick)

    def birthday(self) -> int:
        self.age += 1
        return self.age

    def __repr__(self) -> str:
        # Unambiguous form for developers, shown in the REPL and debugger.
        return f"Dog(name={self.name!r}, age={self.age!r})"

    def __str__(self) -> str:
        # Friendly form, used by print() and f-strings.
        return f"{self.name} ({self.age} years old)"
