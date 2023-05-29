# plot_data.r
# Bode W
# (c) 2023

# This script plots the data from the happiness_gdp.csv file with ggplot2
# X axis: GDP per capita
# Y axis: Happiness score
# Color: Country
# Size: Population

## run script get_csv.py first to obtain the csv file that contain the data

# Load libraries
library(ggplot2)
library(dplyr)
library(here)
library(janitor)

# Disable scientific notation
options(scipen = 999)

# set path of the output directory
dir <- here("hw06", "out")

# Load data
data <- readr::read_csv(paste(dir, "/happiness_gdp.csv", sep = "")) %>%
     janitor::clean_names()  # clean column names

head(data, n = 3)  # print first 3 rows



# Plot data
data %>%
     ggplot(
          aes(
               x = gdp_per_capita,
               y = happiness,
               color = country,
               size = population_in_millions
          )
     ) +  # set aesthetics
     geom_text(aes(label = country), color = "#3b3b3b", alpha = 0.3) +  # add country labels
     geom_point(alpha = 0.7) +  # add points
     scale_size(range = c(2, 10)) +  # set point size range
     theme_minimal() +  # set theme
     theme(legend.position = "none") +  # remove legend
     labs(  # set labels
          title = "Happiness vs. GDP per capita",
          x = "GDP per capita",
          y = "Happiness score",
          size = "Population (millions)"
     )

ggsave(
     paste(dir, "/plot_all_countries.with_other_software.png", sep = ""),
     dpi = 1200, width = 12, height = 8, bg = "white"
)


################################################################################

# plot only countries with population > 100 million
data %>%
     filter(population_in_millions > 100) %>%  # select population < 100 million
     ggplot(
          aes(
               x = gdp_per_capita,
               y = happiness,
               color = country,
               size = population_in_millions
          )
     ) +  # set aesthetics
     geom_point(alpha = 0.8) +  # add points
     scale_size(range = c(5, 17)) +  # set point size range
     geom_text(aes(label = country), color = "#3b3b3b", alpha = 0.5) +  # add country labels
     theme_minimal() +  # set theme
     theme(legend.position = "none") +  # remove legend
     labs(  # set labels
          title = "Happiness vs. GDP per capita",
          x = "GDP per capita",
          y = "Happiness score",
          size = "Population (millions)"
     ) +
     xlim(0, 65000) +  # set x axis limits
     ylim(2, 8)  # set y axis limits

ggsave(
     paste(dir, "/plot_pop_over_100.with_other_software.png", sep = ""),
     dpi = 1200, width = 12, height = 8, bg = "white"
)
