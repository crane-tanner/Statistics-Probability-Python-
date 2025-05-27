import numpy as np
from statsmodels.stats.proportion import proportions_ztest

"""
The proportions_ztest() function performs a z-test between two samples. 
The function requires the statsmodels.stats.proportion library to be imported, and takes two arrays, instead of two integers, 
as parameters.
 The first array is the number of individuals meeting some condition in each group, 
 and the second array is the total number of individuals in each group.

The function returns the z-statistic and the two-tailed p-value. To specify a one-tailed 
p-value, add alternative='smaller' or alternative='larger'
"""

counts = [519, 591]
n = [800, 1000]

print("p1:", 519/800, "\n")
print("p2:", 591/1000, "\n")
overall_p = ((519+591)/1800)
print("Overall p:", overall_p, "\n")
print("Standard error", np.sqrt(overall_p*(1-overall_p)*(1/800 + 1/1000)))
print(proportions_ztest(counts, n, alternative='larger'))

