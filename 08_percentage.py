# Find your percentage
percentage = int(input("Enter your percentage:"))
print(percentage)
print(type(percentage))

if percentage >= 80 and percentage < 100:
    print("AI Grade")
elif percentage >= 70  and percentage < 80:
    print("A Grade")
elif percentage >= 60 and percentage < 70:
    print("B Grade")
elif percentage >= 50 and percentage < 60:
    print("C Grade")
else:
    print("Rickshaw Dilado")