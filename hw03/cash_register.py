'''cash_register.py
Bode W
Homework 3 | Problem 5

This program will ask user for price of each item,
and would return the total price and number of items.
'''

# Initialize variables
total_price = 0
num_items = 0

# Print title
print("Cash register (press enter to exit)")

# This will loop will continue to ask user for price of the item,
# and will add the price to the total price and add 1 to number of items,
# until there is an empty input.
while True:
    price = input("Enter item cost:")
    if price == "":
        break
    else:
        total_price += float(price)
        num_items += 1

# Print the total price and number of items
print(f"You entered {num_items} items totaling ${total_price:.2f}")
