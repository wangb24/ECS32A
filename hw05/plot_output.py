'''plot_output.py
Bode W
Homework 5 | Problem 7

This program plots a line chart of the output of the 'moving_ave_csv.py' program.
'''

# Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme() # Set the theme for the plot

# Read the data
dat = pd.read_csv('MovingAve.csv')
# print(dat.head())

# Plot the data
plot = sns.lineplot(data = dat, x = "Year", y = "Value")
plot.set_title("Sacramento July Temperatures (Moving Average, k = 18)")
plot.set_xlabel("Year")
plot.set_ylabel("Temperature Anomaly")

plt.savefig("figure/Plot_Part_7.png", dpi = 900)