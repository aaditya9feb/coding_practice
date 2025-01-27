# Pritinting Hello World

#print("Hello World")

#Write a program to Find the Average of Three Numbers

"""a = int(input("Enter the first number:  "))
b = int(input("Enter the second number: "))
c = int(input("Enter the thired number: "))

avg = a + b + c / 3

""" """print("The average of the three numbers is: ", avg)"""

#Write a program to Calculate Sum of 5 Subjects and Find Percentage

"""a = int(input("Enter the first subject marks:  "))
b = int(input("Enter the second subject marks: "))
c = int(input("Enter the third subject marks: "))
d = int(input("Enter the fourth subject marks: "))
e = int(input("Enter the fifth subject marks: "))

sum = a + b + c + d + e
percentage = (sum / 500) * 100

print("The percentage of the five subjects is: ", percentage)
"""

#Write a program to Calculate Area of Circle.

"""r = float(input("Enter the radius of the circle : "))
area = 3.14 * r * r

print(f"The area of the circle is {area}")"""

#Write a program to Calculate Area of Rectangle
"""
len = float(input("Enter the length of the rectangle : "))
brd = float(input("Enter the breadth of the reactangle : "))

area = len * brd
print("The area of the rectangle is: ", area)
"""

#Write a program to Calculate Area of Square

"""side = float(input("Enter the side of the square: "))
area =  side * side

print("The area of the given square is: ", area)
"""

#Write a program to Calculate Area and Circumference of Circle

"""r = float(input("Enter the radius of the circle : "))

area = 3.14 * r * r
perimeter = 2 * 3.14 * r

print("The perimeter of the circle is {} and the area of the circle is {}.".format(perimeter, area))
"""

#Write a program to Calculate Area of Scalene Triangle.

"""s1 = float(input("Enter the first side of the triangle: "))
s2 = float(input("Enter the second side of the triangle: "))
s3 = float(input("Enter the third side of the triangle: "))

s = (s1 + s2 + s3) / 2

area = (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5

print("The area of the scalene triangle is: ", area)
"""

# Write a program to Calculate Area of Right angle Triangle
"""base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = 0.5 * base * height

# Display the area
print(f"The area of the right angle triangle is: {area}")"""

#Write a program to find the area of trapezium

"""a = float(input("Enter the length of the first parallel side: "))   
b = float(input("Enter the length of the second parallel side: "))
h = float(input("Enter the height of the trapezium: "))

area = 0.5 * (a + b) * h

print("The area of the trapezium is: ", area)
"""

#Write a program to find the area of rhombus.
"""diagonal1 = float(input("Enter the length of the first diagonal: "))
diagonal2 = float(input("Enter the length of the second diagonal: "))

area = (diagonal1 * diagonal2) / 2

print("The area of the rhombus is: {}".format(area))
"""

# Write a program to find the area of parallelogram.

"""base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

area = base * height

print("The area of the parallelogram is: {}".format(area))

"""

# Write a program to find the volume and surface area of cube.
"""side_length = float(input("Enter the side length of the cube: "))

volume = side_length ** 3
surface_area = 6 * (side_length ** 2)

print(f"The volume of the cube is: {volume}")
print(f"The surface area of the cube is: {surface_area}")
"""

# Write a program to find the volume and surface area of cuboids.

"""length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

volume = length * width * height
surface_area = 2 * (length * width + width * height + height * length)

print(f"Volume of the cuboid: {volume}")
print(f"Surface area of the cuboid: {surface_area}")"""

#import math

# Write a program to find the volume and surface area of cylinder.

"""radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

volume = math.pi * radius ** 2 * height
surface_area = 2 * math.pi * radius * (radius + height)

print(f"Volume of the cylinder: {volume:.2f}")
print(f"Surface area of the cylinder: {surface_area:.2f}")

"""

#import math

"""# Write a program to find the surface area and volume of a cone
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

slant_height = math.sqrt(radius**2 + height**2)
surface_area = math.pi * radius * (radius + slant_height)
volume = (1/3) * math.pi * radius**2 * height

print("Surface Area of the cone: {}".format(surface_area))
print("Volume of the cone: {}".format(volume))
"""

# Write a program to find the surface area and volume of a cone

"""radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

pi = 3.14
slant_height = (radius**2 + height**2)**0.5
surface_area = pi * radius * (radius + slant_height)
volume = (1/3) * pi * radius**2 * height

print("The surface area of the cone is {:.2f}".format(surface_area))
print("The volume of the cone is {:.2f}".format(volume))
"""

#import math

