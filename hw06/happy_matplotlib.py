'''happy_matplotlib.py
Bode W
Homework 6 | Challenge

This program will combine happiness data and gdp data,
select countries with a population greater than 100 million,
and plot them using matplotlib.
'''

### Imports ###
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import happy6 as helper


### Constants ###
DATA_PATH = "data/"
OUTPUT_PATH = "out/"


### Functions ###
def break_point(prompt = None):
    '''break_point()
    This function will pause the program and wait for user input.
    '''
    prompt = "Press <ENTER> to continue or <CTRL+C> to exit..." if prompt is None else prompt
    try:
        input(prompt)
    except KeyboardInterrupt:
        sys.exit("\n\nExiting...")


### Data Preparation ###
# Use functions from happy6.py to build dictionary mapping countries to happiness index
happiness_data = helper.make_happy_dict(DATA_PATH)

# Use functions from happy6.py to read GDP data to a list
gdp_data = helper.read_gdp_file_and_convert_to_list(DATA_PATH)

# Use functions from happy6.py to combine happiness data with GDP data to a list
combined_data = helper.combine_happiness_with_gdp(happiness_data, gdp_data)

# Rename column headers
combined_data[0] = ["country", "population", "gdp", "happiness"]

# Convert the list to a pandas dataframe
data = pd.DataFrame(combined_data[1:], columns=combined_data[0])

# Convert population, gdp, and happiness columns to type float
data["population"] = data["population"].astype(float)
data["gdp"] = data["gdp"].astype(float)
data["happiness"] = data["happiness"].astype(float)

# Select countries with population greater than 100 million
data = data[data["population"] > 100]

# Inspect the data before continuing
print(data.head())
break_point()


### Plotting with matplotlib ###
# Set the style of the plot
sns.set_style("whitegrid")
# Define a function to create the plot
def make_plot() -> None:
    '''make_plot()
    This function will make a scatter plot of GDP vs Happiness, with population as the size of the points, and country as the color.
    It also adds country as a label to each point.
    '''
    # Plot a scatter plot of GDP vs Happiness, with population as the size of the points
    plot = sns.scatterplot(
        x = "gdp", y = "happiness",
        size = "population", sizes = (20, 200),
        hue = "country", data = data
    )
    # Remove legend from plot
    plot.get_legend().remove()
    # Add country as a label to each point
    for gdp, happiness, country in zip(data.gdp, data.happiness, data.country):
        plot.text(
            gdp, happiness, country, horizontalalignment = "left",
            size = "small", color = "black", alpha = 0.5
        )
    # Set the title
    plot.set_title("Happiness vs GDP")
    # Set the x and y axis labels
    plot.set_xlabel("GDP per capita")
    plot.set_ylabel("Happiness Index")
    # Set the x and y axis limits
    plot.set_xlim(-3000, 65000)
    plot.set_ylim(2.5, 7.5)

# Display the plot
make_plot()
plt.show()

# Save the plot
break_point("\nSave the plot?\nPress <ENTER> to save or <CTRL+C> to exit...")
make_plot()
plt.savefig(OUTPUT_PATH + "plot_matplotlib.png", dpi = 1200)