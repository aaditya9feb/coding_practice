# Program to swap two numbers

# Function to swap two numbers
def swap_numbers(a, b):
    a, b = b, a
    return a, b

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Swap the numbers
num1, num2 = swap_numbers(num1, num2)

# Display the result
print(f"After swapping: First number = {num1}, Second number = {num2}")