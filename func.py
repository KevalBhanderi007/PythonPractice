# # Modify this function to return a list of strings as defined above
# def list_benefits():
#     return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# # Modify this function to concatenate to each benefit - " is a benefit of functions!"
# def build_sentence(benefit):
#     return f"{benefit} is a benefit of functions!"


# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits()
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))


# name_the_benefits_of_functions()

def calculate_stats(numbers):
    mean = sum(numbers) / len(numbers)
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        median = sorted_numbers[n//2]
    return mean, median

# Using the function
data = [1, 2, 3, 4, 5,6]
mean_value, median_value = calculate_stats(data)
print(f"Mean: {mean_value}, Median: {median_value}")
# Output: Mean: 3.0, Median: 3


# def factorial(n):
#     """This function calculates the factorial of a number using recursion."""
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Using the recursive function
# result = factorial(5)
# print(f"Factorial of 5 is: {result}"))


def fact(n):
    if n == 0 or  n ==1 :
        return 1
    else :
        return n * fact(n-1)

print(fact(5)) 
         