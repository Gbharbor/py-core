"""
Lesson: Encapsulation and @property

The balance is protected and can only be changed through methods.
"""


class BankAccount:
    """Simple bank account with protected balance."""

    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        amount = float(amount)

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self._balance += amount

    def withdraw(self, amount):
        amount = float(amount)

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False

        if self._balance >= amount:
            self._balance -= amount
            return True

        return False


account = BankAccount()
account.deposit(200)

withdraw_amount = float(input("How much do you want to withdraw? "))

if account.withdraw(withdraw_amount):
    print("Withdrawal completed")
else:
    print("Insufficient balance")

print(f"Current balance: {account.balance}")