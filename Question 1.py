import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from fontTools.merge.util import first
from matplotlib.pyplot import xlabel
from numpy.ma.core import greater

# 1. How does the presidential election affect the general trend of the S&P 500 compared to the years surrounding it?

## Get the file path for the historical data
path = 'Macrotrends-s-p-500-index-daily.csv'

## Load in historical the daily closing values
data = pd.read_csv(path)

## gets the dates in its own vector
date = data['Date']
##date = np.array(date)

## gets the closing values in its own vector
closing_value_np = data['Closing Value']
closing_value_np = np.array(closing_value_np)

closing_value = []
for value in closing_value_np:
    x = float(value)
    closing_value.append(x)

## print(date)
## print(closing_value)
## Create a vector that includes every year

years = []
for year in range(1928,2025):
   years.append(year)

##print(years)

## create a vector that include every election year
M_elections = []
Pres_elecs = []
for M_election in range(len(years)): ## gets every even year (presidential and mid term)
    if M_election % 2 == 0:
        M_elections.append(years[M_election])
for pres_elec in range(len(M_elections)): ## takes those years and returns only presidential elections
    if pres_elec % 2 == 0:
        Pres_elecs.append(M_elections[pres_elec])
#print(M_elections)
##print(Pres_elecs)

## creating a vector of strings for later
Pres_elec_str = []
for x in Pres_elecs:
    Pres_elec_str.append(str(x))

## turn the closing values into differences, so we can see the variance
## closing_diff = []
## for value in range(len(closing_value) - 1):
##   difference = closing_value[value] - closing_value[value - 1]
##   closing_diff.append(difference)  # a vector with the change from the day before it

#make the years strings
years_str = []
for year in years:
    x = str(year)
    years_str.append(x)

## Create an array with the starting date for each year
first_occur =[]

for year_str in years_str:
    for entry in date:
        if year_str in entry:
            first_occur.append(entry)
            break

##print(first_occur)

## Create an array with the index of the first date for each year
first_index = []
for day in first_occur:
    for i in range (0,len(date)):
        if day == date[i]:
            first_index.append(i + 2)

##print(first_index)

## Create an array with the opening value for each year
open_value = []
for index in first_index:
    open_value.append(closing_value[index - 2])
#print(open_value)


## Create an array with the last date for each year
last_occur = []

for year_str in years_str:
    for entry in reversed(date):
        if year_str in entry:
            last_occur.append(entry)
            break

##print(last_occur)

## Create an array with the index of the first date for each year
last_index = []
for day in last_occur:
    for i in range (0,len(date)):
        if day == date[i]:
            last_index.append(i + 2)

##print(last_index)

## Create an array with the opening value for each year
end_value = []
for index in last_index:
    end_value.append(closing_value[index - 2])
#print(end_value)

## end_value and open_value have the closing and opening values for every year the S&P exsited
##print(len(end_value))
##print(len(open_value))

## Here we find the changes in these years
variance = []
for i in range(0, len(end_value)):
    difference = end_value[i] - open_value[i]
    variance.append(difference)
print(variance)


## just the variance in election years
elec_variance = [] ## all election years
pres_variance = [] ## presidential election years
off_variance = [] ## non presidential years
for i in range(0,len(variance)):
    if i % 2 == 0:
        elec_variance.append(variance[i])
    else:
        off_variance.append(variance[i])
for i in range(0, len(elec_variance)):
    if i % 2 == 0:
        pres_variance.append(elec_variance[i])
print('pres' + '\n',pres_variance)
print('off' + '\n',off_variance)

## create a vector for the years before election
before_variance = []
after_variance = []
before_variance.append(0)
for i in range(0,len(off_variance)):
    if i % 2 == 0:
        after_variance.append(off_variance[i])
    else:
        before_variance.append(off_variance[i])
after_variance.append(0)

print('before' + '\n', before_variance)
print('after' + '\n', after_variance)


## off_variance has the variance in years next to presidential elections.
## in this list terms 0 and 1 would be the years before and then after an election
## pres_variance shows the variance for years with presidential elections

## we want to see if presidential years have market improvement than the year before or after it
## to determine this we will create a list counting the amount of times the presidential year is greater than that
## before it and a list counting the amount of times it is greater than the year following. if it is consistently higher
## it will show that during presidential elections the stock market preforms better

## we will plot the differences as well


##creating the vector that will show the year prior and after

comp_before = []
comp_after = []
#print(len(before_variance))
#print(len(after_variance))
#print(len(pres_variance))

# this creates vectors with 1 and -1s, a -1 means the election year had the lower closing value and the 1 means the
# election year had the higher value
for i in range(0, len(before_variance)):
    if before_variance[i] < pres_variance[i]:
        comp_before.append(1)
    elif before_variance[i] > pres_variance[i]:
        comp_before.append(-1)
    if after_variance[i] < pres_variance[i]:
        comp_after.append(1)
    elif after_variance[i] > pres_variance[i]:
        comp_after.append(-1)

print('before' + '\n', comp_before)
print('after' + '\n', comp_after)

## count the number of times the election year was greater for each condition
greater_before = 0
lower_before = 0
greater_after = 0
lower_after = 0
for i in comp_before:
    if i == 1:
        greater_before = greater_before + 1
    else:
        lower_before = lower_before + 1
for i in comp_after:
    if i == 1:
        greater_after = greater_after + 1
    else:
        lower_after = lower_after + 1
print(greater_before , '/', len(comp_before))
print(greater_after ,'/', len(comp_after))