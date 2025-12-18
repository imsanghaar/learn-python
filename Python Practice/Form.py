# Python - Practice

print("Quest Academy - A Place where Quality - Excellence - Success meets Talent")
print("Please fill the form below:\n")

# Collect form data
name = input("Full Name: ")
fname = input("Father's Name: ")
email = input("Email Address: ")
sex = input("Male/Female: ")
dob = input("Date Of Birth (Ex. DD/MM/YYYY): ")
age = int(input("Age: "))
cnic = input("CNIC: ")
phone = input("Phone Number: ")
nationality = input("Nationality: ")
religion = input("Religion: ")
address = input("Address: ")
degree = input("Qualification: ")
skills = input("Skills (if more than one, then write after comma): ").lower()
job = input("Applied for teacher of (Python/Prompt Engineer/Web Developer): ").lower()
experience = input("Experience (in years or none): ").lower()
salary = input("Expected Salary: ")
workplace = input("Workplace (On-site/Remote/Hybrid): ").lower()

print("\n--- Checking your information against our requirements ---\n")

# Job Requirements check using if-elif-else
if "python" in skills or "prompt engineer" in skills or "web developer" in skills or "ai" in skills:
    print("Your skills match our requirements.")
elif age >= 25:
    print("Your age meets our policy.")
elif degree == "intermediate" or degree == "bachelor" or degree == "masters" or degree == "graduation":
    print("Your qualification is acceptable.")
elif nationality == "pakistani":
    print("You are a Pakistani citizen.")
elif job == "python" or job == "prompt engineer" or job == "web developer":
    print("You have applied for the position of", job)
elif experience == "2 years" or experience == "3 years" or experience == "4 years" or experience == "5 years":
    print("Your experience is suitable for our requirements.")
else:
    print("Your data does not match our requirements.")

# Print the full form summary
print("\n--- Applicant Form Summary ---")
print("Name:", name)
print("Father's Name:", fname)
print("Email:", email)
print("Gender:", sex)
print("Date of Birth:", dob)
print("Age:", age)
print("CNIC:", cnic)
print("Phone:", phone)
print("Nationality:", nationality)
print("Religion:", religion)
print("Address:", address)
print("Qualification:", degree)
print("Skills:", skills)
print("Applied for:", job)
print("Experience:", experience)
print("Expected Salary:", salary)
print("Workplace:", workplace)

print("\nThanks", name, "for filling the form. You will be informed via call or email if shortlisted.")
