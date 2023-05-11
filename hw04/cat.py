'''cat.py
Bode W
Homework 4 | Problem 6

This program mimics the UNIX cat command.
It asks user to input a file name, and then prints out the contents of the file.
'''

# Ask user to input a file name
file_name = input("Enter a file name to open:")

# Open the file
with open(file_name, "r", encoding="UTF-8") as f:
    # Print out the contents of the file
    for line in f:
        print(line.strip("\n"))
