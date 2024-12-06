import pytest

from bank_account import BankAccount, InsufficientFunds


@pytest.fixture
def account():
    return BankAccount("MyBank", 100)


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


@pytest.mark.slow
def test_withdraw(account):
    account.withdraw(50)
    assert account.balance == 50


@pytest.mark.parametrize(["value", "raised_exception"], [
    (-100, ValueError),
    (200, InsufficientFunds),
])
def test_withdraw_insufficient_funds(account, value, raised_exception):
    with pytest.raises(raised_exception):
        account.withdraw(value)
    assert account.balance == 100
