from math import pi


def read_in_radius():
    radius = input("Please provide radius: ")
    return float(radius)


radius = read_in_radius()
area = str(pi * radius ** 2)
print(f'The area of radius {radius}, is {area}')
