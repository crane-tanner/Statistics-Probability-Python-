"""
The ztest(x1, value) function is used to perform a one-sample
z-test for means. The function requires the statsmodels.stats.weightstats library to be imported,
and takes two inputs.
The first input x1 is an array and the second input value is the hypothesized value of the
population mean.

The function returns the
z-score and the two-tailed
p-value. The one-tailed
p-value is the two-tailed
p-value divided by 2.

The scipy.stats.ttest_1samp(a, popmean, alternative) function takes
in an array or a column of a DataFrame, the hypothesized population mean,
and the direction of the alternative hypothesis as inputs and gives the
t-test statistic and
p-value as outputs.

The alternative hypothesis default is alternative="two-sided",
but can be specified as either "greater" or "less" for a one-tailed alternative hypothesis

The proportions_ztest(count, nobs, value, prop_var = value) function is used to perform a one-sample 
-test for proportions. The function requires the statsmodels.stats.proportion library to be imported, 
and takes four inputs. st input count is the number of observations meeting some condition, 
the second input nobs is the total number of observations, the third input is the hypothesized value
 of the population proportion, and the fourth is the hypothesized value of the 
 population proportion which is used to calculate the variance of the estimate. 
 The function returns the z-score and the two-tailed p-value.

"""
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd

gpa = pd.read_csv("gpa.csv")

value = float(input())
cutoff = float(input())

student_gpa = gpa['gpa']

counts = student_gpa[student_gpa > cutoff].size  # Determine the number of students with a gpa higher than cutoff

nobs = student_gpa.size  # Determine the total number of students

ztest = proportions_ztest(counts, nobs, value)  # Perform z-test for counts, nobs, and value
print(f'({ztest[0]:.6E}, {ztest[1]:.6E})')
# Determine the correct conclusion
if ztest[1] < value:  # Finish the if statement
    print(
        f'The two-tailed p-value, {ztest[1]:.6E}, is less than \u03B1. Thus, sufficient evidence exists to support the hypothesis that the proportion is different from {value}')
else:
    print(
        f'The two-tailed p-value, {ztest[1]:.6E}, is greater than than \u03B1. Thus, insufficient evidence exists to support the hypothesis that the proportion is different from {value}')

"""
p1 = 98/136 # sample proportion
p0 = 0.67 # hypothesized proportion
n = 136 # sample size
# z = (p1 - p0) / np.sqrt((p0*(1-p0))/n) # z-statistic
z = proportions_ztest(98, 136, 0.67)
print(z)
"""
