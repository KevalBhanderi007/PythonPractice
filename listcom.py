# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_lengths = []
# for word in words:
#       if word != "the":
#           word_lengths.append(len(word))
# print(words)
# print(word_lengths)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
word_lengths = [len(word) for word in words if word != "the"]

print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = [float(x) for x in numbers if x > 0]
print(newlist)

# Using a list comprehension to square numbers from 0 to 9
squares = [x * x for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using a list comprehension to filter out odd numbers from a range
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

matrix = [[[x**z for z in range(1,4)] for y in range(1, 4)] for x in range(1, 4)]
print(matrix)