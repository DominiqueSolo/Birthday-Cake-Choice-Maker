import unittest
from unittest.mock import patch
import io
from src import birthday_dessert_choice_maker as bdc

class TestDessertMaker(unittest.TestCase):

    @patch('builtins.input', side_effect=['cupcakes', 'yolk', 'milk', 'screen', 'no'])
    def test_screen_output(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            bdc.main()
            self.assertIn("Classic Vanilla Cupcakes", fake_out.getvalue())

    @patch('builtins.input', side_effect=['whole cake', 'no yolk', 'milk', 'url', 'no'])
    def test_url_output(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            bdc.main()
            self.assertIn("Egg White Milk Cake", fake_out.getvalue())

    @patch('builtins.input', side_effect=['YOLK', 'MILK', 'cupcakes', 'screen', 'no'])
    def test_case_insensitive(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            bdc.main()
            self.assertIn("Egg White Milk Cupcakes", fake_out.getvalue())

    @patch('builtins.input', side_effect=['invalid', 'cupcakes', 'invalid', 'yolk', 'invalid', 'milk', 'url', 'no'])
    def test_invalid_entries(self, mock_input):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            bdc.main()
            output = fake_out.getvalue()
            self.assertIn("I’m sorry. I did not understand that.", output)
            self.assertIn("Classic Vanilla Cupcakes", output)

    @patch('builtins.input', side_effect=['end program'])
    def test_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            bdc.main()

if __name__ == '__main__':
    unittest.main()
