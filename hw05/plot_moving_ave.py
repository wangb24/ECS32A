'''plot_moving_ave.py
Bode W
Homework 5 | Problem Challenge (8)

This program will plot the original data along with the moving average data.
'''

# Import modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from first_ave import running_average

# Set constants
K = 20  # The number of years to average over

# Read the data
dat = pd.read_csv('data/SacramentoTemps.csv')

# Calculate the moving average
moving_avg, c_year = running_average(dat['Value'].to_list(), dat['Year'].to_list(), K)
dat_avg = pd.DataFrame({'Year': c_year, 'Moving_Average': moving_avg})
del c_year, moving_avg

# Combine the data
dat = dat.merge(dat_avg, on = 'Year', how = 'inner')
del dat_avg
# print(dat.head(15))

# Plot the data
sns.set(style = "whitegrid")

fig, ax = plt.subplots() # Create the figure and axes
sns.lineplot(data = dat, x = "Year", y = "Value", ax = ax) # Plot the original data
sns.lineplot(data = dat, x = "Year", y = "Moving_Average", ax = ax) # Plot the moving average data

# Set the title and labels
ax.set_title(f"Plotting SacramentoTemps.csv (Moving Average, k = {K})")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature Anomaly")

# plt.show()
plt.savefig('figure/matplotlib.pdf', dpi = 900)