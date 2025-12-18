print('''
+ Add
- Subtract
* Multiply
/ Divide
''')

num1= int(input("Enter your value1:-  "))
num2= int(input("Enter your value2:-  "))
opr = input("Enter the operator(+,-,*,/):  ")

if opr == "+":
    print("Your answer is: ",num1+num2)
elif opr == "-":
    print("Your answer is: ",num1-num2)
elif opr == "*":
    print("Your answer is: ",num1*num2)
elif opr == "/":
    print("Your answer is: 10",num1/num2)
else:
    print("Invalid operator")

