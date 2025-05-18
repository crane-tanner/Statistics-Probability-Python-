from scipy.stats import binom
"""
Given a fair coin flipped 100 times, the program gives the probability of 
a user-defined number of flips coming up heads, 
then gives the mean and variance of the binomial distribution
"""
print("Enter k value for flips coming up heads")
k = int(input())  # user-defined number of successes

n = 100  # trials
p = 0.5  # probability of getting heads or tails per coin toss

prob = binom.pmf(k, n, p)
print("Probability:", prob)

mean = binom.stats(n, p, moments='m')
print("Mean:", mean)
var = binom.stats(n, p, moments='v')
print("Variance:", var)



