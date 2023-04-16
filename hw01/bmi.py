'''bmi.py
Bode W
Homework 1 Problem 5

This module asks user to input height and weight (in inches and pounds),
and then calculates and outputs the BMI to the terminal.
'''
# The following lines asks user for input
height = float(input("Enter height in inches:"))
weight = float(input("Enter weight in pounds:"))

# The following line calculates BMI
bmi = weight / (height ** 2) * 703

# The following line prints the result to the terminal
print(f"BMI: {bmi}")
