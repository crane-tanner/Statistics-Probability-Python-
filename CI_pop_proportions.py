"""
A confidence interval can also be calculated from raw data. An example imports data from ExamScores.csv into 
a DataFrame, filters based on a minimum score, and finds the confidence interval.
p = 103.0/1000.0
n = (1.645 / 0.023) ** 2 * (0.5 * (1 - 0.5))
m = 1.960 * np.sqrt(p*(1-p) / 1000)
print(n)
"""

import pandas as pd
from scipy import stats as st

# Import necessary modules

age = int(input())

titanic = pd.read_csv('titanic.csv')

south = titanic[titanic['Embarked'] == 'S']  # Take the subset of the data where Embarked = "S"

n1 = south.shape[0]  # Find total number in subset

x1 = south[south['Age'] > age].shape[0]  # Find number in subset where Age > age

p1 = x1 / n1  # Calculate proportion
print(f'Sample proportion is {p1:.6f}')

stderr = (p1 * (1 - p1) / n1) ** 0.5  # Calculate standard error

conf_int = st.norm.interval(0.95, p1, stderr)  # Find 95% confidence interval
print(f'({conf_int[0]:.6f}, {conf_int[1]:.6f})')

# Find proportion for full data
n2 = titanic.shape[0]  # Count number in data set
x2 = titanic[titanic['Age'] > age].shape[0]  # Count number in full data set where Age > age
p2 = x2 / n2  # Calculate proportion

# Determine if the actual proportion falls within the 95% confidence interval
if conf_int[0] <= p2 <= conf_int[1]:
    print(f'Actual proportion, {p2:.6f}, is within the 95% confidence interval')
else:
    print(f'Actual proportion, {p2:.6f}, is not within the 95% confidence interval')
