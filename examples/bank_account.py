class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds.")
        self.balance -= amount
