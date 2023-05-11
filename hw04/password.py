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

this version is implemented using regular expression
'''

# import regular expression module
import re

# Ask user to input a password
user_input = input("Enter password:")

# Check if password is at least 8 characters long
if len(user_input) >= 8:
    print("Has length")

# Check if password has lower case
if re.search(r"[a-z]+", user_input):
    print("Has lower case")

# Check if password has upper case
if re.search(r"[A-Z]+", user_input):
    print("Has upper case")

# Check if password has digit
if re.search(r"\d+", user_input):
    print("Has digit")

# Check if password has special character
if re.search(r"[^a-zA-Z0-9]+", user_input):
    print("Has special")
