# . How does the month of November react after the election?
#    This question is interesting because we want to know if easing political unrest increases performance for a time being.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a filepath
path_to_file = 'Macrotrends-s-p-500-index-daily.csv'

# Load data
data = pd.read_csv(path_to_file,  delimiter= ',' )
data['Date'] = pd.to_datetime(data['Date'])

# Create Vectors for each column
date = data['Date']
closed_value = data['Closing Value']

#Create list
election_years = []

#For loop to append data into election_years list
for year in range(1928, 2024,4):
    election_years.append(year)

#Create list
non_election_years = []

#For loop to append into non_election_year list
for year in range(1928, 2024):
    if year not in election_years:
        non_election_years.append(year)

#Create List
november_data = []

#Add new list only containing november data
for month in date:
    if month.month == 11:
        november_data.append(month)

#Create new list
november_data_for_election_year = []

#Add new list containing november data and election year data
for something in date:
    if something.month == 11 and something.year in election_years:
        november_data_for_election_year.append(something)

#Filter data to only include november election years
election_year_november_data = data[date.isin(november_data_for_election_year)]

#Extract closing value and date values
november_election_year_closing_value = election_year_november_data['Closing Value']
november_election_year_date = election_year_november_data['Date']

#Create list
november_data_for_non_election_year = []

#Add new list containing november data and non election year data
for something in date:
    if something.month == 11 and something.year in non_election_years:
        november_data_for_non_election_year.append(something)

#Filter data to only include november non election years
non_election_year_november_data = data[date.isin(november_data_for_non_election_year)]

#Extract closing value and date values
november_non_election_year_closing_value = non_election_year_november_data['Closing Value']
november_non_election_year_date = non_election_year_november_data['Date']

#Create plot comparing november election year and non election year data
plt.figure(figsize=(12, 6))
plt.scatter(november_non_election_year_date, november_non_election_year_closing_value, label='November Non Election Year')
plt.scatter(november_election_year_date, november_election_year_closing_value, label='November Election Year')
plt.title('Non Election and Election Years November S&P Graph')
plt.xlabel('Date')
plt.ylabel('Closing Value')  # Y-axis is now Closing Value
plt.legend()
plt.show()


#Take average of november election year closing value data
election_november_average_closing_value = np.average(november_election_year_closing_value)
print("The closing value average for election year novembers are ", election_november_average_closing_value)

#Take average of november non election year closing value data
non_election_november_average_closing_value = np.average(november_non_election_year_closing_value)
print("The closing value average for non election year novembers are ", non_election_november_average_closing_value)

#Take the percent change between averages
percent_change_averages = ((election_november_average_closing_value - non_election_november_average_closing_value)/non_election_november_average_closing_value)*100
print("The percent change from average election year novembers and non election year novembers is ", percent_change_averages)


#Function to find percent change of closed value data
# Calculate percent change
november_election_year_percent_changes = november_election_year_closing_value.pct_change() * 100
november_non_election_year_percent_changes = november_non_election_year_closing_value.pct_change() * 100

november_election_years = november_election_year_date.dt.year
november_non_election_years = november_non_election_year_date.dt.year

# Create a plot with both series on the same plot

plt.plot(november_election_years, november_election_year_percent_changes, label='November Election Years', marker='o', markersize = 3)
plt.plot(november_non_election_years, november_non_election_year_percent_changes, label='November Non-Election Years', marker='o',markersize = 3)
plt.title('Daily Percent Change in November (Election vs. Non-Election Years)')
plt.xlabel('Year')
plt.ylabel('Daily Percent Change (%)')
plt.legend()
plt.grid(True)
plt.show()