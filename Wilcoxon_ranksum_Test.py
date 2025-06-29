import numpy as np
from scipy import stats

# Mean sister chromatid exchange data
x = np.array([9.84,9.40,8.20, 8.24, 9.20,8.55,8.52,8.12]) # Asian
y = np.array([8.27,8.20,8.25,8.14,9.00,8.10,7.20,8.32,7.70]) # Caucasian

W, p = stats.mannwhitneyu(x, y, alternative = 'two-sided')
print("W = ", W)
print("p-value = ", p)

