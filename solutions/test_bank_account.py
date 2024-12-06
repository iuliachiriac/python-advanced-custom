import unittest

from ex_6_5_class_methods import BankAccount


class BankAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("MyBank", 100)

    def test_initialization_without_balance(self):
        account = BankAccount("MyBank")
        self.assertIsInstance(account, BankAccount)
        self.assertTrue(hasattr(account, "bank_name"))
        self.assertEqual(account.bank_name, "MyBank")
        self.assertTrue(hasattr(account, "balance"))
        self.assertEqual(account.balance, 0)

    def test_initialization_with_balance(self):
        account = BankAccount("MyBank", 100)
        self.assertEqual(account.bank_name, "MyBank")
        self.assertEqual(account.balance, 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(150)
