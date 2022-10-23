import unittest
from helpers import Helpers


class TestHelpers(unittest.TestCase):
    def test_is_correct_type(self):
        self.assertEqual(Helpers.is_correct_type(2), True)
        self.assertEqual(Helpers.is_correct_type(2.0), True)
        self.assertEqual(Helpers.is_correct_type(-2.0), True)
        self.assertEqual(Helpers.is_correct_type(-2.12), True)
        self.assertEqual(Helpers.is_correct_type(-2.123), False)
        self.assertEqual(Helpers.is_correct_type("-2.12"), False)
        self.assertEqual(Helpers.is_correct_type([]), False)
        self.assertEqual(Helpers.is_correct_type({}), False)
        self.assertEqual(Helpers.is_correct_type(None), False)
        self.assertEqual(Helpers.is_correct_type(tuple()), False)

    def test_is_nonnegative(self):
        self.assertEqual(Helpers.is_nonnegative(-1), False)
        self.assertEqual(Helpers.is_nonnegative(-1.0), False)
        self.assertEqual(Helpers.is_nonnegative(0), False)
        self.assertEqual(Helpers.is_nonnegative(0.0), False)
        self.assertEqual(Helpers.is_nonnegative(1), True)
        self.assertEqual(Helpers.is_nonnegative(1.0), True)

    def test_is_amount_valid(self):
        self.assertEqual(Helpers.is_amount_valid(0), False)
        self.assertEqual(Helpers.is_amount_valid(-1), False)
        self.assertEqual(Helpers.is_amount_valid(-1.0), False)
        self.assertEqual(Helpers.is_amount_valid(0.1234), False)
        self.assertEqual(Helpers.is_amount_valid(0.01), True)
        self.assertEqual(Helpers.is_amount_valid(1), True)
        self.assertEqual(Helpers.is_amount_valid(1.0), True)
        self.assertEqual(Helpers.is_amount_valid(1.00), True)


    def test_are_funds_sufficient(self):
        self.assertEqual(Helpers.are_funds_sufficient(0, 0), True)
        self.assertEqual(Helpers.are_funds_sufficient(0, 1), False)
        self.assertEqual(Helpers.are_funds_sufficient(1, 0), True)
        self.assertEqual(Helpers.are_funds_sufficient(1, 1), True)


if __name__ == '__main__':
    unittest.main()
