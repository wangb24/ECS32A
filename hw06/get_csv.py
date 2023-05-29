'''get_csv.py
Bode W | Apache 2.0 | (c) 2023

This program will read the happiness data and gdp data, combine them, and
write the combined data to a new csv file.
'''
def main():
    '''main()'''
    happy_data = make_happy_dict("data/happiness.csv")
    gdp_data = read_gdp_file_and_convert_to_list("data/world_pop_gdp.tsv")
    combined = combine_happiness_with_gdp(happy_data, gdp_data)

    with open("out/happiness_gdp.csv", "w", encoding="utf-8") as out_file:
        for line in combined:
            line = str(line).strip("[]").replace(', ', ',').replace("'", "")
            out_file.write(line + "\n")


def make_happy_dict(path: str) -> dict:
    '''make_happy_dict(path) -> dict
    This function will open and read the data file and return a dictionary
    mapping country names to happiness index values.
    '''
    happy_dict = {}  # initialize empty dictionary
    # open file for reading
    with open(path, "r", encoding="utf-8") as csv_happiness:
        csv_happiness.readline()  # skip first line that contain column headers
        # read each line in the file
        for line in csv_happiness:
            country, _, score = line.strip().split(",")
            happy_dict[country] = score

    return happy_dict  # return the dictionary


def read_gdp_file_and_convert_to_list(path: str) -> list:
    '''read_gdp_file_and_convert_to_list(path) -> list
    This function will read the tsv file containing GDP data and convert it
    to a two dimensional list.  It will return the list.'''
    data = []
    # This opens the file for reading
    with open(path, 'r', encoding='utf-8') as gdp_data_file:
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


if __name__ == "__main__":
    main()