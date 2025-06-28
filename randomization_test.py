import numpy as np
import matplotlib.pyplot as plt

# Weights of males and females
male = np.array([245, 200, 145, 180, 250, 205, 140, 195, 170, 175])
female = np.array([165, 120, 170, 190, 195, 120, 170, 140, 130, 150])

# Calculate the difference in means for the sample data
SampleStatistic = np.mean(male) - np.mean(female)
print("Sample Stat:", SampleStatistic)

"""
Null hypothesis: There is no difference between the mean weight of males and mean weight of females.
Any of the observed weights are equally likely of a male or a female. 
To test this we first combine the data samples
"""
X = np.concatenate((male, female))
print("Combined array:",X)

# Conduct 10,000 randomizations
i = 0
results = np.zeros((10000, 1))
while i < 10000:
    np.random.shuffle(X)
    results[i] = np.mean(X[0:10])-np.mean(X[10:20])
    i+=1

# Histogram of the randomized test statistic's distribution
plt.hist(results, bins=range(-55,60,5), edgecolor='black')  # range=(0,80),
plt.title("Distribution of the difference in means \n under the null hypothesis")
plt.show()

pvalue = np.sum(abs(results) >= SampleStatistic)/10000
print("P-value:", pvalue)

# Create a histogram of the test statistic's distribution
# Denote the results equal to the test statistic or more extreme

extreme = results[abs(results) >= SampleStatistic]

plt.hist(results, bins=range(-55, 60, 5), edgecolor='black')  # range=(0,80),
plt.hist(extreme, bins=range(-55, 60, 5), edgecolor='black')
plt.title("Distribution under the null hypothesis \n with |mean diff| $\geq$ 35")
plt.show()

