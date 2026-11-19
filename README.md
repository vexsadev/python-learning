# Python Learning Projects

A basic Hello World Python project.

## Structure

```
python-learning/
├── pyproject.toml          # Project metadata & config
├── README.md
├── src/
│   └── hello_world/
│       ├── __init__.py
│       ├── __main__.py     # Enables `python -m hello_world`
│       └── main.py         # Application code
└── tests/
    └── test_main.py        # Tests (pytest)
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run

```bash
hello                   # via console script
python -m hello_world   # via module
```

## Test

```bash
pytest
```
