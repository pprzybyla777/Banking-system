import unittest
from bank import Bank, AlreadyAddedAccount, NotAnAccount
from account import Account


class TestBank(unittest.TestCase):

    def test_adding_non_added_account(self):
        # Arrange
        bank = Bank()
        account = Account("Jan")
        # Act
        bank.add_account(account)
        # Assert
        self.assertDictEqual({account.id: account}, bank.dict_of_accounts)

    def test_adding_already_added_account(self):
        sut = Bank()
        account = Account("Jan")
        sut.add_account(account)
        with self.assertRaises(AlreadyAddedAccount):
            sut.add_account(account)

    def test_adding_not_an_account(self):
        sut = Bank()
        not_an_account = {}
        with self.assertRaises(NotAnAccount):
            sut.add_account(not_an_account)

    def test_find_added_account(self):
        sut = Bank()
        account = Account("Jan")
        sut.add_account(account)
        res = sut.find_account(account.get_id)
        self.assertEqual(account, res)

    def test_find_not_added_account(self):
        sut = Bank()
        account = Account("Jan")
        res = sut.find_account(account.get_id)
        self.assertEqual(None, res)


if __name__ == '__main__':
    unittest.main()
