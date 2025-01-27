### Program TO find the sum of elements in a list ###
# def sumList(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum


# list = [1,2,3,4,5,6,7,8,9,10]
# print(sumList(list))
    

######################################################################################################

# def findEvenNumbers(list):
#     even_numbers = []
#     for i in list:
#         if i % 2 == 0:
#             even_numbers.append(i)
#     return even_numbers

# list=[1,2,3,4,5,6,7,8,9,10]
# print(findEvenNumbers(list))

######################################################################################################

# def name(name):
#     def stars():
#         print("************")
#     stars()
#     print(name)
#     stars()
    
# name("Aaditya")

######################################################################################################

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# ######################################################################################################

# # write a function to find factorial of a number#

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# ######################################################################################################

# # write a function to find power of a number using recursion #

# def power(base, exp):
#     if exp == 0:
#         return 1
#     return base * power(base, exp - 1)

# print(power(2, 3))  # Output: 8
############################################################################################################

# # write a function to reverse a string using recursion #

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])

# print(reverse_string("hello"))  # Output: "olleh"


##########################################################################################################

# def sumList(list):
#     if len(list) == 1:
#         return list[0]
#     return list[0] + sumList(list[1:])

# list = [1,2,3,4,5,6,7,8,9,10]
# print(sumList(list))  # Output: 55


############################################################################################################

# def multiply(a, b):
#     if b == 0:
#         return 0
#     if b > 0:
#         return a + multiply(a, b - 1)
#     if b < 0:
#         return -multiply(a, -b)

# print(multiply(5, 3))  # Output: 15
# print(multiply(5, -3))  # Output: -15

#########################################################################################################


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#############################################################################################3

def printPrime(limit):
    def isPrime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    for i in range(limit+1):
        if isPrime(i):
            print(i)
            
printPrime(100)  # Output: 2, 3, 5, 7