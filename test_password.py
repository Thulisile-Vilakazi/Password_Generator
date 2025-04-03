import unittest
from unittest.mock import patch
from io import StringIO

from password import password_generator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.test_inputs = "3\n2\n2\n"
    
    def test_password_length(self):
        with patch('sys.stdin', StringIO(self.test_inputs)):
            password = password_generator()
            self.assertEqual(len(password), 7)
    
    def test_contains_letters(self):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        with patch('sys.stdin', StringIO(self.test_inputs)):
            password = password_generator()
            self.assertTrue(any(c in letters for c in password))
    
    def test_contains_symbols(self):
        symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        with patch('sys.stdin', StringIO(self.test_inputs)):
            password = password_generator()
            self.assertTrue(any(c in symbols for c in password))
    
    def test_contains_numbers(self):
        numbers = '0123456789'
        with patch('sys.stdin', StringIO(self.test_inputs)):
            password = password_generator()
            self.assertTrue(any(c in numbers for c in password))
    
    def test_shuffled(self):
        with patch('sys.stdin', StringIO(self.test_inputs)):
            password1 = password_generator()
            password2 = password_generator()
            self.assertNotEqual(password1, password2)
    
    def test_zero_length(self):
        with patch('sys.stdin', StringIO("0\n0\n0\n")):
            password = password_generator()
            self.assertEqual(password, "")

if __name__ == '__main__':
    unittest.main()