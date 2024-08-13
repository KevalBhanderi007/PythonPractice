# todo = [2, 3, 5, 7,"raehjs","edjvz",56]
# for element in todo:
#     print(todo)


# for x in range(5):
#     print(x)

# # Prints out 3,4,5
# for x in range(3, 6):
#     print(x)

# # Prints out 3,5,7
# for x in range(5, 15, 6): 
#     print(x)

# count = 0
# while count < 5:
#     print(count)
#     count += 6

# int = 0
# while int <=10:
#     print(f"5 * {int}   = {int*5} ")
#     int += 1    
# else :
#     print("\t") 
  
   
# for i in range(1,11):
    
#     print(f"18 * {i}   = {i*18}") 
  
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 10:
#         break

# Prints out only odd numbers - 1,3,5,7,9
# for x in range(1,51):
#     # Check if x is even
#     if x % 2 == 0 or x % 3 == 0:
#         continue # like skipping
#     print(x)


# Example of using enumerate() to access index and value
# fruits = ["apple", "banana", "cherry","fjxg","rsesdyyg"]

# for index, fruit in enumerate(fruits):
#   print(f"index {index} : {fruit}")  


# Example of an infinite loop (use with caution!)
while True:
    user_input = input("Enter a number (type 'exit' to quit): ")
    
    if user_input == 'exit':
        break
    
    number = int(user_input)
    print(f"cube of {number} is {number ** 3}")

