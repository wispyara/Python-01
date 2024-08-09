"""Module random providing function to generate password.
Module string providing list of chars for choosing symbols."""

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


print("Welcome to the Linux User Password Generator!")
try:
    lengthOfPassword = int(input("Please enter the desired password length: "))
except ValueError:
    print("Value can't be a string type!")
else:
    try:
        if lengthOfPassword <= 0:
            raise ImportError(
                "Impossible to generate password with such length.")
    except ImportError:
        print("Value can't be a negative number!")
    else:
        input_parameters = str(input("""
    Which parameters you'd like to exclude:
    1. Exclude uppercase letters.
    2. Exclude lowercase letters.
    3. Exclude digits.
    4. Exclude special symbols.
    Enter parameters (e.g. 1, 2, 4 or 1 2 3 or 132): """))
        filtered_parameters = []
        for item in input_parameters:
            if item in ['1', '2', '3', '4']:
                filtered_parameters.append(item)
        try:
            if len(filtered_parameters) == 0:
                raise ImportError(
                    "Impossible to generate password with such parameters.")
        except ImportError:
            print("Impossible to generate password with such parameters.")
        else:
            is_uppercase = True
            is_lowercase = True
            is_digits = True
            is_special_chars = True
            filtered_parameters = list(set(filtered_parameters))
            filtered_parameters.sort()
            for item in filtered_parameters:
                if item == '1':
                    is_uppercase = False
                if item == '2':
                    is_lowercase = False
                if item == '3':
                    is_digits = False
                if item == '4':
                    is_special_chars = False
            new_password1 = PasswordGenerator(
                lengthOfPassword,
                is_uppercase,
                is_lowercase,
                is_digits,
                is_special_chars)
            print("Generated password:", new_password1.generate_password())
