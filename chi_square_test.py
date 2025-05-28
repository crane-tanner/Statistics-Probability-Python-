from scipy import stats
from scipy.stats import chi2_contingency
import numpy as np

"""
gilbert = np.array([[40,217],[34,1350]])
print(gilbert)

chi, pvalue, dof, ex = chi2_contingency(gilbert, correction=False)

print(chi)
print(pvalue)
print(dof)
"""

# Construct a contingency table
table = np.array([[580, 1019], [289,169], [503, 178], [618,208], [742, 1148]])
print(table)
chi2, p, df, ex = chi2_contingency(table, correction=False) # Calculate the test statistic and p-value

print(f'{chi2:.6E}')
print(f'{p:.6E}')

# Determine if null hypothesis is rejected or not
if p <= 0.01: # Write appropriate if statement
    print("The hypothesis that tea and coffee are drunk with the same frequency is rejected.")
else:
    print("The hypothesis that tea and coffee are drunk with the same frequency is not rejected.")
