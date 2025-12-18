#  Lists Methods

# append 
# insert
# pop
# Remove
# len 
# sort 
# reverse
# index


# Append Method
print("Append Method")
numbers_list = [1,2,3,4,6,7,8]
print("List before append", numbers_list) 
numbers_list.append(9)
numbers_list.append(10) # Append means in english at the end and add the given 
numbers_list.append(11)
print("List after append", numbers_list)

# Insert Method
print("Insert Method")
number = [1,2,3,4,6,7,8]
print("List before insert", number)
number.insert(9,10) # insert means to add the given element at the given index
print("List after insert", number)

#  pop
print("Pop Method")
p = [1,2,3,4,5]
print("List before pop", p)
print("The number which popped is: ", p.pop(2)) # removes the element at index 2
print("List after pop", p)

# remove
print("Remove Method")
ls = [1,2,3,4,6,7]
print("List before remove", ls)
ls.remove(2) # removes the element with value 2
print("List after remove", ls)


#  len (length)
print("Len(Length) Method")
num = [1,2,3,6,8] # length = how many elements are there in the list = 5
print("Before the length", num ) 
print("The length of num is: ", len(num)) 

# Sort
print("Sort Method")
l1 = [1,100,2000,4,2,5,7]
print("List before sort", l1)
l1.sort() # sorts the list in ascending order
print("List after sort", l1)

# Reverse
print("Reverse Method")
l2 = [10,30,50,80,120,170]
print("List before reverse", l2)
l2.reverse() # reverses the order of elements in the list
print("List after reverse", l2)

#Index
print("Index Method")
l3 = ["Sanghaar", "Larkana", "SZABIST"]
l3.index("Sanghaar") # returns the index of the element "Sanghaar"
print(l3)