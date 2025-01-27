# # # # Using While loop to print numbers from 1 to 10 # # # # #
# i=1
# while(i<=10):
#     print(i)
#     i+=1
# print("Done")
##########################################################################################
# # # # Using while loop to print numbers from 10 to 5 # # # # #
# i=10
# while(i>=5):
#     print(i)
#     i-=1
# print("Done")
##########################################################################################

# # # # Using while loop to print the tableof 5# # # # #
# i = 1
# num=int(input("Enter a number to print its multiplication table: "))
# while(i<=10):
#     print(f"{num} x {i} = {num * i}")
#     i+=1
# print("Done")

##########################################################################################

# # # # # Print the sum of numbers using the while loop # # # # # #
# sum=0
# i=1
# while(1<=10):
#     sum=sum+i
#     i+=1
# print(f"The sum of numbers from 1 to 10 is {sum}")
# print("Done")
##########################################################################################

# # # # # Find factorial of a number using while loop # # # # # #

# num = int(input("Enter a number to find its factorial: "))
# fact = 1
# i = 1
# while(i<=num):
#     fact*=i
#     i+=1
# print(f"The factorial of {num} is {fact}")
# print("Done")

##########################################################################################

### Add the numbers given by User using while loop###

# sum=0
# while True:
#     num = int(input("Enter a number: "))
#     sum+=num
#     choice = input("Do you want to continue? (y/n): ")
#     if choice.lower() != 'y':
#         break
# print(f"The sum of numbers is {sum}")
# print("Done")

##########################################################################################

#### Add the digits of a number using while loop###

# num = int(input("Enter a number: "))
# sum = 0
# while num>0:
#     sum+=num%10
#     num//=10
# print(f"The sum of digits is {sum}")
# print("Done")

##########################################################################################

#### Using while loop to reverse a number and check if it is a palindrone###

# num = int(input("Enter a number: "))
# rev = 0
# temp = num
# while num>0:
#     rev = rev*10 + num%10
#     num//=10
# print(f"The reverse of the number is {rev}")
# if temp == rev:
#     print("The number is a palindrome")
# else:
#     print("The number is not a palindrome")
# print("Done")

##########################################################################################

# #### Count the number of digits in a number using while loop###
# count = 0
# num = int(input("Enter a number: "))
# rev = 0
# while num>0:
#     count+=1
#     num//=10
# print(f"The number of digits id {count}")
# print("Done")

##########################################################################################

### Check if the number is Armstrong number using while loop###

# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while num>0:
#     digit = num%10
#     sum+=digit**len(str(temp))
#     num//=10
# if temp == sum:
#     print("The number is an Armstrong number")
# else:
#     print("The number is not an Armstrong number")
# print("Done")

##########################################################################################

# def checkArmstrong(num):
#     temp = num
#     sum = 0
#     while num>0:
#         digit = num%10
#         sum+=digit**len(str(temp))
#         num//=10
#     if temp == sum:
#         return True
#     else:
#         return False

# def main():
#     i=1
#     while(i<10000):
#         i+=1
#         if checkArmstrong(i):
#             print(i)

# if __name__ == "__main__":
#     main()    
    
##########################################################################################

# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# power=len(str(temp))
# while num>0:
#     digit = num%10    
#     sum+=digit**power
#     power-=1
#     num//=10
    
# if temp == sum:
#     print("The number is an Special number")
# else:
#     print("The number is not an Special number")
    
################################################################################################

####Use while loop to check if number is prime######

# num = int(input("Enter a number: "))
# i=2
# while i<num:
#     if num%i==0:
#         print("The number is not a prime number")
#         break
#     i+=1
# else:
#     print("The number is a prime number")
    
################################################################################################

# limit = int(input("Enter the limit: "))
# num = 2
# while num <= limit:
#     is_prime = True
#     i = 2
#     while i <= num // 2:
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     if is_prime:
#         print(num)
#     num += 1
    
################################################################################################

# def add(a,b):
#     return a+b

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)

# print(add(2,3))

#######################################################################################################

# def print_armstrong_numbers(limit):
#     def is_armstrong(num):
#         temp = num
#         sum = 0
#         power = len(str(temp))
#         while num > 0:
#             digit = num % 10
#             sum += digit ** power
#             num //= 10
#         return temp == sum

#     for num in range(1, limit + 1):
#         if is_armstrong(num):
#             print(num)

# print_armstrong_numbers(100000)

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
