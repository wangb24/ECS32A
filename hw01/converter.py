'''converter.py
Bode W
Homework 1 Problem 10

Convert character to int and binary and print to the terminal.
'''
# Ask for user input
character = input("Enter a character:")

# Print output
print(f"{character} corresponds to the integer {ord(character)} which is {bin(ord(character))} in binary.")
