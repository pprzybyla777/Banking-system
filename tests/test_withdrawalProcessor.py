import unittest

from selfOperationProcessors import WithdrawProcessor, PassedInvalidAmount, NotEnoughFunds, PassedInvalidAccountId
from account import Account
from bank import Bank


class TestWithdrawalProcessor(unittest.TestCase):

    def test_withdraw_from_not_added_to_bank_account(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan")
        with self.assertRaises(PassedInvalidAccountId):
            sut.operation(account.get_id, 100)

    def test_withdraw_amount_with_zero_decimal_points(self):
        # Arrange
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1000)
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 100)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before - 100, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_withdraw_amount_with_one_decimal_point(self):
        # Arrange
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1000)
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 100.0)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before - 100, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_withdraw_amount_with_two_decimal_points(self):
        # Arrange
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1000)
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 100.00)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before - 100, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_withdraw_amount_with_more_than_two_decimal_points(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1000)
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, 100.001)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_withdraw_amount_equal_to_account_balance(self):
        # Arrange
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1000)
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, account.balance)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(0, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_withdraw_amount_greater_than_account_balance(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(NotEnoughFunds):
            sut.operation(account.get_id, account.balance + 1234)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_withdraw_zero_as_a_amount(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1)
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, 0)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_withdraw_string_as_amount(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1234)
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, "1234")

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_withdraw_negative_amount(self):
        bank = Bank()
        sut = WithdrawProcessor(bank)
        account = Account("Jan", 1234)
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, -1234)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)


if __name__ == '__main__':
    unittest.main()
