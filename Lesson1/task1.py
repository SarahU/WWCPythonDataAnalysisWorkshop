# Create and upload one of the task. Please upload 2 files .py and screen
# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

from math import pi


def read_in_radius():
    radius = input("Please provide radius: ")
    return float(radius)


radius = read_in_radius()
area = str(pi * radius ** 2)
print(f'The area of radius {radius}, is {area}')