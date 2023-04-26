'''ticket.py
Bode W
Homework 3 | Problem 3

This program will ask user to input their age,
and would print the price of the ticket based on their age.
'''

# Ask user for their age
age = int(input("Enter age:"))

# Determine the price with if-elif-else statement
if age < 3:
    print("Your price is FREE")
elif age < 13:
    print("Your price is $29.95")
elif age < 18:
    print("Your price is $39.95")
elif age >= 65:
    print("Your price is $39.95")
else:
    is_student = input("College ID? (y/n)") == "y"
    if is_student:
        print("Your price is $39.95")
    else:
        print("Your price is $49.95")
