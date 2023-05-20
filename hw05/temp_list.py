'''temp_list.py
Bode W
Homework 5 | Problem 3

This program will read a csv file the user specifies and
convert the Value to a list, then print the list.
'''

# import read_csv function from read_csv.py
from read_csv import read_csv as read

# get file name from user
file_name = input('Temperature anomaly filename:')

# read the data
year, value = read(file_name)

# print the list of values
print(value)
