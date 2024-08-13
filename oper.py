# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a // b =", a // b)  # Floor Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print()

# Comparison Operators
x = 5
y = 8
print("Comparison Operators:")
print("x > y is", x > y)
print("x < y is", x < y)
print("x >= y is", x >= y)
print("x <= y is", x <= y)
print("x == y is", x == y)
print("x != y is", x != y)
print()

# Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q is", p and q)
print("p or q is", p or q)
print("not p is", not p)
print()

# Bitwise Operators
# m = 10  # 1010 in binary
# n = 4   # 0100 in binary
# print("Bitwise Operators:")
# print("m & n is", m & n)  # Bitwise AND
# print("m | n is", m | n)  # Bitwise OR
# print("m ^ n is", m ^ n)  # Bitwise XOR
# print("~m is", ~m)  # Bitwise NOT
# print("m << 2 is", m << 2)  # Bitwise Left Shift
# print("m >> 2 is", m >> 2)  # Bitwise Right Shift
# print()

# # Assignment Operators
# print("Assignment Operators:")
# r = 10
# print("r =", r)
# r += 5
# print("r += 5 -> r =", r)
# r -= 3
# print("r -= 3 -> r =", r)
# r *= 2
# print("r *= 2 -> r =", r)
# r //= 4
# print("r //= 4 -> r =", r)
# r %= 3
# print("r %= 3 -> r =", r)
# r **= 2
# print("r **= 2 -> r =", r)
# print()

# Identity Operators
# s1 = "hello"
# s2 = "world"
# print("Identity Operators:")
# print("s1 is s2 is", s1 is s2)
# print("s1 is not s2 is", s1 is not s2)
# print()

# Membership Operators
fruits = ["apple", "banana", "cherry"]
print("Membership Operators:")
print("'banana' in fruits is", 'banana' in fruits)
print("'orange' not in fruits is", 'orange' not in fruits)



# ans = 5 + 9 * 9 / 9 - 2 + 8 * 6
# print(ans)

# remainder = 11 % 3
# print(remainder)

# squared = 7 ** 8
# cubed = 5 ** 5
# print(squared)
# print(cubed)

# lotsofhellos = "Hello" " " * 10
# print(lotsofhellos)

# even_numbers = [2,4,6,8,2,2,45,6,77,7]
# odd_numbers = [1,3,5,7]
# all_numbers = even_numbers + even_numbers
# print(all_numbers)

# print(["ramesh", "50" ,"mahesh","rakesh","sukesh"] * 5)

x = object()
y = object()

# TODO: change this code
x_list = [x]*10 
y_list = [y]*10
big_list = x_list+y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")