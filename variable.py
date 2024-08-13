# Integer Variable
age = 25

# Float Variable
pi = 3.14

# String Variable
name = "Alice"

# Boolean Variable
is_adult = True

# List Variable (a collection of mixed items)
numbers = [1, 2, 3, 4, 5]

# Tuple Variable (similar to lists but immutable)
coordinates = (10, 20)

# Dictionary Variable (key-value pairs)
person = {'name': 'Bob', 'age': 30}

# Set Variable (unordered collection of unique items)
unique_numbers = {1, 2, 3, 4, 5}

# None Variable (represents the absence of a value)
result = None

# Printing variables to demonstrate
print("Age:", age)
print("Pi:", pi)
print("Name:", name)
print("Is Adult:", is_adult)
print("Numbers:", numbers)
print("Coordinates:", coordinates)
print("Person:", person)
print("Unique Numbers:", unique_numbers)
print("Result:", result)


# mystring = "hello"
# myfloat = 10.0
# myint = 20

# # testing code
# if mystring == "hello":
#     print("String: %s" % mystring)
# if isinstance(myfloat, float) and myfloat == 10.0:
#     print("Float: %f" % myfloat)
# if isinstance(myint, int) and myint == 20:
#     print("Integer: %d" % myint)


# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# print(mylist[0]) # prints 1
# print(mylist[1]) # prints 2
# print(mylist[2]) # prints 3

# # prints out 1,2,3
# for x in mylist:
#     print(x)

sub = ["eng","guj","hin","paint"]
# sub.append("eng")
# sub.append("guj")
# sub.append("hin")
# sub.append("math")
# sub.append("paint")

# print(sub[4])

for x in sub:
    print(x)


numbers = [1,2,3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = "eric"


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
  



# List of Numbers
numbers = [1, 2, 3, 4, 5]

# List of Strings
fruits = ["apple", "banana", "cherry"]

# List of Mixed Data Types
mixed_list = [10, "hello", 3.14, True]

# Nested Lists (List of Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Empty List
empty_list = []

# Accessing Elements in a List
print(fruits[0])  # Output: "apple"

# Modifying Elements in a List
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]

# Appending to a List
fruits.append("cherry")
print(fruits)  # Output: ["apple", "banana", "cherry"]

# Slicing a List
print(numbers[1:4])  # Output: [2, 10, 4]

# List Comprehension
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 100, 16, 25]
