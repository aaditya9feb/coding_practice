
######################################################################################################################
# # Function to calculate grade based on percentage
# def calculate_grade(percentage):
#     if percentage >= 90:
#         return 'A'
#     elif percentage >= 80:
#         return 'B'
#     elif percentage >= 70:
#         return 'C'
#     elif percentage >= 60:
#         return 'D'
#     else:
#         return 'F'

# # Function to calculate percentage from marks
# def calculate_percentage(marks):
#     return sum(marks) / len(marks)

# # Main function to get user input and calculate grade
# def main():
#     marks = []
#     for i in range(1, 4):
#         mark = float(input(f"Enter marks for subject {i}: "))
#         marks.append(mark)
    
#     percentage = calculate_percentage(marks)
#     grade = calculate_grade(percentage)
    
#     print(f"Percentage: {percentage:.2f}%")
#     print(f"Grade: {grade}")

# if __name__ == "__main__":
#     main()
    
###################################################################################################################

###Clacluator using if else###
# def add(num1, num2):
#      return num1 + num2

# def subtract(num1, num2):
#         return num1 - num2

# def multiply(num1, num2):
#         return num1 * num2
# def divide(num1, num2):
#         return num1 / num2

# def main():
#     print("Enter the first number: ")
#     num1 = int(input())
#     print("Enter the second number: ")
#     num2 = int(input())
#     print("Enter the operation: ")
#     operation = input()
#     if operation == '+':
#         print(add(num1, num2))
#     elif operation == '-':
#         print(subtract(num1, num2))
#     elif operation == '*':
#         print(multiply(num1, num2))
#     elif operation == '/':
#         print(divide(num1, num2))
#     else:
#         print("Invalid operation")

# if __name__ == "__main__":
#     main()
    

###############################################################################################
# # Function to determine the quadrant of a point
# def find_quadrant(x, y):
#     if x > 0 and y > 0:
#         return "Quadrant I"
#     elif x < 0 and y > 0:
#         return "Quadrant II"
#     elif x < 0 and y < 0:
#         return "Quadrant III"
#     elif x > 0 and y < 0:
#         return "Quadrant IV"
#     elif x == 0 and y != 0:
#         return "On the Y axis"
#     elif y == 0 and x != 0:
#         return "On the X axis"
#     elif x==0 and y==0:
#         return "Origin"
#     else:
#         return "Invalid Input"

# def main():
#     x = float(input("Enter the x-coordinate: "))
#     y = float(input("Enter the y-coordinate: "))
#     quadrant = find_quadrant(x, y)
#     print(f"The point ({x}, {y}) is in {quadrant}")

# if __name__ == "__main__":
#     main()
    
    
    

##############################################################################################3


# # Function to print the multiplication table of a given number
# def print_table(number):
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")

# def main():
#     number = int(input("Enter a number to print its multiplication table: "))
#     print_table(number)

# if __name__ == "__main__":
#     main()

#############################################################################################
##Function to find the factorial of a number using loop###

# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact

# def main():
#     num = int(input("Enter a number to find its factorial: "))
#     print(f"The factorial of {num} is {factorial(num)}")
    
# if __name__ == "__main__":
#     main()
###########################################################################################    
## function to find the sum of numbers using loops###

# def sumNum(x):
#     sum=0
#     for i in range(x+2):
#         sum+=i
#     return sum

# def main():
#     x = int(input("Enter a number: "))
#     print(f"The sum of numbers from 1 to {x} is {sumNum(x)}")

# if __name__ == "__main__":
#     main()
########################################################################################## 
# # Function to check odd and even numbers in a list
# def check_odd_even(numbers):
#     odd_numbers = []
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     return odd_numbers, even_numbers

# def main():
#     numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
#     odd_numbers, even_numbers = check_odd_even(numbers)
#     print(f"Odd numbers: {odd_numbers}")
#     print(f"Even numbers: {even_numbers}")

# if __name__ == "__main__":
#     main()
    
#####################################################################################################3

# # Function to check if the length of strings in a list is greater than 4
# def check_string_length(strings):
#     result = []
#     for string in strings:
#         if len(string) > 4:
#             result.append(string)
#     return result

# def schecStr(strings):
#     result=[]
#     for i in strings:
#         if (type(i)==str):
#             result.append(i)
#     return result

# def main():
#     strings = input("Enter a list of strings separated by space: ").split()
#     long_strings = check_string_length(strings)
#     print(f"Strings with length greater than 4: {long_strings}")
                      

# if __name__ == "__main__":
#     main()

##############################################################################################################

# # Function to print Fibonacci series up to n terms
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
#     print()

# def main():
#     n = int(input("Enter the number of terms for Fibonacci series: "))
#     fibonacci(n)

# if __name__ == "__main__":
#     main()
#################################################################################################################

# for i in range(5):
#     for j in range(5):
#         print(j,end=" ")
#     print()


# for i in range(4):
#     for j in range(i+1):
#         print(chr((65+j)),end=" ")
#     print()
    
# counter=1
# for i in range(4):
#     for j in range(i+1):
#         print(counter,end=" ")
#         counter +=1
#     print()
    
# counter=1
# for i in range(4):
#     for j in range(i+1):
#         print(chr((counter+64)),end=" ")
#         counter +=1
#     print()
############################################################################################################33

##Sum of length of string in a list##
# def sumStrings(strings):
#     sum=0
#     for i in strings:
#         if type(i)==str:
#             sum= sum+ len(i)
#     return sum

# def main():
#     strings = input("Enter a list of strings separated by space: ").split()
#     print(f"Sum of the lengths of strings: {sumStrings(strings)}")    
    
# if __name__=="__main__":
#     main()

##############################################################################################################

# sum=0
# l1=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l1:
#     for j in i:
#         sum=sum+j
# print(sum)

# while(1==1):
#     print("Infinite loop")

##################################################################################################################

