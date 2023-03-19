import unittest
from unittest.mock import patch
from src.get_validated_password_length_input import get_validated_password_length_input


class GetValidatedPasswordLengthInputTestCase(unittest.TestCase):
    """Tests password length input validation."""

    def test_valid_input(self):
        """Tests if input is valid."""
        prompt = 'What length? (8-128): '
        with patch("builtins.input", return_value='89'):
            response = get_validated_password_length_input(prompt)
        self.assertEqual(response, '89')

    def test_valid_input_min_value(self):
        """Tests if input is valid."""
        prompt = 'What length? (8-128): '
        with patch("builtins.input", return_value='8'):
            response = get_validated_password_length_input(prompt)
        self.assertEqual(response, '8')

    def test_valid_input_max_value(self):
        """Tests if input is valid."""
        prompt = 'What length? (8-128): '
        with patch("builtins.input", return_value='128'):
            response = get_validated_password_length_input(prompt)
        self.assertEqual(response, '128')

    def test_invalid_input_then_valid_input(self):
        """Test if input is invalid."""
        prompt = 'What length? (8-128): '
        with patch("builtins.input", side_effect=["3", '129', 'a', 'B', "89"]):
            response = get_validated_password_length_input(prompt)
        self.assertEqual(response, "89")


if __name__ == '__main__':
    unittest.main()
