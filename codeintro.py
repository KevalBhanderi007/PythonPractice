# Example of using various Python introspection functions and attributes

help()
help(list)

# dir()
print("\nAttributes and methods of list:")
print(dir(list))

# hasattr()
class MyClass:
    def __init__(self):
        self.x = 10
    
    def my_method(self):
        print("Hello")

obj = MyClass()
print("\nChecking attributes and methods of MyClass:")
print(hasattr(obj, 'x'))         # True
print(hasattr(obj, 'my_method')) # True

# id()
x = 42
print("\nID of x:", id(x))

# type()
print("\nType of x:", type(x))   # <class 'int'>

# repr()
print("\nRepresentation of x:", repr(x))  # '42'

# callable()
def my_func():
    print("Hello")

print("\nIs my_func callable?", callable(my_func))  # True

# issubclass()
class A:
    pass

class B(A):
    pass

print("\nIs B a subclass of A?", issubclass(B, A))  # True

# isinstance()
print("\nIs x an instance of int?", isinstance(x, int))  # True

# __doc__
def my_func():
    """This function does something."""
    pass

print("\nDocstring of my_func:", my_func.__doc__)  # This function does something.

# __name__
if __name__ == "__main__":
    print("\nThis script is being run directly.")