#Write a program to find the volume and surface area of sphere.
"""radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

print("Volume of the sphere: {:.2f}".format(volume))
print("Surface area of the sphere: {:.2f}".format(surface_area))"""

#import math
"""# Write a program to find the perimeter of a circle, rectangle and triangle

# Perimeter of a circle
radius = float(input("Enter the radius of the circle: "))
circle_perimeter = 2 * math.pi * radius
print(f"The perimeter of the circle is: {circle_perimeter}")

# Perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_perimeter = 2 * (length + width)
print(f"The perimeter of the rectangle is: {rectangle_perimeter}")

# Perimeter of a triangle
side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
triangle_perimeter = side1 + side2 + side3
print(f"The perimeter of the triangle is: {triangle_perimeter}")
"""

# Write a program to Compute Simple Interest.

"""# Input principal, rate and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

simple_interest = (principal * rate * time) / 100

print(f"The simple interest is: {simple_interest}")"""

# Write a program to Convert Fahrenheit temperature in to Celsius.
"""fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)
"""

#Write a program to swap the values of two variables.

"""a = 5
b = 10

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)"""


'''
# Gravitational force calculation between two objects

def gravitational_force(m1, m2, r):
    G = 6.67430e-11  # gravitational constant in m^3 kg^-1 s^-2
    force = G * (m1 * m2) / (r ** 2)
    return force

# Example usage
mass1 = 5.972e24  # mass of the Earth in kg
mass2 = 7.348e22  # mass of the Moon in kg
distance = 3.844e8  # distance between Earth and Moon in meters

force = gravitational_force(mass1, mass2, distance)
print(f"The gravitational force between the objects is {force} N")

'''

'''

# Swapping two values with a third variable
a = 5
b = 10

# Using a third variable
temp = a
a = b
b = temp

print(f"After swapping with third variable: a = {a}, b = {b}")

# Swapping two values without a third variable
a = 5
b = 10

# Without using a third variable
a, b = b, a

print(f"After swapping without third variable: a = {a}, b = {b}")

'''
'''

# Arithmetic operations on variables
x = 8
y = 3

# Addition
addition = x + y
print(f"The addition of {x} and {y} is {addition}")

# Subtraction
subtraction = x - y
print(f"The subtraction of {y} from {x} is {subtraction}")

# Multiplication
multiplication = x * y
print(f"The multiplication of {x} and {y} is {multiplication}")

# Division
division = x / y
print(f"The division of {x} by {y} is {division}")

# Floor Division
floor_division = x // y
print(f"The floor division of {x} by {y} is {floor_division}")

# Modulus
modulus = x % y
print(f"The modulus of {x} and {y} is {modulus}")

# Exponentiation
exponentiation = x ** y
print(f"The exponentiation of {x} to the power of {y} is {exponentiation}")



# Logical operations
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# Relational operations
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x >= y: {x >= y}")
print(f"x <= y: {x <= y}")

# Assignment operations
x += y
print(f"x += y: {x}")
x -= y
print(f"x -= y: {x}")
x *= y
print(f"x *= y: {x}")
x /= y
print(f"x /= y: {x}")
x %= y
print(f"x %= y: {x}")
x **= y
print(f"x **= y: {x}")
x //= y
print(f"x //= y: {x}")

# Bitwise operations
x = 10
y = 5
print(f"x & y: {x & y}")
print(f"x | y: {x | y}")
print(f"x ^ y: {x ^ y}")
print(f"~x: {~x}")
print(f"x << y: {x << y}")
print(f"x >> y: {x >> y}")



# Using identity operators
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")

# Assigning same value to both variables
b = 10
print(f"a is b: {a is b}")
print(f"a is not b: {a is not b}")
'''
'''
# Swapping two values using bitwise XOR operator
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping using XOR:")
print("a =", a)
print("b =", b)

'''

'''
# Program to multiply a number by 4 using bitwise operators

def multiply_by_4(n):
    return n << 2

# Example usage
number = int(input("Enter a number to multiply by 4: "))
result = multiply_by_4(number)
print(f"The result of multiplying {number} by 4 is: {result}")

'''
'''

def sqrt(n):
    return n ** 0.5
# Example usage
number = int(input("Enter a number to find the square root: "))
result = sqrt(number)
print(f"The square root of {number} is: {result}")
'''
'''
def convertSeconds(hours=1, minutes=1, seconds=1):
    return hours * 3600 + minutes * 60 + seconds    

# Example usage
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
total_seconds = convertSeconds(hours, minutes, seconds)
print(f"The total number of seconds is: {total_seconds}")

'''