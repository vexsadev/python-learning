# classes

Learning Python classes, one concept per module. Read the lessons in order;
each one has a matching test file showing how the class behaves.

| # | Module | Concepts |
| --- | --- | --- |
| 1 | [`dog.py`](src/learning_classes/dog.py) | `__init__`, instance vs class attributes, methods, `__repr__` / `__str__` |
| 2 | [`bank_account.py`](src/learning_classes/bank_account.py) | Encapsulation, `@property`, `@classmethod`, `@staticmethod`, custom exceptions |
| 3 | [`shapes.py`](src/learning_classes/shapes.py) | Inheritance, abstract base classes, `super()`, polymorphism |
| 4 | [`vector.py`](src/learning_classes/vector.py) | `@dataclass`, `frozen=True`, operator overloading |

## Structure

```
classes/
├── pyproject.toml
├── README.md
├── src/
│   └── learning_classes/
│       ├── __init__.py
│       ├── __main__.py       # Enables `python -m learning_classes`
│       ├── main.py           # Runs a tour of every lesson
│       ├── dog.py
│       ├── bank_account.py
│       ├── shapes.py
│       └── vector.py
└── tests/
    ├── test_dog.py
    ├── test_bank_account.py
    ├── test_shapes.py
    └── test_vector.py
```

## Setup

```bash
cd classes
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
classes-demo                 # via console script
python -m learning_classes   # via module
```

## Test

```bash
pytest
```

## Try it yourself

- Give `Dog` a `__eq__` so two dogs with the same name and age compare equal.
- Add a `Triangle(Shape)` and check that `total_area` works with it unchanged.
- Add a `transfer(to, amount)` method to `BankAccount`.
- Rewrite `Dog` as a `@dataclass` and see how much code disappears.
