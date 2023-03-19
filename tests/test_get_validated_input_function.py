import unittest
from unittest.mock import patch

from src.get_validated_input import get_validated_input


class GetValidatedInputTestCase(unittest.TestCase):
    """Tests input validation."""

    def test_valid_input(self):
        """Tests if input is valid."""
        valid_responses = ["yes", "no"]
        prompt = "Do you want to proceed? (Yes/No): "
        with patch("builtins.input", return_value="yes"):
            response = get_validated_input(prompt, valid_responses)
        self.assertEqual(response, "yes")

    def test_invalid_input_then_valid_input(self):
        """Test if input is invalid."""
        valid_responses = ["yes", "no"]
        prompt = "Do you want to proceed? (Yes/No): "
        with patch("builtins.input", side_effect=["maybe", "yes"]):
            response = get_validated_input(prompt, valid_responses)
        self.assertEqual(response, "yes")


if __name__ == '__main__':
    unittest.main()
