import numpy as np
from scipy.stats import poisson


x = int(input()) # user-defined number of successes
lam = int(input()) # lambda average rate of success

np.random.seed(seed=123)

r1 = poisson.rvs(lam, size=8)

r2 = poisson.rvs(lam, size=20)

r3 = poisson.rvs(lam, size=100)

cp = poisson.cdf(x, lam) # Calculate the cumulative probability of x or fewer successes for a Poisson distribution with a mean of lam
print(f'Cumulative probability is {cp:.6f}')

mean_theor = poisson.stats(lam, moments='m') # Calculate the theoretical mean of the Poisson distribution
print("Theoretical mean is", mean_theor)

mean_r1 = np.mean(r1)
print(f'Mean of r1 is {mean_r1:.6f}')

mean_r2 = np.mean(r2)
print(f'Mean of r2 is {mean_r2:.6f}')

mean_r3 = np.mean(r3)
print(f'Mean of r3 is {mean_r3:.6f}')