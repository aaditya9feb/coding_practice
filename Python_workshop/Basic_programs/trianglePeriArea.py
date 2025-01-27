# Function to calculate the perimeter of a triangle
def calculate_perimeter(a, b, c):
    return a + b + c

# Function to calculate the area of a triangle using Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

# Input sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate perimeter and area
perimeter = calculate_perimeter(a, b, c)
area = calculate_area(a, b, c)

# Display the results
print(f"The perimeter of the triangle is: {perimeter}")
print(f"The area of the triangle is: {area}")