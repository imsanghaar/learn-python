print("Simple Calculator")

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    opr = input("Enter operator (+, -, /, *, %): ")

    if opr == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opr == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opr == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero")
    elif opr == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opr == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Invalid operator. Please enter (+, -, /, *, %)")

    # Ask user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no or y/n): ").strip().lower()
    if again not in ('yes', 'y'):
        print("Exiting calculator... Goodbye!")
        break

    print()  # for spacing between operations
