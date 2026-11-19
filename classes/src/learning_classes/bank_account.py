"""Lesson 2: encapsulation.

Covers: "private" attributes by convention (``_balance``), read-only
``@property``, validation, ``@classmethod`` (alternative constructors),
``@staticmethod``, and custom exceptions.
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


class BankAccount:
    interest_rate = 0.02  # class attribute shared by all accounts

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.owner = owner
        # A leading underscore means "internal: don't touch from outside".
        self._balance = balance

    @property
    def balance(self) -> float:
        """Read-only: ``account.balance`` works, ``account.balance = 5`` does not."""
        return self._balance

    def deposit(self, amount: float) -> float:
        self._check_positive(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        self._check_positive(amount)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}; balance is {self._balance:.2f}"
            )
        self._balance -= amount
        return self._balance

    def add_interest(self) -> float:
        # Look up through the instance so a subclass can override the rate.
        self._balance += self._balance * self.interest_rate
        return self._balance

    @classmethod
    def from_string(cls, text: str) -> "BankAccount":
        """Alternative constructor: ``BankAccount.from_string("Ana:100")``.

        ``cls`` is the class itself, so subclasses get instances of the subclass.
        """
        owner, balance = text.split(":")
        return cls(owner.strip(), float(balance))

    @staticmethod
    def _check_positive(amount: float) -> None:
        """A static method needs neither ``self`` nor ``cls``."""
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def __repr__(self) -> str:
        return f"{type(self).__name__}(owner={self.owner!r}, balance={self._balance!r})"


class SavingsAccount(BankAccount):
    """Overriding a class attribute in a subclass."""

    interest_rate = 0.05
