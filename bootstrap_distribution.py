"""
Bootstrapping is a resampling technique that randomly selects a set of data points,
 allowing the same data point to potentially be selected more than once,
 to create an approximate sampling distribution. In contrast, the earlier introduced randomization test
 only allowed each data point to be selected once.
 Unlike permutation tests, data from different groups is not mixed.
 In resampling, allowing selection more than once is commonly called with replacement.
 A statistic is calculated for each resample and a bootstrap distribution of that statistic is calculated.
Bootstrapping assumes that the data is representative of the sampling distribution.
Unlike a randomization test, bootstrapping can make inferences on a single sample.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Weights of males and females
male = np.array([245, 200, 145, 180, 250, 205, 140, 195, 170, 175])
female = np.array([165, 120, 170, 190, 195, 120, 170, 140, 130, 150])

# Calculate the difference in means for the sample data
SampleStatistic = np.mean(male) - np.mean(female)
print("Sample Stat:", SampleStatistic)

i = 0
results = np.zeros((10000, 1))

# Set a seed to get same results, edit seed to get different randomizations and results
np.random.seed(1234)

# The command "replace" in random.choice allows selection with  replacement in each of the samples.
while i < 10000:
    data_male = np.random.choice(male, 10, replace=True)
    data_female = np.random.choice(female, 10, replace=True)
    results[i] = np.mean(data_male)-np.mean(data_female)
    i += 1

# Create a histogram of the statistic's distribution
plt.hist(results, bins=20, range=(0, 80), edgecolor='black')
plt.title("Distribution of the difference in means")
plt.show()

# Confidence interval using t-distribution with degrees of freedom n_1 - 1
alpha = 0.05
n1 = len(male)  # 10
n2 = len(female)  # 10

se = np.std(results)
ci_l = SampleStatistic - stats.t(df=n1-1).ppf((1-alpha/2))*se
ci_u = SampleStatistic + stats.t(df=n1-1).ppf((1-alpha/2))*se
print(ci_l)
print(ci_u)

# The confidence interval can also be found directly from the bootstrap distribution
# using the percentile function.
alpha = 0.05
n1 = len(male)  # 10
n2 = len(female)  # 10

ci_lb = np.percentile(results, (alpha/2)*100)
ci_ub = np.percentile(results, (1-(alpha/2))*100)
print(ci_lb)
print(ci_ub)