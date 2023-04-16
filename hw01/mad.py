'''mad.py
Bode W
Homework 1 Problem 4

This module asks user to input a series of words, fills them into
the corresponding spots in the "BOOKish Mad Libs", and prints the result
to the terminal.
'''
# The following lines of code asks user for input
adj = input("Enter an adjective:")
noun = input("Enter a noun:")
plural_noun = input("Enter a plural noun:")
place = input("Enter a place:")
body_part = input("Enter a part of the body:")

print()  # This line adds a blank line to the terminal output.

# The following code fills the words and prints the paragraph to the terminal.
print(f'''There are many {adj} ways to choose a {noun} to read.
You could ask recommendations from your friends and {plural_noun}.
If they are no help, head to your local library or {place} and browse the shelves
until something catches your {body_part}.''')
