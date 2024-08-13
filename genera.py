# import random

# def lottery():
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#         yield random.randint(1, 40)

#     # returns a 7th number between 1 and 15
#     yield random.randint(1, 15)

# for random_number in lottery():
#        print(f"And the next number is...{random_number} !") 
    #   print("And the next number is... %d!" %(random_number))


def square_generator(limit):
    num = 1
    while num <= limit:
        yield num * 5 * 5
        num += 1


for value in square_generator(15):
    print(value)

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n) 
        counter += 1
        if counter == 10:
            break

# or 

def fibonacci():
    a, b = 0 , 1 
    while True:
        yield a        
        a, b = b , a + b
        
genrate = fibonacci()

for i in range(20):
    print(next(genrate))
