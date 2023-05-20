'''temp_file_stats.py
Bode W
Homework 5 | Problem 2

This program will read a csv file the user specifies and
print the minimum and maximum.
'''

# import read_csv.py
from read_csv import read_csv as read

# get file name from user
file_name = input('Temperature anomaly filename:')

# read the data
year, value = read(file_name)

# get the minimum temperature and the year it occurred
min_temp = min(value) # get the minimum
min_year = year[value.index(min_temp)] # get the year

# get the maximum
max_temp = max(value) # get the maximum
max_year = year[value.index(max_temp)] # get the year

# print the results
print(f"Min temp: {min_temp} in {min_year}")
print(f"Max temp: {max_temp} in {max_year}")