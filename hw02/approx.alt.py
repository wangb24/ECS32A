'''approx.py
(c) Bode W | Apache License 2.0
Homework 2 | Challenge Problem

The code would ask user to enter two floating point numbers.
- If the numbers are exactly the same, it would print "Those numbers are identical"
- If the numbers are the same to more than 9 decimal place (difference < 1e-10),
  it would print "Those numbers are nearly identical"
- If the number are the same to 2-9 decimal places (n-th place),
  it would print "Those numbers are the same to {n} decimal places"
- Else, it would print "Those numbers are different"

- updated 4/24/2023
    fix 3.141592 vs 3.1416: should be 3 but not 5
'''


def main() -> None:
    '''main function'''
    # ask user to enter two numbers
    num_1 = input('Enter a number:')
    num_2 = input('Enter a number:')

    # First check if the inputs are identical
    if num_1.strip() == num_2.strip():
        print('Those numbers are identical')
        return

    # Convert the inputs to float
    num_1 = float(num_1)
    num_2 = float(num_2)

    # Then check if the inputs are nearly identical
    if abs(int(num_1 * 1e10) - int(num_2 * 1e10)) < 1:
        print('Those numbers are very nearly identical')
        return 10

    # Then check if the inputs are the same to 2-9 decimal places
    for i in range(9, 1, -1):
        if abs(int(num_1 * 10**i) - int(num_2 * 10**i)) < 1:
            print(f'Those numbers are the same to {i} decimal places')
            return i

    # Else, the inputs are different
    print('Those numbers are different')
    return 0


# Run the program
if __name__ == '__main__':
    main()