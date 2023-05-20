'''moving_ave.py
Bode W
Homework 5 | Problem 5

This program will ask user to input a csv filename and a window size.
The program will calculate and print the average of all windows and 
their corresponding year.
'''

# Import functions form read_csv.py
import read_csv as read

# Import the moving_average function from first_ave.py
from first_ave import running_average

# Ask the user for csv filename and window size
filename = input('Temperature anomaly filename:')
window = int(input('Enter window size:'))

# Read csv file
year, value = read.read_csv(filename)

# Call the running_average function
average, c_year = running_average(value, year, window)

# Print the running average and corresponding year
if __name__ == '__main__':
    for yr, avg in zip(c_year, average):
        print(f"{yr},{avg:.4f}")
