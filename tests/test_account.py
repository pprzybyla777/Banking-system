import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def test_set_id(self):
        sut = Account("Jan")
        sut.set_id("1234")
        self.assertEqual("1234", sut.id)  # add assertion here

    def test_get_id(self):
        sut = Account("Jan")
        self.assertEqual(None, sut.get_id)

if __name__ == '__main__':
    unittest.main()
