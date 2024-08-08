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
import subprocess
from random import choice, shuffle
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

def check_for_username (username: str):
    result = subprocess.run(["grep", username, "/etc/passwd"], stdout=subprocess.PIPE, text=True)
    if result.returncode == 1:
        print("There is no such a user!")
        return False
    # elif 'username:' doesn't contain in result - print("There is no such a user")
    elif result.returncode == 0:
        lines = result.stdout.split('\n')
        for line in lines:
            if username == line.split(':')[0]:
                print(f"There is such a user as {username}.\n{line}")
                return True
        print(f"There user {username} wasn't found.")
        return False

def pass_generator (size=12, chars=punctuation + ascii_uppercase + ascii_lowercase + digits):
    # Generating a string which will pass through condition 
    # There are no if conditions for checking due to optimization. Code will execute faster.
    password=[(choice(punctuation)), (choice(ascii_uppercase)), (choice(ascii_lowercase)), (choice(digits))]
    for _ in range(size-4):
        password.append(choice(chars))
    shuffle(password)
    return ''.join(str(item) for item in password)

def change_password(username, new_password):
    try:
        # Start the passwd process
        process = subprocess.Popen(
            ['sudo','passwd', username],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Sending old password, new password, and confirmation
        process.stdin.write(new_password + '\n')
        process.stdin.write(new_password + '\n')
        process.stdin.flush()

        # Capture the output and error messages
        stdout, stderr = process.communicate()

        # Print the username and password
        print(f'''
Username: {username}
Password: {new_password}

Output: {stdout}
              ''')

    except Exception as e:
        print(f"An error occurred: {e} and {stderr}")

username = input("Please enter your username: ")
if check_for_username(username):
    try:
        operation=int(input('''
Please select an operation to change your password:
1. Manually
2. Password Generator
Enter your choice (1-2): '''))
        try:
            if (operation < 1) and (operation > 2): 
                raise Exception("Value must be in range from 1 to 2!")
            elif operation == 1:
                # manually
                new_password = input("Please enter your new password: ")
            else:
                # pass generator
                print("Welcome to the Linux User Password Generator!")#
                try:
                    length = int(input("Please enter the desired password length: "))
                    try:
                        if length < 4: 
                            raise Exception("Value can't be less then 4 because of requirements")
                        else:
                            new_password = pass_generator(length)
                            print("Generated password:", new_password)
                    except Exception:
                        print("Value can't be less then 4 because of requirements")
                except ValueError:
                    print("Value can't be a string type!")
        except Exception:
            print("Value must be in range from 1 to 2!")
        else:
            change_password(username, new_password)
    except ValueError:
        print("Value must be integer!")    
