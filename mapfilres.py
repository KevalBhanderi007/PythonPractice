num = [1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda x : x ** 2,num))

print(square)

odd = list(filter(lambda x : x % 2 != 0, num ) )

print(odd)

from functools import reduce

sum = reduce(lambda x,y : x+y , num ,10)

print(sum)

def ctof(celsius):
    return (celsius * 9/5) + 32

cetem = [0, 10, 20, 30, 40]

fertem = list(map(ctof, cetem))
print(fertem)


words = ["hello", "world", "python", "programming"]

capitalized_words = list(map(lambda x: x.capitalize(), words))
capitalized_words = list(map(str.upper, words))
print(capitalized_words) 

words = ["apple", "banana", "grape", "kiwi", "orange"]

long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)  

numbers = [3, 8, 1, 5, 14, 4]

# Using reduce to find the maximum number
max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(max_number)  

fruits = ["apple", "banana", "cherry"]
prices = [1.2, 3.5, 2.8]

# Using zip to combine fruits and their prices
fruit_prices = list(zip(fruits, prices))
print(fruit_prices)


dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
