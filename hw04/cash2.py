'''cash2.py
Bode W
Homework 4 | Problem 9

This program will read a file contains a list of prices separated by newlines,
and then print the total price of all the items in the file.
This version will able to handle dollar signs,
and skip lines that are not valid prices.
'''
print("Automated cash register")

# Get the file name from the user
file_name = input("Enter file of prices:")

# Initialize the total and item_count
total = 0
item_count = 0

# Open the file
with open(file_name, "r", encoding="UTF-8") as prices:
    # Iterate over each line in the file
    for line in prices:
        # Strip the line of whitespace
        line = line.strip(" $")
        # use a try/except block to handle invalid prices
        try:
            price = float(line)
            # Add the price to the total
            total += price
            item_count += 1
        except ValueError:
            continue

# Print the total
print(f"File contained {item_count} items totaling ${total:.2f}")
