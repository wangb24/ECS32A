'''read_csv.py
Bode W (c) 2023 
Apache License 2.0

This module will read a csv file contains two columns: Year and Value.
It will return two lists contains those variables. 
'''

def read_csv(file):
    '''read_csv(file) -> [year], [value]
    This function will read a csv file contains columns year and value. It will return two lists contains those variables.
    
    Args:
        file (str): The path to the csv file.
    '''
    # create empty lists to store the data
    year = []
    value = []
    with open(file, 'r', encoding='utf-8') as fs:
        # skip the first line of the file that contains column names
        fs.readline()
        # the for loop will go through each line of the file
        # and write the data to the corresponding list
        for line in fs:
            line = line.strip().split(',')
            year.append(int(line[0]))
            value.append(float(line[1]))
    # return the lists
    return year, value

def mean(lst) -> float:
    '''mean(list) -> float
    This function will calculate the mean of a list.
    '''
    return sum(lst) / len(lst)
