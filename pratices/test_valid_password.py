import unittest
from pratices.valid_password import validate_password

class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(validate_password("Pass123!"))

    def test_length_validation(self):
        self.assertFalse(validate_password("Pa1!"))
        
    def test_uppercase_validation(self):
        self.assertFalse(validate_password("password123!"))
        
    def test_lowercase_validation(self):
        self.assertFalse(validate_password("PASSWORD123!"))
        
    def test_digit_validation(self):
        self.assertFalse(validate_password("Password!!!"))
        
    def test_special_char_validation(self):
        self.assertFalse(validate_password("Password123"))
        
    def test_empty_input(self):
        self.assertFalse(validate_password(""))

if __name__ == '__main__':
    unittest.main()