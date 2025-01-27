
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

