"""Module random providing function to generate password.
Module string providing list of chars for choosing symbols."""

from random import choice
from string import punctuation, ascii_uppercase, ascii_lowercase, digits


class PasswordGenerator:
    def __init__(self, length=8, include_uppercase=True,
                 include_lowercase=True, include_digits=True,
                 include_special_chars=True):
        self.length = length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special_chars = include_special_chars

    def generate_password(self):
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
    length = int(input("Please enter the desired password length: "))
except ValueError:
    print("Value can't be a string type!")
else:
    try:
        if length <= 0:
            raise Exception(
                "Impossible to generate password with such length.")
    except Exception:
        print("Value can't be a negative number!")
    else:
        params = str(input("""
    Which parameters you'd like to exclude:
    1. Exclude uppercase letters.
    2. Exclude lowercase letters.
    3. Exclude digits.
    4. Exclude special symbols.
    Enter parameters (e.g. 1, 2, 4 or 1 2 3 or 132): """))
        filtered_params = []
        for item in params:
            if item in ['1', '2', '3', '4']:
                filtered_params.append(item)
        try:
            if len(filtered_params) == 0:
                raise Exception(
                    "Impossible to generate password with such parameters.")
        except Exception:
            print("Impossible to generate password with such parameters.")
        else:
            include_uppercase = True
            include_lowercase = True
            include_digits = True
            include_special_chars = True
            filtered_params = list(set(filtered_params))
            filtered_params.sort()
            for item in filtered_params:
                if item == '1':
                    include_uppercase = False
                if item == '2':
                    include_lowercase = False
                if item == '3':
                    include_digits = False
                if item == '4':
                    include_special_chars = False
            new_password1 = PasswordGenerator(
                length, include_uppercase,
                include_lowercase,
                include_digits,
                include_special_chars)
            print("Generated password:", new_password1.generate_password())
