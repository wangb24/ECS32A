'''trycat.py
Bode W
Homework 4 | Problem 7

This program mimics the UNIX cat command. 
It asks user to input a file name, and then prints out the contents of the file.
If the file does not exist, it asks user to input another file name.
'''

# initialize a boolean variable to indicate whether the file name is valid
valid_file = False

# keep asking user to input a file name until the file name is valid
while not valid_file:
    # Ask user to input a file name
    file_name = input("Enter a file name to open:")

    # Try to open the file
    try:
        with open(file_name, "r", encoding="UTF-8") as f:
            # Print out the contents of the file
            for line in f:
                print(line.strip("\n"))
            # set valid_file to True
            valid_file = True
    except FileNotFoundError:
        # If the file does not exist, ask user to input another file name
        print(f"Could not open '{file_name}'")
