import re
import unittest
from random import randint

from src.password_generator import password_generator


class PasswordGeneratorFunctionTestCase(unittest.TestCase):
    """Tests for password_generator_function.py"""

    def setUp(self):
        self.random_length = randint(8, 129)

    def test_length_of_password_generated(self):
        """Test for correct length."""
        generated_password = password_generator(self.random_length, True, True, True)
        self.assertEqual(len(generated_password), self.random_length)

    def test_if_lowercase_numbers_capitals_and_symbols_are_in_password_generated(self):
        """Test for checking if there are lowercase, capital letters, numbers and symbols in generated password."""
        generated_password = password_generator(self.random_length, True, True, True)
        lowercase_check = re.search(r'[a-z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and digit_check and caps_check and symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_numbers_and_capitals_are_in_password_generated(self):
        """Test for checking if there are lowercase letters, capital letters and numbers in generated password."""
        generated_password = password_generator(self.random_length, True, True, False)
        lowercase_check = re.search(r'[a-z]', generated_password)
        num_check = re.search(r'\d', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and num_check and caps_check and not symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_capitals_and_symbols_are_in_password_generated(self):
        """Test for checking if there are lowercase letters, capital letters and symbols in generated password."""
        generated_password = password_generator(self.random_length, False, True, True)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and not digit_check and caps_check and symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_digits_and_symbols_are_in_password_generated(self):
        """Test for checking if there are lowercase letters, digits and symbols in generated password."""
        generated_password = password_generator(self.random_length, True, False, True)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and digit_check and not caps_check and symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_and_numbers_are_in_password_generated(self):
        """Test for checking if there are lowercase letters and numbers in generated password."""
        generated_password = password_generator(self.random_length, True, False, False)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        num_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and num_check and not caps_check and not symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_and_capitals_and_in_password_generated(self):
        """Test for checking if there are lowercase letters and capital letters in generated password."""
        generated_password = password_generator(self.random_length, False, True, False)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and not digit_check and caps_check and not symbol_check)
        self.assertTrue(check_password is True)

    def test_if_lowercase_and_symbols_and_in_password_generated(self):
        """Test for checking if there are lowercase letters and capital letters in generated password."""
        generated_password = password_generator(self.random_length, False, False, True)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and not digit_check and not caps_check and symbol_check)
        self.assertTrue(check_password is True)

    def test_if_only_lowercase_letters_in_password_generated(self):
        """Test for checking if there are lowercase letters and capital letters in generated password."""
        generated_password = password_generator(self.random_length, False, False, False)
        lowercase_check = re.search(r'[a-z]', generated_password)
        caps_check = re.search(r'[A-Z]', generated_password)
        digit_check = re.search(r'\d', generated_password)
        symbol_check = re.search(r'[^A-Za-z\d]', generated_password)
        check_password = bool(lowercase_check and not digit_check and not caps_check and not symbol_check)
        self.assertTrue(check_password is True)


if __name__ == '__main__':
    unittest.main()
