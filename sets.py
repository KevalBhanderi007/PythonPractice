# a = set(["Jake", "John", "Eric"])
# b = set(["John", "Jill"])

# # same in both
# print(a.intersection(b)) 
# print(b.intersection(a))

# # differnt in both and combine
# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))

# # differnt in both
# print(a.difference(b))
# print(b.difference(a))

# # join both
# print(a.union(b))

# Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {'apple', 'banana', 'cherry'}

# Sets with mixed types
set3 = {1, 'apple', 3.14, True}

# Adding elements to a set
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

# Attempting to add duplicate elements
set1.add(2)
print(set1)  # Output: {1, 2, 3, 4, 5, 6} (still remains the same, as 2 was already there)

# Removing elements from a set
set2.remove('banana')
print(set2)  # Output: {'apple', 'cherry'}

# Checking membership in a set
print('apple' in set2)  # Output: True
print('orange' in set2)  # Output: False

# Iterating over a set
for element in set1:
    print(element)

# Set operations
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Union of sets
union_set = set_A | set_B
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection of sets
intersection_set = set_A & set_B
print(intersection_set)  # Output: {4, 5}

# Difference of sets
difference_set = set_A - set_B
print(difference_set)  # Output: {1, 2, 3}

# Symmetric Difference of sets
symmetric_difference_set = set_A ^ set_B
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}
