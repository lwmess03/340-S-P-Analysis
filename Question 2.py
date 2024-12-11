# . How does the month of November react after the election?
#    This question is interesting because we want to know if easing political unrest increases performance for a time being.

import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

# Create a filepath
path_to_file = 'Macrotrends-s-p-500-index-daily.csv'

# Load data
data = pd.read_csv(path_to_file, skiprows = 9, delimiter= ',' )
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
plt.plot(november_non_election_year_closing_value, november_non_election_year_date, label = 'November Non Election Year')
plt.plot(november_election_year_closing_value, november_election_year_date, label = 'November Election Year')
plt.title('Non Election and Election Years November S&P Graph')
plt.xlabel('Closing Value')
plt.ylabel('Date')
plt.legend()
plt.show()

#Perform a T-test
t_stat, p_value = ttest_ind(november_election_year_closing_value, november_non_election_year_closing_value)
if p_value < 0.05:
    print("There is a statistical difference between novembers in non election years and election years")
else:
    print("There is not a statistical difference between novembers in non election years and election years")

#Take average of november election year closing value data
election_november_average_closing_value = np.average(november_election_year_closing_value)
print("The closing value average for election year novembers are ", election_november_average_closing_value)

#Take std of november election year closing value data
election_november_std_closing_value = np.std(november_election_year_closing_value)
print("The closing value standard deviation for election year novembers are ", election_november_std_closing_value)

#Take average of november non election year closing value data
non_election_november_average_closing_value = np.average(november_non_election_year_closing_value)
print("The closing value average for non election year novembers are ", non_election_november_average_closing_value)

#Take std of november non election year closing value data
non_election_november_std_closing_value = np.std(november_non_election_year_closing_value)
print("The closing value standard deviation for non election year novembers are ", non_election_november_std_closing_value)

#Take the percent change between averages
percent_change_averages = ((election_november_average_closing_value - non_election_november_average_closing_value)/non_election_november_average_closing_value)*100
print("The percent change from average election year novembers and non election year novembers is ", percent_change_averages)

#Take the percent change between stds
percent_change_std = ((election_november_std_closing_value - non_election_november_std_closing_value)/non_election_november_std_closing_value)*100
print("The percent change from standard deviation election year novembers and non election year novembers is ", percent_change_std)


#Function to find percent change of closed value data
daily_percent_change = closed_value.pct_change()*100

#Only include percent change data on november election year
november_election_year_percent_changes = daily_percent_change[november_election_year_closing_value.index]

#Only include percent change data on november non election year
november_non_election_year_percent_changes = daily_percent_change[november_non_election_year_closing_value.index]

#Create plot comparing november election percent change and non election year percent change
plt.plot(november_election_year_percent_changes, label = 'November Election Years')
plt.plot(november_non_election_year_percent_changes, label = 'November Non Election Years')
plt.title('Daily Percent Changed in November')
plt.xlabel('Closing Value')
plt.ylabel('Daily Percent Change')
plt.legend()
plt.show()