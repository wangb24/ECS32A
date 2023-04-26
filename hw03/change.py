'''change.py
Bode W
Homework 3 | Problem 2

The program asks user to input a number of cents.
Then the program will calculate the number of each
types of coins needed to make that amount of change.
'''

# Ask user for number of cents
cents = int(input("Enter cents:"))

# Calculate number of each type of coin
quarters = cents // 25
dimes = (cents % 25) // 10
nickels = ((cents % 25) % 10) // 5
pennies = ((cents % 25) % 10) % 5

# Print number of each type of coin
print(f'''The minimum coins for {cents} cents are:
{quarters} Quarters
{dimes} Dimes
{nickels} Nickels
{pennies} Pennies''')
