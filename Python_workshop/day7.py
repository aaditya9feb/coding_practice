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

######################################################################################################

# write a function to find factorial of a number#

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))