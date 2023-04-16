'''fahr2cel.py
Bode W
Homework 1 Problem 1

This code converts 32 degree F to degree C and print the result to the terminal.
'''
FAHRENHEIT = 32  # stores degree F to a variable
CELSIUS = (FAHRENHEIT - 32.0) * (5 / 9)  # calculate and stores result to celsius
print(FAHRENHEIT, "Fahrenheit is", CELSIUS, "Celsius.")
