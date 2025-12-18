# Table Generator in Python

print("=== Multiplication Table Generator ===")

# Take input from user for the number
num = int(input("Enter the number for the table: "))

# Take input for how long the table should go
limit = int(input("Enter how long you want the table (e.g., 10): "))

print(f"Multiplication Table of {num} up to {limit}: ")

# Generate and display the table
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
