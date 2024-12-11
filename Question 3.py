# What are the pre-election trends that are common in the months leading up to the election?

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


## Get the file path for the historical data
path = 'Macrotrends-s-p-500-index-daily.csv'

## Load in historical the daily closing values
data = pd.read_csv(path)

## gets the dates time date frame
data['Date'] = pd.to_datetime(data['Date'])

## gets the closing values in its own vector
closing_value_np = data['Closing Value']
closing_value_np = np.array(closing_value_np)

closing_value = []
for value in closing_value_np:
    x = float(value)
    closing_value.append(x)

years = []
for year in range(1928,2025):
   years.append(year)

## create a vector that include every election year
M_elections = []
Pres_elecs = []
for M_election in range(len(years)): ## gets every even year (presidential and mid term)
    if M_election % 2 == 0:
        M_elections.append(years[M_election])
for pres_elec in range(len(M_elections)): ## takes those years and returns only presidential elections
    if pres_elec % 2 == 0:
        Pres_elecs.append(M_elections[pres_elec])


# Creating lists that will be used later in for loop
january_days = []
august_days = []
september_days = []
october_days = []

january_values = []
august_values =[]
september_values = []
october_values = []

august_percent_changes = []
september_percent_changes = []
october_percent_changes = []


for year in Pres_elecs:
    # Go through year and store all days of specific months
    january_dates = pd.date_range(start=f'{year}-01-01', end=f'{year}-01-31')
    august_dates = pd.date_range(start=f'{year}-08-01', end=f'{year}-08-31')
    september_dates = pd.date_range(start=f'{year}-09-01', end=f'{year}-09-30')
    october_dates = pd.date_range(start=f'{year}-10-01', end=f'{year}-10-31')

    # append these values to list
    january_days.append(january_dates)
    august_days.append(august_dates)
    september_days.append(september_dates)
    october_days.append(october_dates)

    # Get closing value mean of specific months before election
    january_value = (closing_value_np[data['Date'].isin(january_dates)].mean())
    august_value =  (closing_value_np[data['Date'].isin(august_dates)].mean())
    september_value = (closing_value_np[data['Date'].isin(september_dates)].mean())
    october_value = (closing_value_np[data['Date'].isin(october_dates)].mean())

    # append these values to list
    january_values.append(january_value)
    august_values.append(august_value)
    september_values.append(september_value)
    october_values.append(october_value)

    # Get percent change comparing january mean values to months prior to election
    august_percent_change = ((august_value - january_value)/january_value)*100
    september_percent_change = ((september_value - january_value) / january_value) * 100
    october_percent_change = ((october_value - january_value) / january_value) * 100

    # Append these values to list
    august_percent_changes.append(august_percent_change)
    september_percent_changes.append(september_percent_change)
    october_percent_changes.append(october_percent_change)


# Plot Results
plt.plot(Pres_elecs, january_values, label='January Closing Value')
plt.plot(Pres_elecs, august_values, label='August Closing Value')
plt.plot(Pres_elecs, september_values, label='September Closing Value')
plt.plot(Pres_elecs, october_values, label='October Closing Value')
plt.xlabel('Election Year')
plt.ylabel('Average Closing Value')
plt.title('Pre-Election Trends: Average Closing Value for Election Years')
plt.grid()
plt.legend()
plt.show()


plt.plot(Pres_elecs, august_percent_changes, label='August Pre-Election Trend', marker = 'X')
plt.xlabel('Election Year')
plt.ylabel('Percentage Change from January')
plt.title('Pre-Election Trends: August Percentage Change')
plt.grid()
plt.legend()
plt.show()

plt.plot(Pres_elecs, september_percent_changes, label='September Pre-Election Trend', marker = 'X')
plt.xlabel('Election Year')
plt.ylabel('Percentage Change from September')
plt.title('Pre-Election Trends: September Percentage Change')
plt.grid()
plt.legend()
plt.show()

plt.plot(Pres_elecs, october_percent_changes, label='October Pre-Election Trend', marker = 'X')
plt.xlabel('Election Year')
plt.ylabel('Percentage Change from October')
plt.title('Pre-Election Trends: October Percentage Change')
plt.grid()
plt.legend()
plt.show()
