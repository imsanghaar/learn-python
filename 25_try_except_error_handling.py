# Try, Except, Error Handling in Python

# This script demonstrates how to handle errors in Python using try and except blocks.
# It includes examples of handling specific exceptions and using a finally block.
# Types of Error:
# 1. SyntaxError
# 2. NameError
# 3. TypeError
# 4. IndexError
# 5. KeyError
# 6. ValueError
# 7. AttributeError
# 8. ZeroDivisionError
# Exception Handling Examples:
# Example 1: Handling ZeroDivisionError
# Example 2: Handling ValueError
# Exception is a global error class in Python
# we can use as e for printing the error message


# In This Error; Handling Practice Project, we will create a simple calculator that takes two numbers and an operator as input from the user and performs the corresponding arithmetic operation. We will handle potential errors such as division by zero and invalid input.
# If ValueError occurs, we will prompt the user to enter valid numbers.
# If ZeroDivisionError occurs, we will inform the user that division by zero is not allowed.
# For any other unexpected errors, we will display a generic error message.
# The calculator will support addition, subtraction, multiplication, and division operations.
# The user will be prompted to enter the operator (+, -, *, /) and the two numbers.
# The result of the operation will be displayed to the user.
# Here is the code for the project:
def calculate(opr: str):  
# Function to perform calculation based on the operator provided
    try:
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))
# Perform the operation based on the operator
        if opr == "+":
            print(num1 + num2)
        elif opr == "-":
            print(num1 - num2)
        elif opr == "*":
            print(num1 * num2)
        elif opr == "/":
            print(num1 / num2)
        else:
            raise Exception("Invalid Operator") # raising custom exception for invalid operator
# Handling specific exceptions
    except ZeroDivisionError as e:
        print(e)
        print("Cannot divide by zero!")
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as err: # adding custom exception or error message
        print(err)
        print("Something Went Wrong")
    
# The else block will execute if there is no error in try block
    else: # This will execute if there is no error. It is part of try block and except block.
        print("Operation completed successfully!")
    finally:  # This will always execute in last no matter what
        print("Thank you for using the calculator!")

calculate(input("Enter the operator (+, -, *, /): "))
# Call the calculate function with user-provided operator
# This code will handle errors gracefully and provide feedback to the user based on the type of error encountered. 
# You can run this code in a Python environment to test its functionality.
