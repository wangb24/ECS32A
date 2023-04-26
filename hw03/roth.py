'''roth.py
Bode W
Homework 3 | Problem 6

The program asks user to input initial amount and annual percentage rate,
then it will calculate the total amount after each year until
the initial amount is doubled.
'''

# Ask user to input initial amount and annual percentage rate
initial_amount = float(input("Enter an initial Roth IRA deposit amount:"))
annual_rate = int(input("Enter an annual percent rate of return:"))

# Initialize variables
total_amount = initial_amount
year = 0

# This loop will continue to calculate the total amount after each year
# until the initial amount is doubled.
while total_amount < initial_amount * 2:
    total_amount += total_amount * (annual_rate / 100)
    year += 1
    print(f"Value after year {year}: ${total_amount:.2f}")

# Print the number of years it takes to double the initial amount
print(f"It will take {year} years to double your investment with a {annual_rate}% APR.")
