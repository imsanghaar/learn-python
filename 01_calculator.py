# Calculator with function method

print('''
Addition
Subtraction
Division
Multiplication
''')


def calculator():
    print("Calculator")
  
num1 = float(input("Enter the Value 1: "))
num2 = float(input("Enter The Value 2: "))
op = input("Select the Operation (+,-,*,/): ")

if op == "+":
    print("num1 + num2 = ", num1 + num2)
elif op == "-":
    print("num1 - num2 = ", num1 - num2)
elif op == "*":
    print("num1 * num2 = ", num1 * num2)
elif op == "/":
    print("num1 / num2 = ", num1 / num2)
else:
    print("Invalid Syntax")


    calculator()