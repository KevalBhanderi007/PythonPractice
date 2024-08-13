# name = int(input("enter your name :" ))
# print("Hello, %s!" % name)



# name = "dilip"
# marks = 456
# float = 2.23
# print("%s your %d and %f marks very different." % (name, marks,float))

# num = 255
# formatted_lower = "{:x}".format(num)  # Lowercase hexadecimal
# formatted_upper = "{:X}".format(num)  # Uppercase hexadecimal
# print(formatted_lower)  # Output: ff
# print(formatted_upper)  # Output: FF

# This prints out: A list: [1, 2, 3]
# mylist = [1,2,3]
# print("A list: %s" % mylist)


# data = ("John", 53.44)
# format_string = "Hello %s. Your current balance is $%s."

# print(format_string % data)

# article = "Asyoucanb see , the first thing you learned was printing a simple sentence. This sentence was stored by Python as a string. However, instead of immediately printing strings out, we will explore the various things you can do to them. You can also use single quotes to assign a string. However, you will face problems "
# afewwords = article.split(" ")

# print(article.upper())
# print(article.startswith("As"))
# print(article.endswith("problems "))

# print(article[1:22])

#  [start:stop:step].
# print(article[-3:-1])

# s = "Hey there! what shou"
# # Length should be 20
# print("Length of s = %d" % len(s))

s = "Hey thera! what shou"
# Length should be 20
# print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
# print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
# print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))



# Define a string
my_string = "Hello, World!"

# Print the string
print(my_string)

# String length
print("Length of the string:", len(my_string))

# Accessing characters in a string
first_char = my_string[0]
print("First character:", first_char)

# Slicing strings
substring = my_string[7:12]
print("Substring:", substring)

# Concatenation
new_string = my_string + " Welcome!"
print("Concatenated string:", new_string)

# String methods
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Splitting the string:", my_string.split(","))
print("Replacing:", my_string.replace("Hello", "Hi"))

# Checking for substrings
if "World" in my_string:
    print("Found 'World' in the string")

# String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)
