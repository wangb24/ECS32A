'''check.py
Bode W
Homework 4 | Challenge Problem

This program will check if the check digit of a "credit card number" is valid.
The user will provide a 8 digit number. The program check if:
    - Starting from the rightmost digit, form the sum of every other digit.
    - Double each of the digits that were not included in the preceding step. Add all digits of the resulting numbers.
    - Add the sums of the two preceding steps. If the last digit of the result is 0, the number is valid.
If its invalid, the program will determine a valid check digit.
'''

# Get the credit card number from the user
card_number = input("Enter your 8-digit card number:")
card_number = card_number.replace(" ", "")


# define a function that check if the card number is valid,
# and returns a boolean
def check(card_number) -> bool:
    '''check(card_number) -> bool
    This function will check if the card number is valid.
    
    Args:
        card_number (str): The card number to check.
    '''
    
    # Calculate the sum of every other digit
    sum_nums = sum([int(i) for i in card_number[::-2]])

    # Double each of the digits that were not included in the preceding step
    double = "".join([str(int(i) * 2) for i in card_number[-2::-2]])
    double = sum([int(i) for i in double])
    
    # Add the sums of the two preceding steps
    total = sum_nums + double
    
    # return the result
    return total % 10 == 0

# If the card number is valid, print a message,
# otherwise, use brute force to find a valid check digit
if check(card_number):
    print("Valid")
else:
    print("Invalid")
    # Brute force
    for i in range(10):
        if check(card_number[:-1] + str(i)):
            print(f"Check digit should be {i}")
            break
