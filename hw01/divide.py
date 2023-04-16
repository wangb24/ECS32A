'''divide.py
Bode W
Homework 1 Problem 9

User inputs two numbers, the program calculates the quotient and remainder
and prints the results to the terminal.
'''
# Define a function to handle various inputs
def input_handler(prompt: str):
    '''Convert input to int if user inputs int, or float otherwise'''
    inp = input(prompt)
    try:
        return int(inp)
    except ValueError:
        try:
            return float(inp)
        except ValueError:
            print("Invalid input")
            return input_handler(prompt)

# Asks user for inputs
divident = input_handler("Enter a number:")
divisor = input_handler("Enter a number to divide that by:")

# Perform calculations and print results
print(f"{divident} divided by {divisor} is {divident//divisor} with {divident%divisor} remaining")
