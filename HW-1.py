# Homework Assignment: Python Internals

# Task: Create a Calculator

# As we started discuss on Lection a basic program that can ever exist - Calculator,

# Your task is to create a basic calculator program using Python.

# The program should allow the user to perform simple arithmetic operations on two numbers.

# Requirements:

# Prompt the user to enter two numbers.
# Prompt the user to select an operation from the following options:
# addition
# subtraction
# multiplication
# division.

# Note:

# Ensure that the program handles division by zero and provides an appropriate error message if the user attempts to divide by zero. Consider using functions to encapsulate the calculation logic for each operation. Include clear instructions and error handling for invalid input.

def calculate(number1, number2, operation):
    match operation:
        case 1:
            return print("The result of addition is: ",number1 + number2)
        case 2:
            return print("The result of subtraction is: ",number1 - number2)
        case 3:
            return print("The result of multiplication is: ",number1 * number2)
        case 4:
            try:
                return print("The result of division is: ",number1 / number2)
            except ZeroDivisionError:
                print("Division by zero!")
        
print("Welcome to the Calculator Program!")
try:
    number1=int(input("Please enter the first number: "))
    number2=int(input("Please enter the second number: "))
except ValueError:
    print("Value can't be a string type!")
try:
    operation=int(input('''
Please select an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter your choice (1-4): '''))
    try:
        if (operation < 1) and (operation > 4): 
            raise Exception("Value must be in range from 1 to 4!")
        else:
            calculate(number1, number2, operation)
    except Exception:
        print("Value must be in range from 1 to 4!")
except ValueError:
    print("Value must be integer!")
