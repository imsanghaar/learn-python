# In This Error; Handling Practice Project, we will create a simple calculator that takes two numbers and an operator as input from the user and performs the corresponding arithmetic operation. We will handle potential errors such as division by zero and invalid input.
# If ValueError occurs, we will prompt the user to enter valid numbers.
# If ZeroDivisionError occurs, we will inform the user that division by zero is not allowed.
# For any other unexpected errors, we will display a generic error message.
# The calculator will support addition, subtraction, multiplication, and division operations.
# The user will be prompted to enter the operator (+, -, *, /) and the two numbers.
# The result of the operation will be displayed to the user.
# Here is the code for the project:
def calculate(opr: str):  
    try:
        num1 = int(input("Enter Your First Number: "))
        num2 = int(input("Enter Your Second Number: "))

        if opr == "+":
            print(num1 + num2)
        elif opr == "-":
            print(num1 - num2)
        elif opr == "*":
            print(num1 * num2)
        elif opr == "/":
            print(num1 / num2)
        else:
            print("Invalid operator")

    except ZeroDivisionError as e:
        print(e)
        print("Cannot divide by zero!")
    except ValueError:
        print("Please enter valid numbers!")
    except Exception:
        print("Something Went Wrong")
    
    finally: 
        print("Thank you for using the calculator!")

calculate("+")

