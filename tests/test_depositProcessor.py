import unittest

from selfOperationProcessors import DepositProcessor, PassedInvalidAmount, PassedInvalidAccountId
from bank import Bank
from account import Account


class TestDepositProcessor(unittest.TestCase):

    def test_deposit_to_not_added_to_bank_account(self):
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        with self.assertRaises(PassedInvalidAccountId):
            sut.operation(account.get_id, 100)

    def test_deposit_amount_with_zero_decimal_points(self):
        # Arrange
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 1000)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before + 1000, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_deposit_amount_with_one_decimal_point(self):
        # Arrange
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 1000.0)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before + 1000, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_deposit_amount_with_two_decimal_points(self):
        # Arrange
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_balance_before = account.balance
        account_transaction_history_before = len(account.transaction_history.show_history)
        # Act
        sut.operation(account.get_id, 1000.00)
        account_balance_after = account.balance
        account_transaction_history_after = len(account.transaction_history.show_history)
        # Assert
        self.assertEqual(account_balance_before + 1000, account_balance_after)
        self.assertEqual(account_transaction_history_before + 1, account_transaction_history_after)

    def test_deposit_amount_with_more_than_two_decimal_points(self):
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, 1000.001)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_deposit_zero_as_a_amount(self):
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, 0)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_deposit_string_as_amount(self):
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, "1234")

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)

    def test_deposit_negative_amount(self):
        bank = Bank()
        sut = DepositProcessor(bank)
        account = Account("Jan")
        bank.add_account(account)
        account_transaction_history_before = len(account.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(account.get_id, -1234)

        account_transaction_history_after = len(account.transaction_history.show_history)
        self.assertEqual(account_transaction_history_before, account_transaction_history_after)



if __name__ == '__main__':
    unittest.main()
