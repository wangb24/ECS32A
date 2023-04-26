'''pocket.py
Bode W
Homework 3 | Problem 1

This program will ask the user to enter the number of 
pennies, nickels, dimes, and quarters.
Then the program will calculate the total value of the
coins in the pocket.
'''
print("Compute your pocket change!")

# Ask user for number of pennies, nickels, dimes, and quarters
quarters = int(input("Quarters?"))
dimes = int(input("Dimes?"))
nickels = int(input("Nickels?"))
pennies = int(input("Pennies?"))

# Calculate total value of coins
total = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)

# Print total value of coins
print(f"The total is ${total/100:.2f}")
