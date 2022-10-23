import unittest

from accountToAccountOperationProcessors import TransferProcessor
from selfOperationProcessors import PassedInvalidAmount, NotEnoughFunds, PassedInvalidAccountId
from bank import Bank
from account import Account


class TestTransferProcessor(unittest.TestCase):

    def test_transfer_from_not_added_to_bank_account(self):
        bank = Bank()
        sut = TransferProcessor(bank)

        acc_from = Account("Jan", 1000)

        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)

        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAccountId):
            sut.operation(acc_from.get_id, acc_to.get_id, 500)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_to_not_added_to_bank_account(self):
        bank = Bank()
        sut = TransferProcessor(bank)

        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)

        acc_to = Account("Ala", 1000)

        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAccountId):
            sut.operation(acc_from.get_id, acc_to.get_id, 500)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_amount_with_zero_decimal_points(self):
        bank = Bank()
        sut = TransferProcessor(bank)

        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)

        acc_from_balance_before = acc_from.balance
        acc_to_balance_before = acc_to.balance
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        sut.operation(acc_from.get_id, acc_to.get_id, 500)
        acc_from_balance_after = acc_from.balance
        acc_to_balance_after = acc_to.balance
        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_balance_before - 500, acc_from_balance_after)
        self.assertEqual(acc_to_balance_before + 500, acc_to_balance_after)
        self.assertEqual(acc_from_transaction_history_before + 1, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before + 1, acc_to_transaction_history_after)

    def test_transfer_amount_with_one_decimal_point(self):
        bank = Bank()
        sut = TransferProcessor(bank)

        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)

        acc_from_balance_before = acc_from.balance
        acc_to_balance_before = acc_to.balance
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        sut.operation(acc_from.get_id, acc_to.get_id, 500.0)
        acc_from_balance_after = acc_from.balance
        acc_to_balance_after = acc_to.balance
        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_balance_before - 500, acc_from_balance_after)
        self.assertEqual(acc_to_balance_before + 500, acc_to_balance_after)
        self.assertEqual(acc_from_transaction_history_before + 1, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before + 1, acc_to_transaction_history_after)

    def test_transfer_amount_with_two_decimal_points(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_balance_before = acc_from.balance
        acc_to_balance_before = acc_to.balance
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        sut.operation(acc_from.get_id, acc_to.get_id, 500.00)
        acc_from_balance_after = acc_from.balance
        acc_to_balance_after = acc_to.balance
        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_balance_before - 500, acc_from_balance_after)
        self.assertEqual(acc_to_balance_before + 500, acc_to_balance_after)
        self.assertEqual(acc_from_transaction_history_before + 1, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before + 1, acc_to_transaction_history_after)

    def test_transfer_amount_with_more_than_two_decimal_points(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)
        with self.assertRaises(PassedInvalidAmount):
            sut.operation(acc_from.get_id, acc_to.get_id, -5.123456)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_amount_equal_to_account_balance(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_balance_before = acc_from.balance
        acc_to_balance_before = acc_to.balance
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        sut.operation(acc_from.get_id, acc_to.get_id, 1000)
        acc_from_balance_after = acc_from.balance
        acc_to_balance_after = acc_to.balance
        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_balance_before - 1000, acc_from_balance_after)
        self.assertEqual(acc_to_balance_before + 1000, acc_to_balance_after)
        self.assertEqual(acc_from_transaction_history_before + 1, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before + 1, acc_to_transaction_history_after)

    def test_transfer_amount_greater_than_account_balance(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        with self.assertRaises(NotEnoughFunds):
            sut.operation(acc_from.get_id, acc_to.get_id, 1001)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_zero_as_a_amount(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)

        with self.assertRaises(PassedInvalidAmount):
            sut.operation(acc_from.get_id, acc_to.get_id, 0)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)
        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_string_as_amount(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)
        with self.assertRaises(PassedInvalidAmount):
            sut.operation(acc_from.get_id, acc_to.get_id, "1000")

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)

    def test_transfer_negative_amount(self):
        bank = Bank()
        sut = TransferProcessor(bank)
        acc_from = Account("Jan", 1000)
        bank.add_account(acc_from)
        acc_to = Account("Ala", 1000)
        bank.add_account(acc_to)
        acc_from_transaction_history_before = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_before = len(acc_to.transaction_history.show_history)
        with self.assertRaises(PassedInvalidAmount):
            sut.operation(acc_from.get_id, acc_to.get_id, -1000)

        acc_from_transaction_history_after = len(acc_from.transaction_history.show_history)
        acc_to_transaction_history_after = len(acc_to.transaction_history.show_history)

        self.assertEqual(acc_from_transaction_history_before, acc_from_transaction_history_after)
        self.assertEqual(acc_to_transaction_history_before, acc_to_transaction_history_after)




if __name__ == '__main__':
    unittest.main()
