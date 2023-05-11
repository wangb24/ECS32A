'''digits.py
Bode W
Homework 4 | Problem 4

This program will ask user to input a phone number of any format,
and extract the digits from the input.
'''

# import regular expression module
import re

# Ask user to input a phone number
user_input = input("Enter phone number:")

# Extract the digits from the input
digits = re.findall(r"\d", user_input)

# Print out the results
print(f"Digit string: {''.join(digits)}")
