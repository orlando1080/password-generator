from random import choice, randint
from string import punctuation
import unittest

from src.password_generator import password_generator
from src.password_type_count import password_type_count


class PasswordTypeCountFunctionTestCase(unittest.TestCase):
    """Tests for password_type_count_function.py."""

    def setUp(self):
        self.password = password_generator(randint(8, 129), choice([True, False]), choice([True, False]),
                                           choice([True, False]))
        self.type_count = password_type_count(self.password)

    def test_if_password_type_count_function_counts_lowercase_letters(self):
        """Tests the password count of lowercase letters."""
        lowercase_count = self.type_count['lowercase']
        self.assertEqual(lowercase_count, sum(1 for char in self.password if char.islower()))

    def test_if_password_type_count_function_counts_digits(self):
        """Tests the password count of digits."""
        digit_count = self.type_count['digits']
        self.assertEqual(digit_count, sum(1 for char in self.password if char.isdigit()))

    def test_if_password_type_count_function_counts_uppercase_letters(self):
        """Tests the password count of uppercase letters."""
        uppercase_count = self.type_count['uppercase']
        self.assertEqual(uppercase_count, sum(1 for char in self.password if char.isupper()))

    def test_if_password_type_count_function_counts_symbols(self):
        """Tests the password count of symbols."""
        symbol_count = self.type_count['symbols']
        self.assertEqual(symbol_count, sum(1 for char in self.password if char in punctuation))


if __name__ == '__main__':
    unittest.main()
