"""
Importing module unittest to ensure class PasswordGenerator is working correct
Module random providing function to generate password.
Module string providing list of chars for choosing symbols.
"""
import unittest
from random import choice
from string import punctuation, ascii_uppercase, ascii_lowercase, digits


class PasswordGenerator:
    """Class represent a generator of passwords"""

    def __init__(self,
                 length=8,
                 include_uppercase=True,
                 include_lowercase=True,
                 include_digits=True,
                 include_special_chars=True):
        """
        Initializing of class variables.

        Parameters:
        length (int): Length of password.
        include_uppercase (boolean): Password contains uppercase letters.
        include_lowercase (boolean): Password contains lowercase letters.
        include_digits (boolean): Password contains numbers.
        include_special_chars (boolean): Password contains special characters.
        """
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self):
        """"
        Generates password based on give parameters such as:
        Length of password;
        Presence of lowercase, uppercase and special characters, numbers 
        """
        chars = ''
        password = ''
        if self.include_uppercase:
            chars += ascii_uppercase
        if self.include_lowercase:
            chars += ascii_lowercase
        if self.include_digits:
            chars += digits
        if self.include_special_chars:
            chars += punctuation
        for _ in range(self.length):
            password += str(choice(chars))
        return password


class MyTest(unittest.TestCase):
    """Class for testing of hw4 module"""

    def test_for_length_1(self):
        # Act
        password1 = PasswordGenerator(include_uppercase=False,
                                      include_lowercase=True,
                                      include_digits=True,
                                      include_special_chars=True)
        # Assert
        result = password1.generate_password()
        self.assertEqual(len(result), 8)

    def test_for_length_2(self):
        # Act
        password1 = PasswordGenerator(-99)
        # Assert
        result = password1.generate_password()
        self.assertEqual(len(result), 0)

    def test_for_length_2(self):
        # Act
        test_length = 10
        password1 = PasswordGenerator(length=test_length)
        # Assert
        result = password1.generate_password()
        self.assertEqual(len(result), test_length)

    def test_for_includes_1(self):
        # Act
        password1 = PasswordGenerator(include_uppercase=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(ascii_uppercase)
        self.assertEqual(set1 & set2, set())

    def test_for_includes_2(self):
        # Act
        password1 = PasswordGenerator(include_digits=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(digits)
        self.assertEqual(set1 & set2, set())

    def test_for_includes_3(self):
        # Act
        password1 = PasswordGenerator(include_lowercase=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(ascii_lowercase)
        self.assertEqual(set1 & set2, set())

    def test_for_includes_4(self):
        # Act
        password1 = PasswordGenerator(include_special_chars=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(punctuation)
        self.assertEqual(set1 & set2, set())

    def test_for_includes_5(self):
        # Act
        password1 = PasswordGenerator(include_special_chars=False,
                                      include_lowercase=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(punctuation)
        set3 = set(ascii_lowercase)
        self.assertEqual(set1 & set2 & set3, set())

    def test_for_includes_6(self):
        # Act
        password1 = PasswordGenerator(include_uppercase=False,
                                      include_digits=False)
        # Assert
        set1 = set(password1.generate_password())
        set2 = set(ascii_uppercase)
        set3 = set(digits)
        self.assertEqual(set1 & set2 & set3, set())
    
if __name__ == "__main__":
    unittest.main()