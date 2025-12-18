Python Basics — A quick and simple guide to start learning Python

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/ff819f75-ae1c-47e2-bacb-b18d4ceb89b6" />









A flow Chart of PYTHON BASICS

<img width="246" height="768" alt="python_basics_flowchart" src="https://github.com/user-attachments/assets/6c8c71fd-cdeb-4635-a6aa-82ce2c924813" />

## 📦 Variables in Python

In Python, **variables** act like containers (or boxes) that hold values.  
Think of it like a **pizza box** 🍕 — the box is the **variable**, and the pizza inside is the **value**.  

You can store different kinds of data in variables such as text, numbers, or more complex objects.

### 📝 Example
```python
# Variables are like boxes, storing values inside them.

name = "Sanghaar"     # A variable storing a string
age = 17              # A variable storing an integer
caste = "Chandio"     # Another string variable
school = "SZABIST"    # Yet another string variable

# Printing values stored in variables
print("Hello", name, caste)
print("Your age is", age)
print("You study in", school)

▶️ Output
Hello Sanghaar Chandio
Your age is 17
You study in SZABIST

✅ Key Points

A variable is created by assigning a value with the = operator.

Variables can store different data types like strings ("Sanghaar") or integers (17).

You can use variables inside functions like print() to display their values.

## 🔤 Data Types in Python

In Python, every value stored in a variable has a specific **data type**.  
Data types define the kind of value a variable can hold, such as **text, numbers, or boolean values**.

### 📝 Example
```python
# Different data types in Python

name = "Sanghaar"      # String (text)
age = 17               # Integer (whole number)
is_student = True      # Boolean (True/False)

# Checking the type of each variable
name_type = type(name)
age_type = type(age)
is_student_type = type(is_student)

print("The type of name is :", name_type)
print("The type of age is :", age_type)
print("The type of is_student is :", is_student_type)

▶️ Output
The type of name is : <class 'str'>
The type of age is : <class 'int'>
The type of is_student is : <class 'bool'>
✅ Key Points

str (String): Used for text values, e.g., "Sanghaar".

int (Integer): Used for whole numbers, e.g., 17.

bool (Boolean): Used for logical values True or False.

Use the built-in type() function to check the data type of any variable.


## ➗ Arithmetic Operators in Python

Arithmetic operators are used to perform **basic mathematical operations** on numbers such as addition, subtraction, multiplication, division, etc.

### 📝 Example
```python
x = 10
y = 2

print("Let's do Arithmetic Operations:")
print("Let's suppose x = 10 and y = 2")

# Addition
print("1. Addition:")
print("x + y =", x + y)

# Multiplication
print("2. Multiplication:")
print("x * y =", x * y)

# Subtraction
print("3. Subtraction:")
print("x - y =", x - y)

# Division
print("4. Division:")
print("x / y =", x / y)

# Floor Division
print("5. Floor Division:")
print("x // y =", x // y)

# Modulus
print("6. Modulus:")
print("x % y =", x % y)

# Exponentiation
print("7. Exponentiation:")
print("x ** y =", x ** y)

▶️ Output
Let's do Arithmetic Operations:
Let's suppose x = 10 and y = 2
1. Addition:
x + y = 12
2. Multiplication:
x * y = 20
3. Subtraction:
x - y = 8
4. Division:
x / y = 5.0
5. Floor Division:
x // y = 5
6. Modulus:
x % y = 0
7. Exponentiation:
x ** y = 100

✅ Key Points

+ → Addition

- → Subtraction

* → Multiplication

/ → Division (returns float)

// → Floor Division (ignores decimal part)

% → Modulus (remainder)

** → Exponentiation (power)

## 🖊️ Assignment Operators in Python

Assignment operators are used to **assign values to variables** and also perform operations while assigning.  
They provide a shorthand way to update the value of a variable.

### 📝 Example
```python
num = 50
print("Initial Value =", num)

num += 5     # Add and assign
print("After num += 5 :", num)

num *= 2     # Multiply and assign
print("After num *= 2:", num)

num -= 4     # Subtract and assign
print("After num -= 4:", num)

print("Final Value after solution is =", num)
▶️ Output
Initial Value = 50
After num += 5 : 55
After num *= 2: 110
After num -= 4: 106
Final Value after solution is = 106

✅ Key Points

= → Assigns value to a variable

+= → Adds value and assigns result

-= → Subtracts value and assigns result

*= → Multiplies value and assigns result

/= → Divides value and assigns result

%= → Modulus and assigns result

**= → Exponentiation and assigns result

//= → Floor division and assigns result


## ⚖️ Comparison Operators in Python

Comparison operators are used to **compare two values**.  
They return a **Boolean value** (`True` or `False`) depending on whether the condition is satisfied.

