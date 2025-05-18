from scipy.stats import hypergeom
import matplotlib.pyplot as plt
"""
Given user defined numbers k and n, if n cards are drawn from a deck, the program gives the probability 
that at least k cards are black.
"""
n = int(input())
k = int(input())

N = 52
x = 26

P = hypergeom.pmf(k, N, x, n, loc=0)
print("Probability:", P)

cp = 1 - hypergeom.cdf(k-1, N, x, n)
print("Probability at least k cards are black:", cp)

