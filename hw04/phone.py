'''phone.py
Bode W
Homework 4 | Problem 3

Check if the input is exactly this format and contain only digits:
xxx xxx-xxxx
'''

# import regular expression module
import re

# Ask user to input a phone number
user_input = input("Enter number as ### ###-####:")

# Check if the input is exactly this format and contain only digits
is_match = re.match(r"^\d{3} \d{3}-\d{4}$", user_input)

# Print out the results
if is_match:
    print("Valid")
else:
    print("Invalid")
