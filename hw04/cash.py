'''cash.py
Bode W
Homework 4 | Problem 8

This program will read a file contains a list of prices separated by newlines,
and then print the total price of all the items in the file.
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
        # Add the price to the total
        total += float(line)
        item_count += 1

# Print the total
print(f"File contained {item_count} items totaling ${total:.2f}")