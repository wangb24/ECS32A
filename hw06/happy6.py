'''happy6.py
Bode W
Homework 6 | Part 6
'''

from settings import DATA_PATH

def main():
    '''main()'''
    # Part 1
    # Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()

    # Part 2
    # Print key value pairs sorted by key
    # Uncomment the function call below for part 2 only
    #print_sorted_dictionary(happy_dict)

    # Part 3
    # Uncomment the function call below for part 3 only
    # lookup happiness by country until the user enters done
    #lookup_happiness_by_country(happy_dict)

    # Parts 4-6
    # Uncomment the function call below for parts 4-6
    # Read file containing population and GDP data and add happiness data
    read_gdp_data(happy_dict)



def make_happy_dict(data_path: str = DATA_PATH) -> dict:
    '''make_happy_dict(data_path) -> dict
    This function will open and read the data file and return a dictionary
    mapping country names to happiness index values.
    '''
    happy_dict = {}  # initialize empty dictionary
    # open file for reading
    with open(data_path + "happiness.csv", "r", encoding="utf-8") as csv_happiness:
        csv_happiness.readline()  # skip first line that contain column headers
        # read each line in the file
        for line in csv_happiness:
            country, _, score = line.strip().split(",")
            happy_dict[country] = float(score)

    return happy_dict  # return the dictionary


def read_gdp_data(happy_dict: dict) -> None:
    '''read_gdp_data(happy_dict: dict) -> None
    This function will read the GDP data file, combine happiness data with the GDP
    data, select the countries where population is greater than 100 million, and
    print the combined data.'''
    # First read the GDP data
    gdp_data = read_gdp_file_and_convert_to_list()
    # Then combine the happiness data with the GDP data
    combined_data = combine_happiness_with_gdp(happy_dict, gdp_data)
    # Then select the countries where population is greater than 100 million
    selected_data = [datum for datum in combined_data[1:] if float(datum[1]) > 100]
    selected_data = [combined_data[0]] + selected_data
    print_2d_list(selected_data)


def read_gdp_file_and_convert_to_list(data_path: str = DATA_PATH) -> list:
    '''read_gdp_file_and_convert_to_list() -> list
    This function will read the tsv file containing GDP data and convert it
    to a two dimensional list.  It will return the list.'''
    data = []
    # This opens the file for reading
    with open(data_path + "world_pop_gdp.tsv", 'r', encoding='utf-8') as gdp_data_file:
        # This for loop will read each line in the file
        for line in gdp_data_file:
            # First strip the line of any leading or trailing whitespace
            line = line.strip()
            # Then remove any dollar signs or commas
            line = line.replace("$", "").replace(",", "")
            # Then split the line into a list of strings
            line = line.split("\t")
            # Then append the list to the data list
            data.append(line)
    # Finally, return the data list
    return data


def print_2d_list(data: list) -> None:
    '''print_2d_list(data) -> None
    This function will print the data in the two dimensional list'''
    # Handles exceptions if there are bug in this awfully written code
    # and prints out the error message and some debugging information
    try:
        # This for loop will iterate through each list in the data list
        for datum in data:
            print(",".join([str(d) for d in datum]))
    except Exception as err:
        print(err)
        print(len(data))
        print(data[0])
        print(type(data[0]))
        print(len(data[0]))



def combine_happiness_with_gdp(happiness_data: dict, gdp_data: list) -> list:
    '''combine_happiness_with_gdp(happiness_data, gdp_data) -> list
    This function will combine the happiness data with the GDP data and return
    the combined data as a two dimensional list. It will omit any countries
    that are not found in both data sets.'''
    # Create a new list with the column headers
    data = ["Country,Population in Millions,GDP per Capita,Happiness".split(",")]
    # This for loop will iterate through each list in the happiness_data list
    for datum in gdp_data:
        # look up happiness for the country
        happiness = \
        lookup_happiness_by_country_but_return_the_value_instead_of_printing_it_to_the_terminal(
            happiness_data, datum[0]
        )
        # Check if the country exit in the happiness list
        if happiness == -1.0:
            continue
        else:
            to_add = datum.copy()
            to_add.append(happiness)
            data.append(to_add)
    # Finally, return the data list
    return data


# def lookup_happiness_by_country(happy_dict: dict) -> None:
#     '''lookup_happiness_by_country(happy_dict) -> None
#     This function will prompt the user for a country name and print the
#     happiness index for that country.  If the country is not found, it will
#     print a message saying so. It will keep asking for a country until the
#     user enters "done".'''
#     # This is an indefinite loop that keeps asking for a country name.
#     # It would stop when the user enters "done"
#     while True:
#         country_to_lookup = input("Enter a country to lookup or 'done' to exit:")
#         if country_to_lookup == "done":
#             return
#         happiness = \
#         lookup_happiness_by_country_but_return_the_value_instead_of_printing_it_to_the_terminal(
#             happy_dict, country_to_lookup
#         )
#         str_to_print = f"{happiness}" if happiness != -1.0 else f"{country_to_lookup} not found"
#         print(str_to_print)


def lookup_happiness_by_country_but_return_the_value_instead_of_printing_it_to_the_terminal(
    happy_dict: dict, country: str, case_sensitive: bool = False) -> float:
    '''lookup_happiness_..._terminal(dict, country, case_sensitive) -> float
    This function will return the happiness index for the given data and country.
    If the country is not found, it will return -1.0.'''
    # the if statement below convert everything to lowercase if case_sensitive is False
    if not case_sensitive:
        happy_dict = {key.lower(): value for key, value in happy_dict.items()}
        country = country.lower()
    return happy_dict.get(country, -1.0)


# Function prints all the values in a dictionary d sorted by key
def print_sorted_dictionary(D):
    if not isinstance(D, dict):
        print("Dictionary not found")
        return
    print("Contents of dictionary sorted by key.")
    print("Key", "Value")
    for key in sorted(D.keys()):
        print(key, D[key])


if __name__ == "__main__":
    main()
