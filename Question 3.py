# What are the pre-election trends that are common in the months leading up to the election?

import numpy as np

path = 'Macrotrends-s-p-500-index-daily.csv'

data = np.loadtxt(path, skiprows = 10, delimiter = ',')

print(data)
