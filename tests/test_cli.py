import unittest
from unittest.mock import patch

from sci_calculator.cli import main


class CliTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["99", "0"])
    @patch("builtins.print")
    def test_invalid_choice_does_not_crash(self, mocked_print, _mocked_input):
        self.assertEqual(main(), 0)
        messages = [str(call.args[0]) for call in mocked_print.call_args_list if call.args]
        self.assertIn("Scelta non valida. Riprova.", messages)

    @patch("builtins.input", side_effect=["1", "/", "1", "0", "0"])
    @patch("builtins.print")
    def test_operation_error_returns_to_menu(self, mocked_print, _mocked_input):
        self.assertEqual(main(), 0)
        messages = [str(call.args[0]) for call in mocked_print.call_args_list if call.args]
        self.assertTrue(any("dividere per zero" in message for message in messages))


if __name__ == "__main__":
    unittest.main()
