"""Run a short tour of every lesson."""

from learning_classes.bank_account import BankAccount, InsufficientFundsError, SavingsAccount
from learning_classes.dog import Dog
from learning_classes.shapes import Circle, Rectangle, Square, total_area
from learning_classes.vector import Vector


def main() -> None:
    print("== Lesson 1: basics")
    rex = Dog("Rex", 3)
    rex.learn("sit")
    print(rex, "|", repr(rex), "|", rex.bark(), "| tricks:", rex.tricks)

    print("\n== Lesson 2: encapsulation")
    account = BankAccount.from_string("Ana:100")
    account.deposit(50)
    try:
        account.withdraw(500)
    except InsufficientFundsError as error:
        print("Error:", error)
    savings = SavingsAccount("Ben", 100)
    savings.add_interest()
    print(account, savings)

    print("\n== Lesson 3: inheritance")
    shapes = [Rectangle(2, 3), Square(2), Circle(1)]
    for shape in shapes:
        print(shape.describe())
    print(f"Total area: {total_area(shapes):.2f}")

    print("\n== Lesson 4: dataclasses")
    v = Vector(3, 4)
    print(v, v + Vector(1, 1), 2 * v, abs(v), v == Vector(3, 4))


if __name__ == "__main__":
    main()
