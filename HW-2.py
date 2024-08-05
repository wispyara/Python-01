# Requirements:

# The program should prompt the user to enter a username.
# The program should check if user exist in system.
# The program should ask the user to input a password or generate a new one if not provided.
# The program should check the password against specified requirements
# minimum length
# presence of different character types (uppercase, lowercase, digits, special characters)
# any other criteria you specify.
# Change password for user
# The program should print the results, including the username, the original or generated password, and whether the password meets the requirements.


import os
import random
import subprocess

username = input("Please enter your username: ")
# os.system(f'grep {username} /etc/passwd')
os.system(f'net user Guest')
