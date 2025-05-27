import pandas as pd
import scipy.stats as st

"""
The ztest(x1, x2, value = 0) function can also be used to perform a two-sample 
z-test for means. However, the value parameter should be set to 0.
 The function requires the statsmodels.stats.weightstats library to be imported and takes two inputs. 
The first input x1 is an array containing sample observations from one population and the second input x2 is also an array 
containing sample observations from another population. The function returns the z-score and the two-tailed p-value.

The st.ttest_rel(x, y) function takes two arrays or DataFrame columns x and y with the same length as inputs and returns the 
t-statistic and the corresponding two-tailed p-value as outputs.

The st.ttest_ind(x, y) command takes two arrays or DataFrame columns x and y as inputs and 
returns the t-statistic and the corresponding two-tailed p-value as outputs.

"""

titanic = pd.read_csv("titanic.csv")

male = titanic[titanic['Sex'] == 'male']['Fare']
female = titanic[titanic['Sex'] == 'female']['Fare'] # Subset on Sex = "female"

t_test_results = st.ttest_ind(male, female) # Use the correct t-test to compare values of Fare for both subsets

print(f'Ttest_indResult(statistic={t_test_results[0]:.6E}, pvalue={t_test_results[1]:.6E})')