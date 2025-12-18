# Files Operation or File Handling

# To read, write, update files is called file handling
# Syntax of file handling
#    file name       w -> write
file = open("example.txt", "w") 
# With this method we can write in the file we gave
file.write("Hello, My name is Sanghaar and I am a student at PIAIC")
file.close()

# file2 = open("example.txt", "r") # This will open the file we wrote previously
# read = file2.read()             # This is a variable set to read the file
# print("Response: ", read)             # This will print the content inside the file
# file2.close                     # This will close the file


# file3 = open("example.txt", "w")
# file3.write("I am Student at NED University")
# file3.close()

# file3 = open("example.txt", "r")
# res = file3.read()
# print("Content: ", res)
# file3.close()


#append is also used to add something in the file
# with -> we don't have problem if we close or not

with open("example.txt", "r") as file100:
    result = file100.read()
    print("result>>>",result)

