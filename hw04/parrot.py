'''parrot.py
Bode W 
Homework 4 | Problem 1

This program will echo back whatever the user types in all uppercase letters,
until the user types quiet.
'''

while True:
    user_input = input(">")
    if user_input.lower().strip() == "quiet":
        break
    else:
        print(user_input.upper())
