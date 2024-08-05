import os

def check_for_username (username: str):
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if username == line.split(':')[0]:
                    return line
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("Error reading file!")
    else:
        print("File read successfully!")
        
username = input("Please enter your username: ")
print(check_for_username(username))