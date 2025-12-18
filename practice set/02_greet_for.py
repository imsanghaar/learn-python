# l = ["Sanghaar", "Ali", "Naveed", "Sherry"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello{name}")

# n = int(input("Enter a number: "))

# i = 1
# while(i<11):
#     print(f"{n} x {i} = {n * i}")
#     i +=1



# lets check if the number is prime or not
# n = int(input("Enter a number: "))

# for i in range(2, n):
#     if(n%1)== 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")




# sum of n natural number using while loop

# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while(i<=n):
#     sum +=i
#     i +=1
# print(f"The sum of first {n} natural number is {sum}")


# FAcotrial sum using while loop

# n = int(input("Enter a number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i
# print(f"The factorial of {n} is {product}")


# Printing Star  Pattern with 3 space

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " *(n -i ), end="")
    print("*"* (2*i-1), end="")
    print(" ")