
import unittest
from unittest.mock import patch
import builtins

from your_script_filename import normalize_input, get_valid_input, recipes

class TestDessertChoiceMaker(unittest.TestCase):

    def test_normalize_input(self):
        self.assertEqual(normalize_input("  WHOLE Cake "), "whole cake")
        self.assertEqual(normalize_input("Yolk"), "yolk")
        self.assertEqual(normalize_input("no Milk"), "no milk")

    @patch('builtins.input', side_effect=['invalid', 'Whole Cake'])
    def test_get_valid_input_corrects_invalid_then_accepts_valid(self, mock_input):
        result = get_valid_input("Test prompt: ", ['whole cake', 'cupcakes'])
        self.assertEqual(result, 'whole cake')

    def test_recipe_combinations_exist(self):
        expected_keys = [
            ('whole cake', 'yolk', 'milk'),
            ('whole cake', 'no yolk', 'milk'),
            ('whole cake', 'yolk', 'no milk'),
            ('whole cake', 'no yolk', 'no milk'),
            ('cupcakes', 'yolk', 'milk'),
            ('cupcakes', 'yolk', 'no milk'),
            ('cupcakes', 'no yolk', 'milk'),
            ('cupcakes', 'no yolk', 'no milk')
        ]
        for key in expected_keys:
            self.assertIn(key, recipes)

    def test_recipe_fields_present(self):
        for key, recipe in recipes.items():
            self.assertIn('name', recipe)
            self.assertIn('ingredients', recipe)
            self.assertIn('time', recipe)
            self.assertIn('instructions', recipe)
            self.assertIn('url', recipe)

if __name__ == '__main__':
    unittest.main()
