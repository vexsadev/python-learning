import pytest

from learning_classes.bank_account import (
    BankAccount,
    InsufficientFundsError,
    SavingsAccount,
)


def test_deposit_and_withdraw():
    account = BankAccount("Ana", 100)
    assert account.deposit(50) == 150
    assert account.withdraw(30) == 120
    assert account.balance == 120


def test_balance_is_read_only():
    account = BankAccount("Ana")
    with pytest.raises(AttributeError):
        account.balance = 1_000_000


def test_overdraw_raises():
    with pytest.raises(InsufficientFundsError):
        BankAccount("Ana", 10).withdraw(20)


@pytest.mark.parametrize("amount", [0, -5])
def test_amount_must_be_positive(amount):
    account = BankAccount("Ana", 10)
    with pytest.raises(ValueError):
        account.deposit(amount)
    with pytest.raises(ValueError):
        account.withdraw(amount)


def test_negative_opening_balance_rejected():
    with pytest.raises(ValueError):
        BankAccount("Ana", -1)


def test_from_string_classmethod():
    account = BankAccount.from_string("Ana : 42.5")
    assert account.owner == "Ana"
    assert account.balance == 42.5


def test_from_string_returns_subclass():
    assert type(SavingsAccount.from_string("Ben:1")) is SavingsAccount


def test_subclass_overrides_interest_rate():
    assert BankAccount("Ana", 100).add_interest() == pytest.approx(102)
    assert SavingsAccount("Ben", 100).add_interest() == pytest.approx(105)


def test_repr_uses_class_name():
    assert repr(SavingsAccount("Ben", 5)) == "SavingsAccount(owner='Ben', balance=5)"
