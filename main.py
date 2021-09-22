from datetime import datetime
import pandas

import graphing # Custom graphing code. See our GitHub repository

# Load a file that contains weather data for Seattle
data = pandas.read_csv('seattleWeather_1948-2017.csv', parse_dates=['date'])

# Remove all dates after July 1 because we have to to plant onions before summer begins
data = data[[d.month < 7 for d in data.date]].copy()


# Convert the dates into numbers so we can use them in our models
# We make a year column that can contain fractions. For example,
# 1948.5 is halfway through the year 1948
data["year"] = [(d.year + d.timetuple().tm_yday / 365.25) for d in data.date]

# Let's take a quick look at our data
print("Visual Check:")
graphing.scatter_2D(data, 
                    label_x="year", 
                    label_y="min_temperature",
                    title="Temperatures over time (°F)")