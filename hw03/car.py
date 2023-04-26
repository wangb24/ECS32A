'''car.py
Bode W
Homework 3 | Problem 7

The program will ask user to guess the price of a car.
If the user's guess is too high, the program will print "Too high!"
If the user's guess is too low, the program will print "Too low!"
If the user's guess is correct, the program will print number of guesses.
If number of guesses <= 5, the player wins.
'''
print("Guess the price and win the prize!")
# initiate constants and variables
ACTUAL_PRICE = 44500
num_guesses = 0

# This while loop will run until the user guesses the correct price
while True:
    guess = int(input("Enter your guess:"))
    num_guesses += 1
    if guess > ACTUAL_PRICE:
        print("Too high!")
    elif guess < ACTUAL_PRICE:
        print("Too low!")
    else:
        print(f"It took {num_guesses} guesses.")
        break

# Determine if the player wins the prize
if num_guesses <= 5:
    print("You won the car!")
else:
    print("Too many guesses!")
