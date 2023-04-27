'''tip.py
Bode W
Homework 3 | Problem 4

This program will ask user for the total price,
and will calculate 15% to 25% tip based on the total price.
'''

# Ask user for the total price
total_price = float(input("Enter total:"))

# Calculate the tip
i = 15
# If the variable i, representing the tip percentage,
# is less than or equal to 25, then print the tip amount
while i <= 25:
    print(f"A {i}% tip is ${total_price * i / 100:.2f}")
    i += 1
