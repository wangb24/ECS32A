'''mileage.py
Bode W
Homework 3 | Problem 8

The program repeatedly asks the user to enter number of miles driven
and gallons of gas used. 
Then the program will calculate and print the mileage.
'''
print("Your Personal Fuel Economy")
# initiate variables
total_miles = 0
total_gallons = 0

# This while loop will ask user to enter miles and gallons,
# until the user enters an empty string
while True:
    miles = input("Number of miles traveled (or enter to exit):")
    if miles == "":
        break
    else:
        miles = float(miles)
        gallons = float(input("Number of gallons needed:"))
        print(f"Mileage this tank = {miles/gallons:.1f}")
        total_miles += miles
        total_gallons += gallons

# Calculate and print the total mileage
print(f"Average mileage = {total_miles/total_gallons:.1f}")
