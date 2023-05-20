'''first_ave.py
Bode W
Homework 5 | Problem 4

This program will ask user to input a csv filename and a window size.
The program will calculate the average of the first window.
'''

# Import functions from read_csv.py
import read_csv as read

# Define a function that returns a list of the average of all windows
def running_average(list_value, list_year, window_size):
    '''running_average(value, year, window_size) -> [average], [year]
    This function will calculate the average of all windows, and return a list
    of the averages and their corresponding years.
    '''
    # Create empty lists to store the average and corresponding year
    avg_list = []
    corresponding_year = []
    # get the length of the data
    data_size = len(list_value)
    # this loop will go through each window
    for i in range(window_size, data_size - window_size):
        # determine start and end index of each window
        start = i - window_size
        end = i + window_size + 1
        # get the average of each window
        avg = read.mean(list_value[start:end])
        # get the corresponding year of the average
        yr = list_year[i]
        # append the calculations to the list
        avg_list.append(avg)
        corresponding_year.append(yr)
    # return the list of averages and corresponding years
    return avg_list, corresponding_year

# Run the program only if it is not imported
if __name__ == '__main__':
    # Ask user for csv filename and window size
    filename = input('Temperature anomaly filename:')
    window = int(input('Enter window size:'))

    # Read csv file
    year, value = read.read_csv(filename)

    # Call the function
    average, c_year = running_average(value, year, window)

    # Print the average of the first window
    print(f"{c_year[0]},{average[0]:.4f}")