### 📝 Example
```python
s = 100
t = 99

print(s > t)   # Greater than
print(s < t)   # Less than
print(s == t)  # Equal to
print(s != t)  # Not equal to
print(s >= t)  # Greater than or equal to
print(s <= t)  # Less than or equal to

▶️ Output
True
False
False
True
True
False

✅ Key Points

> → Returns True if left value is greater than right

< → Returns True if left value is less than right

== → Returns True if both values are equal

!= → Returns True if values are not equal

>= → Returns True if left value is greater or equal

<= → Returns True if left value is less or equal



## 🔗 Logical Operators in Python

Logical operators are used to **combine conditional statements**.  
They return a **Boolean value** (`True` or `False`) depending on the logic applied.

### 📝 Example
```python
a = True
b = False

print(a and b)   # Logical AND
print(a or b)    # Logical OR
print(not a)     # Logical NOT
print(not b)     # Logical NOT

▶️ Output
False
True
False
True

✅ Key Points

and → Returns True only if both conditions are True

or → Returns True if at least one condition is True

not → Reverses the result (i.e., True becomes False, and False becomes True)

📊 Truth Table
a	b	a and b	a or b	not a	not b
True	True	True	True	False	False
True	False	False	True	False	True
False	True	False	True	True	False
False	False	False	False	True	True

## 🆔 Identifying the ID of a Variable

In Python, every variable is stored in memory, and each one has a **unique ID (identity)**.  
The built-in **`id()`** function returns the memory address (identity) of an object.

### 📝 Example
```python
name = "Imam Sanghaar"

print(id(name))   # Get the unique ID of the variable

▶️ Output (example)
140472518798640

(The exact number will vary depending on your system and runtime, because memory addresses change.)

✅ Key Points

id() returns a unique identifier for a variable’s object in memory.

If two variables hold the same immutable value (like numbers or strings), Python may optimize memory by making them share the same ID.


## 🧭 Conditionals: `if`, `elif`, `else`

This program asks the user for their age and tells them whether they are eligible for a CNIC.

### 📝 Code
```python
# If and Else and elif
Age = int(input("Enter Age:"))

if Age >= 19:
    print("you already have a CNIC")
elif Age == 18:
    print("you can   get CNIC")
else:
    print("You are not eligible for CNIC")

🔍 Step-by-step explanation

Prompt for input & convert to integer

Age = int(input("Enter Age:"))


input("Enter Age:") shows a prompt and returns what the user types as a string.

int(...) converts that string to an integer.

The result is stored in the variable Age.

First condition: age 19 or older

if Age >= 19:
    print("you already have a CNIC")


The if runs only if the condition is True.

Age >= 19 checks whether the user is 19 or older.

If true, it prints the message and skips the rest of the chain.

Second condition: exactly 18

elif Age == 18:
    print("you can   get CNIC")


elif means “else if”. It is checked only if the previous if was False.

Age == 18 checks for exactly 18.

If true, it prints the message and ends the chain.

Fallback for all other ages

else:
    print("You are not eligible for CNIC")


else runs when none of the above conditions were True.

Covers ages below 18 (and any other unexpected values).

▶️ Example runs

Input: 21 → Output: you already have a CNIC

Input: 18 → Output: you can get CNIC

Input: 16 → Output: You are not eligible for CNIC

🧠 Notes & tips

Indentation matters in Python: the code under each if/elif/else must be indented consistently.

If the user types non-numeric input (e.g., eighteen), int(...) will raise a ValueError. You can handle this with a try/except for a more user-friendly message.

## 📊 Find Your Percentage & Grade

This program takes the user’s percentage as input and assigns a grade based on their score.

### 📝 Code
```python
percentage = int(input("Enter your percentage:"))
print(percentage)
print(type(percentage))

if percentage >= 80 and percentage < 100:
    print("AI Grade")
elif percentage >= 70 and percentage < 80:
    print("A Grade")
elif percentage >= 60 and percentage < 70:
    print("B Grade")
elif percentage >= 50 and percentage < 60:
    print("C Grade")
else:
    print("Rickshaw Dilado")

🔍 Step-by-step Explanation

Take input from the user

percentage = int(input("Enter your percentage:"))


input() prompts the user for their percentage.

By default, input is a string, so we convert it to an integer using int().

The value is stored in the variable percentage.

Print the value and its type

print(percentage)
print(type(percentage))


Shows the entered number.

type(percentage) confirms the value is an integer.

Check grade conditions with if, elif, and else

if percentage >= 80 and percentage < 100:
    print("AI Grade")


If the percentage is between 80 and 99, the student gets AI Grade.

Notice the use of the logical operator and, which requires both conditions to be true.

elif percentage >= 70 and percentage < 80:
    print("A Grade")


If not the first case, but the score is 70–79, it prints A Grade.

elif percentage >= 60 and percentage < 70:
    print("B Grade")


For scores 60–69, the grade is B.

elif percentage >= 50 and percentage < 60:
    print("C Grade")


For scores 50–59, the grade is C.

else:
    print("Rickshaw Dilado")


If none of the above conditions match (i.e., score below 50 or invalid input), the student is given the funny message: "Rickshaw Dilado" 🚕 (meaning: no grade, you fail).

▶️ Example Runs

Input: 85 → Output: AI Grade

Input: 72 → Output: A Grade

Input: 65 → Output: B Grade

Input: 52 → Output: C Grade

Input: 40 → Output: Rickshaw Dilado

✅ Key Points

Use logical operators (and) to check score ranges.

Conditions are checked in order — once one matches, the rest are skipped.

Always use else as a fallback for unexpected or lower values.

## 💰 Pocket Money Example

This program checks how much pocket money you have and tells you whether you can buy a **Feastables** (a chocolate brand).

### 📝 Code
```python
pocket_money = int(input("Enter Amount:"))

