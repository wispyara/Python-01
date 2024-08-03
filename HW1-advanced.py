# Task Advanced: Create a Password Generator for Linux Users

# Your task is to create a password generator program using Python specifically designed for Linux users. The program should generate strong and secure passwords that can be used for user accounts on Linux systems.

# Requirements:

# Prompt the user to enter the desired length for the password. Generate a random password consisting of a combination of uppercase letters, lowercase letters, numbers, and special characters. Ensure that the generated password meets the following criteria:

# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one number
# Contains at least one special character (e.g., !, @, #, $, %, etc.)
# Display the generated password to the user.

from random import choice, shuffle
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

def pass_generator (size=12, chars=punctuation + ascii_uppercase + ascii_lowercase + digits):
    password=[(choice(punctuation)), (choice(ascii_uppercase)), (choice(ascii_lowercase)), (choice(digits))]
    for _ in range(size-4):
        password.append(choice(chars))
    shuffle(password)
    return ''.join(str(item) for item in password)

print("Welcome to the Linux User Password Generator!")
try:
    length = int(input("Please enter the desired password length: "))
    try:
        if length < 4: 
            raise Exception("Value can't be less then 4 because of requirements")
        else:
            print("Generated password:", pass_generator(length))
    except Exception:
        print("Value can't be less then 4 because of requirements")
except ValueError:
    print("Value can't be a string type!")