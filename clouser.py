# def outer_function(outer_variable):
#     def inner_function():
#         print(f'Accessing variable from outer function: {outer_variable}')

#     return inner_function

# # Example usage:
# closure_example = outer_function("Hello, closure!")

# # Calling the closure
# closure_example()

# def multiplier_of(n):
#     def multiplier(number):
#         return number*n
#     return multiplier

# multiplywith5 = multiplier_of(5)
# print(multiplywith5(9))


# def addition (a,b,c ,d):
#     def add(num):
#         return num+a+b+c+d
#     return add

# result = addition(1,2,3,4)
# print(result(5))

# def transmit_to_space(message):
# #   "This is the enclosing function"
#   def data_transmitter():
#     #   "The nested function"
#       print(message)
#   return data_transmitter

# fun2 = transmit_to_space("Burn the Sun!")
# fun2()


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def type_check(correct_type):
    def check(old_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])    

