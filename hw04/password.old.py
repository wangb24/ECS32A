'''password.py
Bode W
Homework 4 | Problem 2

This program will ask user to input a password,
and will check if the password met the following conditions: 
    - At least 8 characters long
    - Has lower case
    - Has upper case
    - Has a digit
    - Has a special character
'''

# Ask user to input a password
user_input = input("Enter password:")

# Check if password is at least 8 characters long
if len(user_input) >= 8:
    print("Has length")

# initialize variables
lower = False
upper = False
digit = False
special = False

# This for loop loops through each character in the user input,
# and checks if it is a lower case, upper case, digit, or special character.
for char in user_input:
    if char.isdigit():
        digit = True
        continue
    if not char.isalnum():
        special = True
        continue
    if char.lower() == char:
        lower = True
    if char.upper() == char:
        upper = True

# Print out the results
if lower:
    print("Has lower case")
if upper:
    print("Has upper case")
if digit:
    print("Has digit")
if special:
    print("Has special")
