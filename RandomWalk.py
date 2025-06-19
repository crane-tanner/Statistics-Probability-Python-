import random as rand
from math import log
import numpy as np
import matplotlib.pyplot as plt

"""
# Random walk with drift 
# Takes in the number of steps num and outputs an array of size num+1 and the position at each step
def rand_walk_drift(num, a):
    L = [0]
    pos = 0
    for i in range(num):
        # a is the drift term
        pos = a + pos + rand.gauss(0, 1)
        L.append(pos)
    return np.array(range(num+1)), L

rand.seed(123)

plt.title('Random walk with drift', fontsize=20)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Position', fontsize=12)
plt.plot(rand_walk_drift(100, 0.5)[0], rand_walk_drift(100, 0.5)[1])
plt.show()
"""

"""
# random walk with deterministic trend
def rand_walk_det(num, a, b):
    L = [0]
    pos = 0
    for i in range(num):
        # a is the drift term
        pos = a + b*i + rand.gauss(0, 1)
        L.append(pos)
    return np.array(range(num+1)), L

rand.seed(123)

plt.title('Random walk with \ndeterministic trend', fontsize=20)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Position', fontsize=12)
plt.plot(rand_walk_det(100, 0.05, 0.3)[0], rand_walk_det(100, 0.05, 0.3)[1])
plt.show()

"""
# Random walk with drift and deterministic trend
def rand_walk_drift_det(num, a, b):
    L = [0]
    pos = 0
    for i in range(num):
# a is the drift term
        pos = a + b*i + pos +  rand.gauss(0,1)
        L.append(pos)
    return np.array(range(num+1)), L

rand.seed(123)

plt.title('Random walk with drift \n and deterministic trend', fontsize=20)
plt.xlabel('Steps', fontsize=12)
plt.ylabel('Position', fontsize=12)
plt.plot(rand_walk_drift_det(100, 0.05, 0.3)[0],rand_walk_drift_det(100, 0.05, 0.3)[1])
plt.show()