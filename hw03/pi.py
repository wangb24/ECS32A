'''pi.py
Bode W
Homework 3 | Challenge Problem

This program will estimate pi using following infinite series:
pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 + ...
The program will prompt number of terms to use in the series,
then print the estimate of pi.
'''

# import math (for actual value of pi)
from math import pi

def estimate_pi(terms: int) -> float:
    '''This function will estimate pi using the infinite series

    Args: 
        terms (int) - number of terms to use in the series
    '''
    # initialize variables
    pi_estimate = 0
    i = 0

    # loop through terms and add/subtract next term in series to the estimate
    while i < terms:
        # add/subtract next term in series
        pi_estimate += 4 * (-1)**i / (2*i + 1)
        i += 1

    return pi_estimate

def main():
    '''main function'''
    # prompt user for number of terms to use in series
    n = int(input("Number of terms:"))
    # calculate estimate of pi
    estimate = estimate_pi(n)
    # print estimate of pi
    print(f"Estimate of pi: {estimate:.9f}")
    # print error of the estimate
    print(f"Error: {(pi - estimate):.9f}")

# call main function
if __name__ == "__main__":
    main()
