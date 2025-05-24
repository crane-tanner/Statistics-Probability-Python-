import scipy.stats as st
import numpy as np

"""
The norm.interval() function is used to find a confidence interval for a normally distributed variable.
The function takes the desired confidence level, the sample mean, and the standard error as parameters.
0.
The t.interval() function is used to find a confidence interval for a variable with a t-distribution. 
The function takes the desired confidence level, the degrees of freedom, the mean, and the standard error as parameters.
"""

# Get user defined mean and standard deviation
mean_def = int(input())
sd_def = int(input())

np.random.seed(seed=123)

# Generate 100 random numbers with a normal distribution with a mean of mean_def and a standard deviation of sd_def
r = st.norm.rvs(mean_def, sd_def, size=100)

mean = np.mean(r)
print(f'Sample mean is {mean:.2f}')

# Calculate the standard error of r
std_dev = np.std(r)
stderr = std_dev / np.sqrt(len(r))

int1 = st.norm.interval(0.95, mean, stderr)
# Calculate the 95% confidence interval using the sample mean and standard error
print(f'({int1[0]:.2f}, {int1[1]:.2f})')

# Determine if the user defined mean falls within the 95% confidence interval
if int1[0] < mean_def < int1[1]:
    print("User defined mean,", mean_def, ", is within the 95% confidence interval")
else:
    print("User defined mean,", mean_def, ", is not within the 95% confidence interval")
