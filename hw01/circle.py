'''circle.py
Bode W
Homework 1 Problem 8

This code asks user to input radius of a circle, and then it prints out
diameter, circumference, and area of the circle to the terminal. 
'''
# Define constants
PI = 3.14159

# Following line asks user for input
radius = float(input("Enter radius:"))

# The following lines perform the calculations
diameter = radius * 2
circumference = PI * diameter
area = PI * (radius ** 2)

# The following lines prints the output
print(f"""Diameter {diameter}
Circumference {circumference}
Area {area}""")
