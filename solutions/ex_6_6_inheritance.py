class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class CreditBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft exceeded.")
        self.balance -= amount


if __name__ == "__main__":
    my_account = CreditBankAccount("RandomBank", 100, 50)
    my_account.withdraw(50)
    my_account.deposit(20)
    print(my_account.bank_name, my_account.balance)

    my_account.withdraw(100)
    print(my_account.bank_name, my_account.balance)

    try:
        my_account.withdraw(100)
    except ValueError as ex:
        print(ex)
    print(my_account.bank_name, my_account.balance)
