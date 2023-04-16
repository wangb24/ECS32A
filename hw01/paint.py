'''paint.py
Bode W
Homework 1 Problem 7

This module estimates number of cans of paint needed based on dimensions
of the room (user input), and print the result. 
'''
from math import ceil
print("Paint coverage estimator")

# The following lines ask user to input dimensions
length = float(input("Length of room in inches:")) / 12
width = float(input("Width of room in inches:")) / 12
height = float(input("Average height of room in inches:")) / 12

# The following lines perform calculations
area = 2 * (length * height) + 2 * (width * height)
number_cans = ceil(area/100)

# Print the result
print(f"You'll want {number_cans} cans.")
