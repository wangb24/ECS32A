'''heart.py
Bode W
Homework 1 Problem 6

This module asks user for age, then it calculates the maximum heart rate
and target heart rate based on the formula provided by AHA. Finally it 
prints the results to the terminal.
'''
# The following line asks user for input and converts it to int
age = int(input("Enter your age:"))

# The following lines are for calculations
max_heartrate = 220 - age
target_heartrate = [i * max_heartrate for i in (0.5, 0.85)]

# The following lines prints the result to the terminal
print(f"""Your maximum heart rate is {max_heartrate} bpm
Your target heart rate is {target_heartrate[0]} - {target_heartrate[1]} bpm""")
