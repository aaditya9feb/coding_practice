# Program to swap two numbers without using a third variable

# Function to swap two numbers
def swap(a, b):
    print("Before swapping: a =", a, "b =", b)
    a = a + b
    b = a - b
    a = a - b
    print("After swapping: a =", a, "b =", b)

# Example usage
x = 5
y = 10
swap(x, y)