'''plot_output.py
Bode W
Homework 5 | Problem 7

This program plots a line chart of the output of the 'moving_ave_csv.py' program.
'''

# Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from first_ave import running_average
from read_csv import read_csv

# Set constants
K = 18  # Window size

sns.set_theme() # Set the theme for the plot

# dat = pd.read_csv('MovingAve.csv')
# Create the data
yrs, val = read_csv('data/SacramentoTemps.csv')
val, yrs = running_average(val, yrs, K)
dat = pd.DataFrame({'Year': yrs, 'Value': val})
del yrs, val

# Plot the data
plot = sns.lineplot(data = dat, x = "Year", y = "Value")
plot.set_title(f"Sacramento July Temperatures (Moving Average, k = {K})")
plot.set_xlabel("Year")
plot.set_ylabel("Temperature Anomaly")

# plt.show()
plt.savefig("figure/Plot_Part_7.png", dpi = 900)