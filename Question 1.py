import numpy as np
import matplotlib.pyplot as plt

# 1. How does the presidential election affect the general trend of the S&P 500 compared to the years surrounding it?

## Get the file path for the historical data
path = 'Macrotrends-s-p-500-index-daily.csv'

## Load in historical the daily closing values
closing_values = np.loadtxt(path, skiprows=10, delimiter=',')
print(closing_values)