if pocket_money > 1000:
    print("You can buy a Feastables")
elif pocket_money == 1000:
    print("Save more money to buy a Feastabes")
else:
    print("You cannot buy a Feastable")

🔍 Step-by-step Explanation

Take input from the user

pocket_money = int(input("Enter Amount:"))


The program asks the user how much money they have.

input() returns a string, so int() converts it into an integer.

The value is stored in the variable pocket_money.

Check if the money is greater than 1000

if pocket_money > 1000:
    print("You can buy a Feastables")


If the user has more than 1000, they can buy the chocolate.

Check if the money is exactly 1000

elif pocket_money == 1000:
    print("Save more money to buy a Feastabes")


If the user has exactly 1000, it suggests saving more money.

Else (for less than 1000)

else:
    print("You cannot buy a Feastable")


For less than 1000, the program tells the user they don’t have enough money.

▶️ Example Runs

Input: 1500 → Output: You can buy a Feastables

Input: 1000 → Output: Save more money to buy a Feastabes

Input: 700 → Output: You cannot buy a Feastable

✅ Key Points

if checks the first condition.

elif checks another condition if the first is False.

else is the fallback for all other cases.

Always use int() for numeric input when comparing numbers.


📝 Detailed Note on Nested If Elements
🔹 What is a Nested If?

A nested if is an if statement placed inside another if or elif block.

It allows you to check multiple layers of conditions and handle more specific cases.

Think of it like decision-making:

First, you decide a broad category (e.g., negative, zero, or positive).

Then, within a category, you make further decisions (e.g., if positive, check the exact range).

🔹 Code (Original Version)
num = int(input("Enter the value of number: "))
if (num < 0):
    print("Number is negative")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num == 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

🔹 Step-by-Step Execution

Take Input

input("Enter the value of number: ") prompts the user.

The value is converted into an integer using int().

Example: If the user enters 15, then num = 15.

Check if Negative

if (num < 0):
    print("Number is negative")


If the number is less than 0, it prints "Number is negative".

Example: num = -3 → Output: Number is negative.

Check if Positive

elif (num > 0):
    ...


If the number is greater than 0, it goes into another nested structure.

Example: num = 7 → The program will check further conditions.

Nested If inside Positive Numbers

If the number is between 1 and 10 (inclusive):

if (num <= 10):
    print("Number is between 1-10")


Example: num = 8 → Output: Number is between 1-10

If the number is greater than 10 but exactly equal to 20:

elif (num > 10 and num == 20):
    print("Number is between 11-20")


Example: num = 20 → Output: Number is between 11-20
❌ Problem: This condition only works for 20, not for 11–19.

Else (any number greater than 20):

else:
    print("Number is greater than 20")


Example: num = 50 → Output: Number is greater than 20

Check if Zero

else:
    print("Number is zero")


If the number is exactly 0, it prints Number is zero.

🔹 Example Runs
Input	Output
-5	Number is negative
0	Number is zero
5	Number is between 1-10
15	Number is greater than 20 (⚠ logical mistake, should be 11–20)
20	Number is between 11-20
100	Number is greater than 20
🔹 Problem in Logic

The condition:

elif (num > 10 and num == 20):


This only checks when num == 20.

It ignores 11–19.

For num = 15, it wrongly prints Number is greater than 20.

✅ Corrected Version
num = int(input("Enter the value of number: "))

if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
else:  # num > 0
    if num <= 10:
        print("Number is between 1-10")
    elif num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")

🔹 Why This Correction Works

Clear separation between negative, zero, and positive.

Correct ranges:

1–10

11–20

Greater than 20

🎯 Key Takeaways

Use nested if when you need more detailed decisions inside a broader decision.

Always check for logical coverage (make sure all possible inputs fall into the right category).

Use ranges (<=, >=) for cleaner conditions instead of combining multiple checks unnecessarily.

Basic Calculator:
# What it actually does you know that what calculator does but ypu can make it in python by using if-else-elif.
# this is the full code:
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
    print(num1+num2)
elif opr == "-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid operator")


print('''
+ Add
- Subtract
* Multiply
/ Divide
''')

This line of code prints that things that you write in it. Like I have written some operations in it which are used in the program. Let's see what functions are used in it:



<img width="246" height="768" alt="python_basics_flowchart" src="https://github.com/user-attachments/assets/5bbec034-e40d-4a53-af8a-affc2441a1de" />


🎯 Conclusion

This repository covers the fundamental building blocks of Python with simple and clear examples.
It’s a starting point for anyone who wants to learn programming from scratch.

👨‍💻 Author

Imam Sanghaar Chandio
Contact: 03441323835
