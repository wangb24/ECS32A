'''read_temp_file.py
Bode W
Homework 5 | Problem 1

This program will ask user to input a file name,
and then print the data of the file. 
'''

# Ask user to input file name
file_name = input('Temperature anomaly filename:')

# open file
with open(file_name, 'r', encoding="utf-8") as file:
    # ignore the first line that contains the title
    file.readline()
    # read the rest of the file
    # this for loop will read the file line by line
    for line in file:
        # strip the empty character
        line = line.strip()
        # split the line
        year, temp = line.split(',')
        # convert temp to float
        temp = float(temp)
        # print the data
        print(f'{year} {temp}')
