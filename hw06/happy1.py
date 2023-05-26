'''happy1.py
Bode W
Homework 6 | Part 1
'''

from settings import DATA_PATH

def main():
    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    # The following line prints the dictionary
    for country, index in happy_dict.items():
        print(country, index)

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    # print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    # lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6 
    # Read file containing population and GDP data and add happiness data
    #read_gdp_data(happy_dict)


def make_happy_dict():
    '''make_happy_dict() -> dict
    This function will open and read the data file and return a dictionary
    mapping country names to happiness index values.
    '''
    happy_dict = {}  # initialize empty dictionary
    # open file for reading
    with open(DATA_PATH + "happiness.csv", "r", encoding="utf-8") as csv_happiness:
        csv_happiness.readline()  # skip first line that contain column headers
        # read each line in the file
        for line in csv_happiness:
            country, _, score = line.strip().split(",")
            happy_dict[country] = float(score)

    return happy_dict  # return the dictionary


main()
